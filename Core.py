import cv2 as cv2
import numpy as np
import asyncio


class Core:
    def __init__(self):
        self.kernel = 1 / 454 * np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],
                                          [100, 4, 6, 4, 100]])
        self.nrTh = 4

    def readFile(self, fileName):
        self.img = cv2.imread(fileName)

    def writeImg(self, fileName):
        cv2.imwrite(fileName, self.img)

    def parseImg(self):
        h = self.img.shape[0]
        w = self.img.shape[1]

        blank_image = np.zeros((h, w, 3), np.uint8)

        for x in range(2, w - 2):
            for y in range(2, h - 2):
                for c in range(0, 3):
                    asyncio.create_task()
                    blank_image[y, x, c] = self.multiplyPx(y, x, c)
                    print(blank_image[y, x, c])

        cv2.imshow('MORI',blank_image)
        cv2.waitKey()

    def showImg(self):
        cv2.imshow("SA", self.img)

    def multiplyPx(self, i, j, channel):

        res = 0

        for kerI in range(0, 5):
            for kerJ in range(0, 5):
                res += self.kernel[kerI, kerJ] * self.img[i - 2 + kerI, j - 2 + kerJ, channel]

        return res
