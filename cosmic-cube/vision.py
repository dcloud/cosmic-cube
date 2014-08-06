import cv2
from cv2 import cv as cv
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
        self._otsu = None
        self._otsu_iplimage = None
        self._original = None
        self._original_iplimage = None
        self._grayscale = None
        self._grayscale_iplimage = None
        self.edges = None
        self.lines = None
        self.rectangles = None
        if autoload:
            self._read_image()

    @property
    def original(self):
        if self._original is None:
            self._read_image()
        return self._original

    @property
    def original_iplimage(self):
        if self._original_iplimage is None:
            self._original_iplimage = self._array_to_iplimage(self.grayscale, cv.IPL_DEPTH_8U, 3)
        return self._original_iplimage

    @property
    def grayscale(self):
        if self._grayscale is None:
            self._read_image()
        return self._grayscale

    @property
    def grayscale_iplimage(self):
        if self._grayscale_iplimage is None:
            self._grayscale_iplimage = self._array_to_iplimage(self.grayscale, cv.IPL_DEPTH_8U, 1)
        return self._grayscale_iplimage

    @property
    def otsu(self):
        if self._otsu is None:
            self._threshold_image()
        return self._otsu

    @property
    def otsu_iplimage(self):
        if self._otsu_iplimage is None:
            self._otsu_iplimage = self._array_to_iplimage(self.otsu, cv.IPL_DEPTH_8U, 1)
        return self._otsu_iplimage

    def _array_to_iplimage(self, image_arr, depth, num_channels):
            size = (image_arr.shape[1], image_arr.shape[0])
            adjustor = 1 if num_channels == 3 else 3
            # width_step = image_arr.dtype.itemsize * num_channels * self.original.shape[1] + adjustor
            width_step = image_arr.dtype.itemsize * num_channels * image_arr.shape[1]
            iplimage = cv.CreateImageHeader(size, depth, num_channels)
            cv.SetData(iplimage, image_arr.tostring(), width_step)
            return iplimage

    def _read_image(self):
        self._original = cv2.imread(self.filename, cv2.CV_LOAD_IMAGE_UNCHANGED)
        self._grayscale = cv2.cvtColor(self._original, cv2.cv.CV_BGR2GRAY)

    def load(self):
        self._read_image()

    def _threshold_image(self):
        blur = cv2.GaussianBlur(self.grayscale,(5,5),0)
        self._otsu_thrsh, self._otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

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



