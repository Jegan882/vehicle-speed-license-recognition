import cv2

def draw_zones(frame):
    cv2.line(frame, (0, 300), (frame.shape[1], 300), (0, 0, 255), 2)
    cv2.line(frame, (0, 500), (frame.shape[1], 500), (255, 0, 0), 2)
    return frame
