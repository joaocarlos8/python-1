import os
import time

def jogo_animais():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==== JOGO DOS ANIMAIS ====\n")
        print("1 - Adivinhar o animal")
        print("2 - Instruções")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adivinhar_animal()
        elif opcao == "2":
            mostrar_instrucoes()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida, tente novamente.")
            time.sleep(1.5)


def mostrar_instrucoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==== INSTRUÇÕES ====\n")
    print("Pense em um animal e responda as perguntas com 's' (sim) ou 'n' (não).")
    print("No final, o programa tentará adivinhar qual animal você pensou.")
    input("\nPressione ENTER para voltar...")


def adivinhar_animal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Pense em um animal e responda as perguntas abaixo.\n")
    time.sleep(1)

    vive_na_agua = input("O animal vive na água? (s/n): ").lower()

    if vive_na_agua == 's':
        eh_peixe = input("É um peixe? (s/n): ").lower()
        if eh_peixe == 's':
            print("\nAcertei! 🐟")
        else:
            print("\nEntão deve ser um golfinho! 🐬")
    else:
        voa = input("O animal voa? (s/n): ").lower()
        if voa == 's':
            ave_rapina = input("É uma ave de rapina? (s/n): ").lower()
            if ave_rapina == 's':
                print("\nAcertei! 🦅")
            else:
                print("\nEntão deve ser um papagaio! 🦜")
        else:
            domestico = input("É um animal doméstico? (s/n): ").lower()
            if domestico == 's':
                late = input("Ele late? (s/n): ").lower()
                if late == 's':
                    print("\nAcertei! 🐶")
                else:
                    print("\nEntão é um gato! 🐱")
            else:
                selvagem = input("É um animal selvagem grande? (s/n): ").lower()
                if selvagem == 's':
                    print("\nDeve ser um leão! 🦁")
                else:
                    print("\nTalvez seja um coelho! 🐰")

    input("\nPressione ENTER para voltar ao menu...")


# Execução direta do programa
if __name__ == "__main__":
    jogo_animais()