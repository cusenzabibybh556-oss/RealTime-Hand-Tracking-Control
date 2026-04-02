# 📂 Pre-trained Model Weights

The system requires two models from the **OpenMMLab RTMPose Series**. Please download the checkpoints from the official Model Zoo:

### 1. Hand Detector (RTMDet)
- **Model**: RTMDet-Nano
- **Source**: [MMPose RTMDet Hand Project](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose)
- **Direct Download**: [rtmdet_nano_hand.pth](https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmdet_nano_8xb32-300e_hand-267f9c8f.pth)

### 2. Hand Pose Estimator (RTMPose)
- **Model**: RTMPose-M (Hand5)
- **Source**: [RTMPose Hand Configs](https://github.com/open-mmlab/mmpose/tree/main/configs/hand_2d_keypoint/rtmpose)
- **Direct Download**: [rtmpose-m_hand5.pth](https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-hand5_pt-aic-coco_210e-256x256-74fb594_20230320.pth)

---
### Troubleshooting
If the direct download links fail:
1. Visit the [MMPose Model Zoo](https://mmpose.readthedocs.io/en/latest/model_zoo.html).
2. Search for **RTMPose-M** and **RTMDet-Nano**.
3. Download the `.pth` files and move them to this `/weights` directory.
