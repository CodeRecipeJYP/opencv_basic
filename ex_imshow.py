# -*- coding: utf-8 -*-
import cv2
from cv2 import *
from toolbox import *

cv2.destroyAllWindows()
filename = 'Korean_License_Plate_for_Rent_Passenger_car_-_Heo.jpg'
#filename = '기차나.png'
#
#filename = '라이센스1.png'

img = cv2.imread(filename,cv2.IMREAD_COLOR)
#imshow_(img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imshow_(img)

#gray = cv2.GaussianBlur(gray, (3, 3), 0)
#imshow_(gray)

#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#imshow_(thresh)

#edged = cv2.Canny(img, 10, 10000)
#imshow_(edged)
#edged = cv2.Canny(img, 50, 100)
#imshow_(edged)
edged = cv2.Canny(img, 50, 200)
#crop = img.crop(100, 200, 300, 300).load()




i=-20
new_image = img[22:167][54+i:83+i]
#imshow_newtype(new_image)
cv2.imwrite('crop.png',new_image)
#imshow_(edged)
#edged = cv2.Canny(img, 100, 200)
#imshow_(edged)
#edged = cv2.Canny(img, 300, 400)
## imshow_(edged)
#edged = adjustSobel(img)

ret, thresh = cv2.threshold(edged,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
imshow_(thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
imshow_(closed)


img = closed







img2, contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#img2 = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#imshow_(img2)
height, width, channels = img.shape
img_size = height*width


#cv2.drawContours(img,contours, 3, (0,255,0),3)
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    x, y, w, h = cv2.boundingRect(c)
    aspectratio = float(w) / h

    area = cv2.contourArea(c)
    rect_area = w*h
    extent = float(area)/rect_area

    flag = True
    if area < img_size * 0.1:
        flag = False
    if float(area) > img_size * 0.7:
        flag = False
    #cv2.drawContours(img, [approx], -1, (0, 255, 255), 3)
    if (aspectratio) > 8:
        flag = False
    if (aspectratio) < 1.6:
        flag = False

    if extent <0.5:
        flag = False

    if len(approx) != 4:
        flag = False
# 8 > (aspectratio) > 1.6:


    if flag:
        cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
        print('area')
        print(area)
        print('rectarea')
        print(rect_area)
        print('ratio')
        print(float(area)/rect_area)
        print('aspectratio')
        print(aspectratio)

        imshow_(img)
        pass
    else:
        cv2.drawContours(img, [approx], -1, (0, 255, 255), 3)
        #imshow_(img)

#


    #else:
    #    pass


#cv2.namedWindow('LICENSEPLATE', cv2.WINDOW_NORMAL)
cv2.imshow('LICENSEPLATE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

