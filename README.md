🚗 Vehicle Speed Estimation & License Plate Recognition

A computer vision surveillance pipeline to estimate vehicle speed using zone-based tracking and recognize license plates using enhanced OCR techniques. Built with deep learning, super-resolution, and adversarial text recognition techniques for robust performance under real-world surveillance conditions.

---

## 📌 Project Overview

This project performs:
- **Vehicle detection** using YOLOv8.
- **Zone-based speed estimation** using inter-frame temporal tracking.
- **License plate detection** from detected vehicles.
- **Super-resolution enhancement** using ESRGAN (4x) for clearer OCR input.
- **Adversarial OCR recognition** using both PaddleOCR and Tesseract.
- **Confidence-based selector** for best license number prediction.

---

## 🎯 Objectives

- Build a traditional surveillance-based speed monitoring system.
- Handle low-resolution license plate images using GAN-based enhancement.
- Improve license plate recognition accuracy using hybrid OCR strategy.

---

## 🧠 Technologies Used

- `YOLOv8` – Vehicle and License Plate Detection
- `Real-ESRGAN` – Plate image enhancement
- `PaddleOCR`, `Tesseract` – Dual-path OCR engine
- `OpenCV` – Image I/O and bounding box annotation
- `Python`, `NumPy`, `Torch` – Backend logic

---

## 📁 Folder Structure

```
vehicle-speed-license-recognition/
├── data/                      # Input video/image
├── models/                    # Pretrained weights (YOLO, ESRGAN, LP Detector)
├── outputs/                   # Final output images with annotations
├── scripts/                   # Python scripts
│   ├── detect_vehicle.py
│   ├── track_and_speed.py
│   ├── license_plate_crop.py
│   ├── enhance_esrgan.py
│   ├── ocr_adversarial.py
│   └── utils.py
├── requirements.txt          # Python packages
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/vehicle-speed-license-recognition.git
cd vehicle-speed-license-recognition
```

### 📦 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 📥 3. Download Pretrained Models
Place the following files into the `models/` folder:

| Model               | File Name               | Source |
|--------------------|-------------------------|--------|
| YOLOv8n            | `yolov8n.pt`            | https://github.com/ultralytics/ultralytics/releases |
| LP Detector YOLOv8 | `lp_detector.pt`        | Fine-tuned YOLO model for license plates |
| ESRGAN             | `RealESRGAN_x4plus.pth` | https://github.com/xinntao/Real-ESRGAN |

---

## 🧪 Run the Pipeline

### Step 1: Detect vehicles and generate bounding boxes
```bash
python scripts/detect_vehicle.py
```

### Step 2: Estimate speed via zone tracking
```bash
python scripts/track_and_speed.py
```

### Step 3: Crop and enhance license plate
```python
plate = extract_plate(frame, vehicle_bbox)
plate_sr = enhance_plate(plate)
```

### Step 4: Get final OCR result
```python
plate_number = get_best_ocr_result(plate_sr)
print("Detected Plate:", plate_number)
```

---

## 📸 Sample Output

- Vehicles detected with bounding boxes
- Speed annotation shown
- License plate recognized and labeled

_Example:_
![Sample](outputs/sample_result.png)

---


## 🧑 Author

👨‍💻 Jegan R.V.  
2024 – 2025 Project Implementation

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 📬 Future Improvements

- Integrate automatic vehicle ID tracking (DeepSORT)
- Real-time stream processing
- Log speed violations with image + OCR + timestamp
