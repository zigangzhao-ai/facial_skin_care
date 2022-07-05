# -*- coding: UTF-8 -*-
import numpy as np
import cv2

global inpaintMask,img
global point1, point2

def on_mouse(event, x, y, flags, param):
	global img, point1, point2
    img2 = img.copy()
    height1, width1, n = img.shape
    inpaintMask = np.zeros((height1, width1), dtype='uint8')
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0),-1)
        cv2.circle(inpaintMask, point1, 10,  255, -1)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
         cv2.circle(img2, point1, 10, (0, 255, 0),  -1)
         cv2.circle(inpaintMask, point1, 10, 255,  -1)
         cv2.imshow("inpaintMask", inpaintMask)
         cv2.imshow('image', img2)
         cv2.imshow('image0', img)
         dst=cv2.inpaint(img, inpaintMask,  3, cv2.INPAINT_TELEA)
	     cv2.imshow("inpainted image", dst)

def main():
        global img
        img = cv2.imread('3.jpg')
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', on_mouse)
        cv2.imshow('image', img)
        cv2.waitKey(0)

if __name__ == '__main__':
        main()
