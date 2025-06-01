# Exercicio
"""
Escreva um programa em Python que leia o arquivo 'dados/alice.txt' e conte quantas vezes a palavra "Alice" aparece no texto.
Para isso, utilize as funções de abertura e leitura de arquivos. Em seguida, imprima o resultado na tela.
Certifique-se de que a contagem não depende de maiúsculas ou minúsculas (ou seja, considere 'Alice', 'alice' e 'ALICE' como a mesma palavra).

Dicas:
- Utilize o método .lower() para facilitar a contagem de forma case insensitive.
- Considere que a palavra "Alice" pode aparecer em diferentes contextos e pontuações.
"""


def contar_a_palavra_alice():
    pass


def main():
    quantidade = contar_a_palavra_alice()
    if quantidade:
        print(f"A palavra 'Alice' aparece {quantidade} vezes no texto.")
    else:
        print("Modifique o código para contar as palavras")
        


if __name__ == "__main__":
    main()
