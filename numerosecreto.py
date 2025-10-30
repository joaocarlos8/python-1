import os
import time
import random

def mestre_dos_numeros():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("DESAFIO DO NÚMERO SECRETO\n")
        print("1 - Iniciar jogo")
        print("0 - Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            jogar_numero_secreto()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida, tente novamente.")
            time.sleep(1.5)


def jogar_numero_secreto():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("DESAFIO DO NÚMERO SECRETO\n")
        print("Adivinhe o número secreto entre 1 e 100!")
        print("Você tem 8 tentativas.\n")

        numero_secreto = random.randint(1, 100)
        tentativas = 8
        acertou = False

        for tentativa in range(1, tentativas + 1):
            while True:
                try:
                    palpite = int(input(f"Tentativa {tentativa}/{tentativas} → Seu palpite: "))
                    if 1 <= palpite <= 100:
                        break
                    else:
                        print("O número deve estar entre 1 e 100!")
                except ValueError:
                    print("Digite apenas números inteiros!")

            if palpite == numero_secreto:
                print("\nParabéns! Você acertou o número secreto!")
                acertou = True
                break
            elif palpite < numero_secreto:
                print("O número secreto é MAIOR.\n")
            else:
                print("O número secreto é MENOR.\n")

            time.sleep(1)

        if not acertou:
            print(f"\nSuas tentativas acabaram! O número era {numero_secreto}.")

        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            break

    print("\nVoltando ao menu principal...")
    time.sleep(1.5)


if __name__ == "__main__":
    mestre_dos_numeros()
