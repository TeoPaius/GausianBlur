import cv2 as cv2
import asyncio

from Core import Core

if __name__ == '__main__':

    imgParser = Core()
    imgParser.readFile("cactusmic.png")

    asyncio.run(imgParser.parseImg())
    imgParser.showImg()

    cv2.waitKey()
