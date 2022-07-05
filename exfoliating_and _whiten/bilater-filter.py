import cv2
import matplotlib.pyplot as plt
img = cv2.imread('mopi_ep.jpg') 
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121) 
# plt.axis('off')
plt.xlabel('img')
plt.imshow(img[..., ::-1])
plt.subplot(122)
plt.xlabel('bilater')
plt.imshow(blur[..., ::-1])

plt.savefig('bilater_fliter.jpg')
plt.show()