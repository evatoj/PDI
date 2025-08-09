# PDI

## Estrutura do projeto

- Imagens de entrada na pasta `/input`
- Imagens de saída na pasta `/output`

> [!IMPORTANT]
> A função `salvar_imagem` no arquivo de utilidades `filters\util.py` salva quaisquer imagem no formato `.bmp` para evitar interferências de outros formatos após a aplicação dos filtros. Por exemplo, imagens no formato `.jpg` ou `.jpeg` aplicam filtro de compressão ao serem salvos com a biblioteca `PIL` alterando o resultado dos filtros criados.

## Referências de Bibliotecas usadas

1. [PIL - Conceitos - `mode`](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes)
