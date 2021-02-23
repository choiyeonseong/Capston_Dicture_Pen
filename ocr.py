from pytesseract import *
from PIL import Image
from crawling import get_dic_search


def ocrToStr(img):
    outText = image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c preserve_interword_spaces=1')
    print('+++++++ OCR 결과 +++++++')
    print("단어 : " + outText)


    sword,smean=get_dic_search(outText)
    return sword,smean



