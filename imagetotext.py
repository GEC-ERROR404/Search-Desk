import re
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


image = cv2.imread(input('Browse file path'))
b, g, r = cv2.split(image)
rgb_img = cv2.merge([r, g, b])
plt.imshow(rgb_img)
plt.title('ORIGINAL IMAGE')
plt.show()
gray = get_grayscale(image)
thresh = thresholding(gray)
images = {'gray': gray,
          'thresh': thresh,
          }

fig = plt.figure(figsize=(13, 13))
ax = []

rows = 1
columns = 2
keys = list(images.keys())
for i in range(rows * columns):
    ax.append(fig.add_subplot(rows, columns, i + 1))
    ax[-1].set_title(' - ' + keys[i])
    plt.imshow(images[keys[i]], cmap='gray')
custom_config = r'--oem 3 --psm 6'
print('-----------------------------------------')
print('TESSERACT OUTPUT --> ORIGINAL IMAGE')
print('-----------------------------------------')
print(pytesseract.image_to_string(image, config=custom_config))
print('\n-----------------------------------------')
print('TESSERACT OUTPUT --> THRESHOLDED IMAGE')
print('-----------------------------------------')
print(pytesseract.image_to_string(image, config=custom_config))