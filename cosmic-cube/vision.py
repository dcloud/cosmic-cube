import cv2
import numpy as np


class VisionImage(object):
    lines_rho = 1
    lines_theta = np.pi/180.0
    lines_threshold = 2
    lines_min_length = 80
    lines_max_gap = 1
    rectangle_height = 20
    """VisionImage as read into an numpy ndarray by opencv"""
    def __init__(self, filename, autoload=True):
        super(VisionImage, self).__init__()
        self.filename = filename
        self.otsu = None
        self.original = None
        self.grayscale = None
        self.edges = None
        self.lines = None
        self.rectangles = None
        if autoload:
            self._read_image()

    def _read_image(self):
        self.original = cv2.imread(self.filename, cv2.CV_LOAD_IMAGE_UNCHANGED)
        self.grayscale = cv2.cvtColor(self.original, cv2.cv.CV_BGR2GRAY)

    def load(self):
        self._read_image()

    def _threshold_image(self):
        blur = cv2.GaussianBlur(self.grayscale,(5,5),0)
        self._otsu_thrsh, self.otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    def find_lines(self):
        self._threshold_image()
        self.edges = cv2.Canny(self.otsu,50,150)
        self.lines = cv2.HoughLinesP(self.otsu, self.lines_rho, self.lines_theta, self.lines_threshold, \
                                            np.array([]), self.lines_min_length, self.lines_max_gap)
        return self.lines

    def generate_rectangles(self):
        if self.lines is None:
            self.find_lines()
        self.rectangles = []
        flat_arr = self.lines.squeeze()
        for line in flat_arr:
            x1,y1,x2,y2 = line
            # opencv rectangles draw from top-left tp bottom-right.
            y_vals = sorted([y1, (y1+self.rectangle_height)])
            x_vals = sorted([x1, x2])
            self.rectangles.append(zip(x_vals, y_vals))



