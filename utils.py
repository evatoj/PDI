from PIL import Image
from os import path

def carregar_imagem(arquivo: str) -> Image.Image:
  arquivo_dir = path.join('input', arquivo)
  return Image.open(arquivo_dir)

# salva a imagem na pasta /output no formato .bmp
# para não haver interferências após a aplicação dos filtros
def salvar_imagem(nome_arquivo: str, imagem: Image.Image):
  saida = path.join('output', nome_arquivo)
  imagem.save(f"{saida}.bmp")