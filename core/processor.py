import numpy as np

def calculate_angles(keypoints, palm_configs):
    kp = keypoints[0]
    wrist = kp[0]
    palm_root = kp[9]
    
    # --- 核心亮点：空间归一化 (Spatial Normalization) ---
    palm_size = np.linalg.norm(palm_root - wrist) + 1e-6
    
    finger_tips = [20, 16, 12, 8, 4]
    current_angles = []

    for i, tip_idx in enumerate(finger_tips):
        dist = np.linalg.norm(kp[tip_idx] - wrist)
        ratio = dist / palm_size
        
        # 线性映射逻辑
        cfg = palm_configs[i]
        val = (ratio - cfg[0]) / (cfg[1] - cfg[0]) * 1000
        current_angles.append(int(np.clip(val, 0, 1000)))
    
    current_angles.append(1000) 
    return np.array(current_angles)
