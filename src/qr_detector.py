import cv2

def detect_qr(frame):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        return data.strip()
    return None