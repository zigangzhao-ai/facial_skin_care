import cv2
import math
import matplotlib.pyplot as plt

def main():
    img = cv2.imread("mopi_ep.jpg")
    height, width, n = img.shape
    img2 = img.copy()
    beta = 3
    alpha = 40

    for i in range(height):
        for j in range(width):
           img2[i, j][0] = alpha * math.log(img[i, j][0] * (beta - 1) + 1) / math.log(beta)
           img2[i, j][1] = alpha * math.log(img[i, j][1] * (beta - 1) + 1) / math.log(beta)
           img2[i, j][2] = alpha * math.log(img[i, j][2] * (beta - 1) + 1) / math.log(beta)
    # cv2.imwrite('res.jpg',img2)
    plt.subplot(121) 
    plt.xlabel('img')
    plt.imshow(img[..., ::-1])
    plt.subplot(122)
    plt.xlabel('whiten')
    plt.imshow(img2[..., ::-1])
    plt.savefig('meibai/beta_whiten.jpg')

if __name__ == '__main__':
    main()
