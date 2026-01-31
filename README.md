# AI-Based Smart Construction Site Safety Monitoring System

This system monitors construction sites for safety using computer vision, detecting PPE, unauthorized persons, and unsafe behaviors.

## Features

- Live camera feed processing
- Employee database with QR code identification
- PPE detection (helmet, safety vest)
- Unsafe behavior detection (drowsiness)
- Real-time risk scoring
- Alert system (audio and visual)
- Modular architecture for scalability

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Download the dlib shape predictor model:
   - Download `shape_predictor_68_face_landmarks.dat` from [dlib models](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Place it in the `models/` directory.

3. (Optional) Add an alert sound file `alert.wav` in `data/` for audio alerts.

4. Populate the employee database by running:
   ```python
   from src.database import EmployeeDB
   db = EmployeeDB()
   db.add_employee('EMP001', 'QR123', 'John Doe')
   ```

## Usage

Run the main script:
```
python src/main.py
```

The system will start monitoring the default camera (source 0). Press 'q' to quit.

For multiple cameras, modify the camera_sources list in main.py.

## Architecture

- `database.py`: Manages employee data
- `camera.py`: Handles camera feeds
- `qr_detector.py`: Detects QR codes
- `ppe_detector.py`: Detects PPE using computer vision
- `behavior_detector.py`: Detects drowsiness
- `risk_scorer.py`: Calculates risk scores
- `alert_system.py`: Handles alerts
- `main.py`: Main application loop

## Scalability

The system uses threading for multiple cameras. For cloud scaling, deploy on edge devices or cloud instances with multiple camera inputs.

## Troubleshooting

- If camera doesn't open, check camera permissions.
- If dlib fails, ensure the model file is present.
- For better PPE detection, train a custom model with YOLO or similar.