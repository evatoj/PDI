from PIL import Image
import os


def converter_para_cinza(imagem_rgb):

    largura, altura = imagem_rgb.size  # Obtendo as dimensões da imagem.
    imagem_cinza = Image.new('L', (largura, altura))
    # O L é só para remover as crominâncias I e Q, preservando o Y.

    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem_rgb.getpixel((x, y))
            # Convertendo R, G e B para Y, de acordo com os pesos.
            valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            # Garantindo que o valor esteja no intervalo 0-255.
            valor_cinza = max(0, min(255, valor_cinza))
            imagem_cinza.putpixel((x, y), valor_cinza)

    return imagem_cinza


def gerar_nome_arquivo(pasta, base, extensao):
    # Função só pra organizar os arquivos de forma crescente na pasta destino.

    nome = f"{base}.{extensao}"
    contador = 1

    while os.path.exists(os.path.join(pasta, nome)):
        contador += 1
        nome = f"{base}{contador}.{extensao}"

    # Ela basicamente incrementa de um em um os nomes das imagens geradas, só pra ficar mais organizado mesmo xd.

    return nome


def main():
    pasta_entrada = 'input'
    pasta_saida = 'output'

    # Lembre-se de mudar o nome do arquivo de entrada para teste aqui.
    arquivo_entrada = 'dinheiro.jpg'
    caminho_entrada = os.path.join(pasta_entrada, arquivo_entrada)

    # Só pra garantir que a pasta output existe.
    os.makedirs(pasta_saida, exist_ok=True)

    # Tentando abrir a imagem, se der erro, já sabe...
    try:
        imagem_original = Image.open(caminho_entrada).convert('RGB')
    except FileNotFoundError:
        print(
            f"Arquivo '{arquivo_entrada}' não encontrado na pasta '{pasta_entrada}'.")
        return

    # Converte a imagem para escala de cinza.
    imagem_cinza = converter_para_cinza(imagem_original)

    # Gera um nome de saída único.
    nome_saida = gerar_nome_arquivo(pasta_saida, 'saida', 'jpg')

    caminho_saida = os.path.join(pasta_saida, nome_saida)

    # Salva e exibe o resultado, a imagem vai aparecer na tua tela, não se assuste kkkkk.
    imagem_cinza.save(caminho_saida)
    imagem_cinza.show()

    print(f"Imagem salva em: {caminho_saida}")


if __name__ == "__main__":
    main()
