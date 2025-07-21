import cv2
from ultralytics import YOLO

model = YOLO('models/yolov8n.pt')
cap = cv2.VideoCapture('data/input_video.mp4')
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imwrite(f'outputs/frame_{frame_id:04d}.jpg', frame)
    frame_id += 1
cap.release()
