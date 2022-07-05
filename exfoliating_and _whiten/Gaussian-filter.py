import cv2
import matplotlib.pyplot as plt
img = cv2.imread('mopi_ep.jpg') #直接读为灰度图像
blur = cv2.GaussianBlur(img,(7,7),0)

plt.subplot(121) 
# plt.axis('off')
plt.xlabel('img')
plt.imshow(img[..., ::-1])
plt.subplot(122)
plt.xlabel('gauss')
# plt.axis('off')
plt.imshow(blur[..., ::-1])

plt.savefig('gauss_fliter.jpg')
plt.show()