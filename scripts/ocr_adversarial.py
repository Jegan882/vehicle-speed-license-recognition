from paddleocr import PaddleOCR
import pytesseract

ocr_model = PaddleOCR(use_angle_cls=True, lang='en')

def get_best_ocr_result(image):
    paddle_result = ocr_model.ocr(image)
    paddle_text = paddle_result[0][0][1][0] if paddle_result[0] else ""
    paddle_conf = paddle_result[0][0][1][1] if paddle_result[0] else 0.0
    tesseract_text = pytesseract.image_to_string(image).strip()
    return paddle_text if paddle_conf > 0.85 else tesseract_text

