# Exercicio
"""
Você deve criar uma função que leia o arquivo shakespeare.txt, que contém todas as obras de William Shakespeare.
A função deve receber duas entradas: o caminho do arquivo e uma citação. A função deve retornar o título da obra
em que a citação se encontra.

Crie a função identificar_livro_por_citacao e teste-a com as seguintes citações:

1) "To be, or not to be, that is the question" -> deve retornar "THE TRAGEDY OF HAMLET, PRINCE OF DENMARK"
2) "What’s in a name? That which we call a rose\nBy any other name would smell as sweet;" -> deve retornar "THE TRAGEDY OF ROMEO AND JULIET"
"""


def identificar_livro_por_citacao(caminho_arquivo, citacao):
    pass


def main():
    # Caminho do arquivo shakespeare.txt
    caminho_arquivo = "dados/shakespeare.txt"

    # Testes das citações
    citacao1 = "To be, or not to be, that is the question"
    print(f'Resultado para a citação 1: "{citacao1}" -> {identificar_livro_por_citacao(caminho_arquivo, citacao1)}')

    citacao2 = "What’s in a name? That which we call a rose\nBy any other name would smell as sweet;"
    print(f'Resultado para a citação 2: "{citacao2}" -> {identificar_livro_por_citacao(caminho_arquivo, citacao2)}')


if __name__ == "__main__":
    main()
