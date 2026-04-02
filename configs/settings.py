# 模型路径
DET_CFG = 'projects/rtmpose/rtmdet/hand/rtmdet_nano_320-8xb32_hand.py'

# 归一化与映射配置 
FINGER_CONFIGS = [
    [0.9, 1.0],  # 小指
    [1.0, 1.4],  # 无名指
    [1.2, 1.6],  # 中指
    [1.2, 1.6],  # 食指
    [0.9, 1.05], # 大拇指
]
DEADBAND_THRESHOLD = 12  # 死区阈值
EMA_ALPHA = 0.7          # EMA滤波权重
