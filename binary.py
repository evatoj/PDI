from PIL import Image

def binarizar(imagem: Image.Image, limiar=128) -> Image.Image:

  #verificar se o valor do liminar está entre 0 e 255

  if limiar > 255:
    raise ValueError(f"liminar {limiar} não pode ser maior que 255.")
  elif limiar < 0:
    raise ValueError(f"liminar {limiar} não pode ser negativo.")

  # cria uma nova imagem (imagem de saida) 
  # com a resolução da imagem original

  img_bin = Image.new(mode="L", size=imagem.size)

  # percorre a imagem original,
  # aplica o filtro pontual limiar na imagem de saida

  altura, largura = imagem.size

  for i in range(altura):
    for j in range(largura):
      pixel = imagem.getpixel((i,j))
      # escreve o pixel na imagem de saída dependendo do liminar
      if (pixel <= limiar):
        img_bin.putpixel((i,j), 0)
      else:
        img_bin.putpixel((i,j), 255)

  # retorna a imagem binarizada
  return img_bin