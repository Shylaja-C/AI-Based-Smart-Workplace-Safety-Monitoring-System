import cv2
import time
import threading
from src.database import EmployeeDB
from src.camera import CameraFeed
from src.qr_detector import detect_qr
from src.ppe_detector import detect_ppe
from src.behavior_detector import detect_drowsiness
from src.risk_scorer import calculate_risk
from src.alert_system import audio_alert, visual_alert

class SafetyMonitor:
    def __init__(self, camera_sources=[0]):
        self.db = EmployeeDB()
        self.cameras = [CameraFeed(source) for source in camera_sources]
        self.threads = []
        self.running = True
        self.alerts = []
        self.risk_scores = {}
        self.unsafe_counts = {}

    def monitor_camera(self, camera, camera_id):
        while self.running:
            frame = camera.get_frame()
            if frame is None:
                continue

            # Detect QR
            qr_data = detect_qr(frame)
            if qr_data:
                if self.db.is_authorized(qr_data):
                    print(f"Authorized employee: {qr_data}")
                else:
                    self.trigger_alert(f"Unauthorized person detected: {qr_data}", frame)

            # Detect PPE
            ppe_status = detect_ppe(frame)
            if not ppe_status['helmet'] or not ppe_status['vest']:
                self.trigger_alert("PPE missing", frame)

            # Detect behavior
            if detect_drowsiness(frame):
                self.unsafe_counts[camera_id] = self.unsafe_counts.get(camera_id, 0) + 1
                self.trigger_alert("Drowsiness detected", frame)

            # Calculate risk
            risk = calculate_risk(ppe_status, self.unsafe_counts.get(camera_id, 0))
            self.risk_scores[camera_id] = risk

            # Visual alerts
            for alert in self.alerts:
                frame = visual_alert(frame, alert)
                self.alerts.remove(alert)  # Clear after display

            cv2.imshow(f'Camera {camera_id}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break

        camera.release()

    def trigger_alert(self, message, frame=None):
        print(f"Alert: {message}")
        audio_alert(message)
        self.alerts.append(message)

    def start_monitoring(self):
        for i, camera in enumerate(self.cameras):
            t = threading.Thread(target=self.monitor_camera, args=(camera, i))
            self.threads.append(t)
            t.start()

        for t in self.threads:
            t.join()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    monitor = SafetyMonitor([0])  # Single camera for demo
    monitor.start_monitoring()