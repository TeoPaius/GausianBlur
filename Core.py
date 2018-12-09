import cv2 as cv2


class Core:
    def __init__(self):
        self.kernel = 1 / 256 * [[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],
                                 [1, 4, 6, 4, 1]]
        self.nrTh = 4

    def readFile(self, fileName):
        self.img = cv2.imread(fileName)

    def writeImg(self, fileName):
        cv2.imwrite(fileName, self.img)

    def parseImg(self):
        pass

    def showImg(self):
        cv2.imshow("SA", self.img)

    def multiplyPx(self, i, j, channel):
        pass