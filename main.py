import cv2 as cv2

from Core import Core

if __name__ == '__main__':

    imgParser = Core()
    imgParser.readFile("cactus.jpg")
    cv2.resize(imgParser.img, (300, 300))
    imgParser.showImg()

    cv2.waitKey()
