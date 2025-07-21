from ultralytics import YOLO

plate_model = YOLO('models/lp_detector.pt')

def extract_plate(frame, vehicle_bbox):
    x1, y1, x2, y2 = vehicle_bbox
    vehicle_img = frame[y1:y2, x1:x2]
    results = plate_model(vehicle_img)
    for r in results:
        for b in r.boxes.xyxy:
            px1, py1, px2, py2 = map(int, b)
            return vehicle_img[py1:py2, px1:px2]
