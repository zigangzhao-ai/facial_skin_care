import cv2
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("mopi_ep.jpg")
height,width,n = img.shape
img2 = img.copy()
for i in range(height):
    for j in range(width):
        img2[i, j][0] = 255
        img2[i, j][1] = 255
        img2[i, j][2] = 255

# img = cv2.bilateralFilter(img, 9, 75, 75)
dst=cv2.addWeighted(img, 0.6, img2, 0.4, 0)
# cv2.imwrite('meibai/res.jpg', dst)
img3 = Image.fromarray(dst)
enh_con = ImageEnhance.Contrast(img3)
contrast = 1.2
image_contrasted = enh_con.enhance(contrast)
# image_contrasted.show()
enh_bri = ImageEnhance.Brightness(image_contrasted)
brightness = 1.1
image_brightened = enh_bri.enhance(brightness)
# image_brightened.show()

plt.subplot(121) 
plt.xlabel('img')
plt.imshow(img[..., ::-1])
plt.subplot(122)
plt.xlabel('whiten')
image_brightened = np.array(image_brightened)
plt.imshow(image_brightened[..., ::-1])
plt.savefig('meibai/whiten.jpg')
plt.show()


