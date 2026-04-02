import serial

def init_serial(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate, timeout=0.1)
        print(f"成功连接到串口: {port}")
        return ser
    except Exception as e:
        print(f"警告：无法打开串口 {port}。")
        return None

def send_to_hand(ser, angles):
    if ser and ser.is_open:
        data = []
        for a in angles:
            data += [a & 0xFF, (a >> 8) & 0xFF]
        addr = 1486
        frame = [0x01, len(data) + 3, 0x12, addr & 0xFF, (addr >> 8) & 0xFF] + data
        checksum = sum(frame) & 0xFF
        ser.write(bytes([0xEB, 0x90] + frame + [checksum]))
