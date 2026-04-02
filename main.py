import cv2
import time
import numpy as np
from mmengine.registry import DefaultScope
from mmpose.apis import inference_topdown, init_model
from mmdet.apis import inference_detector, init_detector

from configs.settings import *
from core.processor import calculate_angles
from core.hardware import init_serial, send_to_hand

def main():
    ser = init_serial(SERIAL_PORT, BAUD_RATE)
    det_model = init_detector(DET_CFG, DET_CKPT, device=DEVICE)
    pose_model = init_model(POSE_CFG, POSE_CKPT, device=DEVICE)
    
    cap = cv2.VideoCapture(0)
    last_angles = np.array([500] * 6)
    last_send_time = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break

        with DefaultScope.overwrite_default_scope('mmdet'):
            det_result = inference_detector(det_model, frame)
            bboxes = det_result.pred_instances.bboxes[det_result.pred_instances.scores > 0.8].cpu().numpy()

        if len(bboxes) > 0:
            with DefaultScope.overwrite_default_scope('mmpose'):
                pose_results = inference_topdown(pose_model, frame, bboxes)
            
            if len(pose_results) > 0:
                kpts = pose_results[0].pred_instances.keypoints
                target_angles, ratios = calculate_angles(kpts, FINGER_CONFIGS)
                
                # EMA
                smooth_angles = (target_angles * SMOOTH_FACTOR + last_angles * (1 - SMOOTH_FACTOR)).astype(int)
                
                # Deadband
                now = time.time()
                if now - last_send_time > SEND_INTERVAL:
                    if np.abs(smooth_angles - last_angles).max() > DEADBAND_LIMIT:
                        send_to_hand(ser, smooth_angles)
                        last_angles = smooth_angles
                        last_send_time = now
                        print(f"Ratios: {ratios} | Synchronizing...")

        cv2.imshow('System View', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    if ser: ser.close()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
