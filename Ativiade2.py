import cv2
import numpy as np


def convolve2d(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2
    output = np.zeros_like(image)

    for i in range(pad_h, h - pad_h):
        for j in range(pad_w, w - pad_w):
            region = image[i - pad_h:i + pad_h + 1, j - pad_w:j + pad_w + 1]
            output[i, j] = np.sum(region * kernel)
    return np.clip(output, 0, 255)


img = cv2.imread("fla.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Imagem não encontrada. Verifique o nome e a pasta.")


identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
blur = np.ones((3,3)) / 9
sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])


out_identity_manual = convolve2d(img, identity)
out_blur_manual = convolve2d(img, blur)
out_sharpen_manual = convolve2d(img, sharpen)


out_identity_cv = cv2.filter2D(img, -1, identity)
out_blur_cv = cv2.filter2D(img, -1, blur)
out_sharpen_cv = cv2.filter2D(img, -1, sharpen)


cv2.imshow("Original", img)
cv2.imshow("Manual - Identity", out_identity_manual)
cv2.imshow("OpenCV - Identity", out_identity_cv)
cv2.imshow("Manual - Blur", out_blur_manual)
cv2.imshow("OpenCV - Blur", out_blur_cv)
cv2.imshow("Manual - Sharpen", out_sharpen_manual)
cv2.imshow("OpenCV - Sharpen", out_sharpen_cv)

cv2.waitKey(0)
cv2.destroyAllWindows()
