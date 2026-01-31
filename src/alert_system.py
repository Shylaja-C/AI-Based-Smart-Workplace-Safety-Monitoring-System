import cv2
import os

def audio_alert(message):
    # Simple audio alert using system beep or print
    print(f"Audio Alert: {message}")
    # For Windows, use winsound.Beep(1000, 500) but import winsound
    # For now, print

def visual_alert(frame, message):
    cv2.putText(frame, message, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame