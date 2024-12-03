from PIL import Image
import pytesseract
from utils.log_helper import get_logger


def get_captcha_imgtostr(filepath):

    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    captcha_image = Image.open(filepath)
    captcha_text = pytesseract.image_to_string(captcha_image).strip()
    
    logger = get_logger("utils-readcaptcha", "captcha_helper")
    logger.debug(captcha_text)

    return captcha_text
