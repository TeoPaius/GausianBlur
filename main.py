import cv2 as cv2

from Core import Core

if __name__ == '__main__':

    imgParser = Core()
    imgParser.readFile("cactusmic.png")

    imgParser.parseImg()
    imgParser.showImg()

    cv2.waitKey()
