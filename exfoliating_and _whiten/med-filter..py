import cv2
import matplotlib.pyplot as plt
img = cv2.imread('mopi_ep.jpg') #直接读为灰度图像
blur = cv2.blur(img,(7,7))#模板大小3*5

plt.subplot(121) 
# plt.axis('off')
plt.xlabel('img')
plt.imshow(img[..., ::-1])
plt.subplot(122)
plt.xlabel('blur')
# plt.axis('off')
plt.imshow(blur[..., ::-1])

plt.savefig('blur_fliter.jpg')
plt.show()

# cv2.imshow('blur', blur)
# cv2.imshow('img', img)
# cv2.waitKey(0)