# -*- coding:utf-8 -*-
# 2021年12月20日
import cv2
#图像按顺序命名为1.jpg、2.jpg等
num = 3;#图片总数量
im = cv2.imread("1.jpg")
hight,width = im.shape[0:2]
widths = width*(num+1)
images = cv2.resize(im,(int(widths),int(hight)))
cv2.imwrite("result.jpg",images)
widths = 0
for i in range(num):
    im_x = cv2.imread("%s.jpg"%(i+1))
    hight_x, width_x = im.shape[0:2]
    bl = width_x/hight_x#宽高比
    width_x = bl * hight
    im_x = cv2.resize(im_x,(int(width_x),int(hight_x)))
    images[0:int(hight),int(widths):int(width_x+widths)]=im_x
    widths = widths + width_x#总宽度

result = images[0:int(hight),0:int(widths)]
hight,width = result.shape[0:2]
print("拼接后图像的高",hight,"宽",width)
cv2.imwrite("result.jpg",result)