import cv2
import numpy as np

img = cv2.imread("fla.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Exemplo: faixa para vermelho
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

isolated = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Isolado Vermelho", isolated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ajuste de contraste e brilho
alpha = 1.5  # contraste
beta = 30    # brilho
contrasted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Correção gamma
gamma = 1.8
invGamma = 1.0 / gamma
table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(256)]).astype("uint8")
gamma_corrected = cv2.LUT(img, table)

import matplotlib.pyplot as plt

def plot_histogram(image, title):
    color = ('b','g','r')
    for i,col in enumerate(color):
        hist = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=col)
    plt.title(title)
    plt.show()

plot_histogram(img, "Histograma Original")
plot_histogram(contrasted, "Histograma Contraste")
plot_histogram(gamma_corrected, "Histograma Gamma")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Global
global_eq = cv2.equalizeHist(gray)

# CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_eq = clahe.apply(gray)

cv2.imshow("Global Equalization", global_eq)
cv2.imshow("CLAHE Equalization", clahe_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("resultado_qualidade1.png", clahe_eq, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.imwrite("resultado_qualidade2.png", clahe_eq, [cv2.IMWRITE_PNG_COMPRESSION, 5])
cv2.imwrite("resultado_qualidade3.png", clahe_eq, [cv2.IMWRITE_PNG_COMPRESSION, 9])