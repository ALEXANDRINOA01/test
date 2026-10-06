from PIL import Image


img = Image.open("fotoboborleta.png")   # substitua pelo nome real da sua imagem
img.show()


print("Formato:", img.format)       # JPEG, PNG etc.
print("Dimensões:", img.size)       # (largura, altura)
print("Modo:", img.mode)            # RGB, RGBA, L (escala de cinza)

# 3. Um pixel específico
pixel = img.getpixel((10, 10))
print("Pixel (10,10):", pixel)

# 4. Crop de uma região
crop = img.crop((50, 50, 200, 200))  # (esquerda, topo, direita, baixo)
crop.show()

# 5. Salvar e reabrir
crop.save("recorte.png")
nova_img = Image.open("../Atividades/recorte.png")
nova_img.show()

# 6. Comparar PNG e JPEG
img.save("teste.jpeg", "JPEG")
img.save("teste.png", "PNG")
print("Salvei versões em JPEG e PNG. Compare os tamanhos dos arquivos no sistema.")

# 7. Converter para escala de cinza
gray = img.convert("L")
gray.show()
print("Dimensões em cinza:", gray.size)
print("Modo em cinza:", gray.mode)
