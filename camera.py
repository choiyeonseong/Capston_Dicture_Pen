import cv2
import os
import configparser

import time
from scipy.stats import wasserstein_distance
from imageio import imread
import numpy as np
import threading

from gui_selectedword_window import selected_window
from ocr import ocrToStr

img_path = os.path.dirname(os.path.realpath(__file__))+os.sep+'resource'+os.sep +'image'
config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__))+os.sep + 'envs' + os.sep + 'property.ini')

def ToDo():
    print("Timer")
    timer = threading.Timer(2, ToDo)
    timer.start()

def get_histogram(img):
    h, w = img.shape
    hist = [0.0] * 256
    for i in range(h):
        for j in range(w):
            hist[img[i, j]] += 1
    return np.array(hist) / (h * w)

def img_diff() :
    a = imread('./resource/image/image1.jpg', pilmode='L')
    b = imread('./resource/image/image2.jpg', pilmode='L')
    a_hist = get_histogram(a)
    b_hist = get_histogram(b)
    dist = wasserstein_distance(a_hist, b_hist)
    result = (dist<0.0003)
    return result

def img_processing (img_file):
    src = cv2.imread(img_file, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 종이에 해서 그런지 그레이스케일만 하는게 제일 나음
    #  threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    #  blur = cv2.GaussianBlur(threshold,(5,5),0)
    cv2.imwrite('./resource/image/image.jpg', gray)

def img_trim(img) :
    x = 30; y = 230;
    w = 580; h = 150;
    img_trim = img[y:y+h,x:x+w]
    cv2.imwrite('./resource/image/image.jpg',img_trim)


def cam_on() :
    cam = cv2.VideoCapture(0)  # 카메라 연결
    cv2.namedWindow("Dicture pen")
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    while (True):
        ret, frame = cam.read()
        ret, frame2 = cam.read()
        cv2.line(frame, (40,240), (600,240),(255,255,255),3) #세로
        cv2.line(frame, (40,360), (600,360),(255,255,255),3) #가로
        cv2.imshow('Dicture pen', frame)

        if not ret:
            print('카메라를 켜주세요')
            break

        k = cv2.waitKey(1)

        if k % 256 == 27: #취소는 ESC
            print("카메라를 끕니다")
            cam.release()
            cv2.destroyAllWindows()
            break

        if k % 256 == 32: # Space
            cv2.imwrite("./resource/image/image1.jpg", frame2) # 캡쳐1
            time.sleep(1)
            ret, frame2 = cam.read()
            cv2.imwrite("./resource/image/image2.jpg", frame2) # 캡쳐2
            time.sleep(1)

            img_diff() # image1이랑 image2 비교했을때 0.0003 미만이면 True 반환
            if img_diff() == True :
                img_file = img_path + os.sep + 'image1.jpg' # True 일 경우 image1으로 이미지 전처리
                img_processing(img_file)

                trim_img = cv2.imread("./resource/image/image1.jpg") # line 대로 잘라내기
                img_trim(trim_img)

                ocr_img=cv2.imread('./resource/image/image.jpg') #ocr 해서 텍스트 추출
                sword,smean=ocrToStr(ocr_img)  #get_dic_serach 까지 해서 단어랑 뜻 출력력
    return sword,smean



if __name__ == "__main__":
   sword,smean=cam_on()
   selected_window(sword,smean)



