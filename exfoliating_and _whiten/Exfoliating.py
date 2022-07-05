import cv2
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('mopi_ep.jpg')
blur = cv2.bilateralFilter(img, 9, 75, 75)

## 图像融合
alpha = 0.3
beta = 1 - alpha
gamma = 0
img_add = cv2.addWeighted(img, alpha, blur, beta, gamma)
# cv2.imwrite('img_add.jpg', img_add)
## 锐度增强
# img_add = Image.open('img_add.jpg')
img_add = Image.fromarray(img_add)
# img_add.show()
enh_sha = ImageEnhance.Sharpness(img_add)
sharpness = 1.5
image_sharped = enh_sha.enhance(sharpness)

# # 对比度增强
enh_con = ImageEnhance.Contrast(image_sharped)
contrast = 1.15
image_contrasted = enh_con.enhance(contrast)

# image_contrasted.show()
# cv2.waitKey(0)

plt.subplot(231) 
plt.xlabel('img')
plt.imshow(img[..., ::-1])
plt.subplot(232)
plt.xlabel('bilatera')
plt.imshow(blur[..., ::-1])
plt.subplot(233) 
plt.xlabel('img_add')
img_add = np.array(img_add)
plt.imshow(img_add[..., ::-1])
plt.subplot(234)
plt.xlabel('image_sharped')
image_sharped = np.array(image_sharped)
plt.imshow(image_sharped[..., ::-1])
plt.subplot(235)
plt.xlabel('image_contrasted')
image_contrasted = np.array(image_sharped)
plt.imshow(image_contrasted[..., ::-1])

plt.savefig('exfoliat_fliter2.jpg')
plt.show()
