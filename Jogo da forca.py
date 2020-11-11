from os import system, name
palavra = ''
chances = 0
def ler_arquivo():
    global palavra
    global chances
    c = 0
    with open('arquivo.txt') as f:
        for line in f:
            c+=1
            if c == 1:
                palavra = line.strip()
            elif c == 2:
                chances = int(line)
        f.close()


def verifica_fim_jogo(tentativa_palavra) -> bool:
    global palavra
    global chances
    if tentativa_palavra == palavra:
        print("Você ganhou com apenas {}!" .format(chances))
        return True

    if chances == 0:
        print("Você perdeu!")
        return True

def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def jogar():
    global palavra
    global chances
    ler_arquivo()
    letras_usadas = []
    while True:
        tentativa_palavra = ""

        limpar_tela()

        print("Número de chances: %d - tentativas:" % chances)  # interpolação de string
        print(*letras_usadas)  # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")

        if verifica_fim_jogo(tentativa_palavra):
            break

        while True:
            chute = input("Digite uma letra:").lower()

            try:
                float(chute)
                print('Você digitou um número. Digite algo válido!')
                continue
            except:
                ...
            if chute in letras_usadas:
                print('Essa letra já foi usada.')
            else:
                break


        letras_usadas.append(chute)

        if not chute in palavra:
            chances -= 1


if __name__ == "__main__":
    jogar()
