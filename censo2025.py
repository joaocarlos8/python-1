import os
import time

def censo_2025():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📊 CENSO 2025 - LEVANTAMENTO DEMOGRÁFICO 📊\n")
        print("1 - Iniciar coleta de dados")
        print("0 - Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            iniciar_censo()
        elif opcao == "0":
            break
        else:
            print("\n⚠️ Opção inválida, tente novamente.")
            time.sleep(1.5)


def iniciar_censo():
    os.system('cls' if os.name == 'nt' else 'clear')

    total_residencias = 0
    total_pessoas = 0
    soma_idades_geral = 0
    total_homens = 0
    total_mulheres = 0
    total_nao_inf = 0
    soma_salarios_geral = 0
    qtd_salarios_geral = 0

    while True:
        print("📊 CENSO 2025 - LEVANTAMENTO DEMOGRÁFICO 📊\n")
        try:
            pessoas = int(input("Quantas pessoas moram na residência? "))
        except ValueError:
            print("⚠️ Digite um número válido!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if pessoas == 0:
            break

        total_residencias += 1
        total_pessoas += pessoas

        soma_idades_casa = 0
        soma_sal_homens = 0
        qtd_homens_sal = 0
        soma_sal_mulheres = 0
        qtd_mulheres_sal = 0

        for i in range(1, pessoas + 1):
            print(f"\nPessoa {i}:")
            idade = int(input("Idade: "))
            sexo = input("Sexo (homem/mulher/não informado): ").strip().lower()
            salario = float(input("Salário (0 se não trabalha): "))

            soma_idades_casa += idade
            soma_idades_geral += idade

            if sexo == "homem":
                total_homens += 1
                if salario > 0:
                    soma_sal_homens += salario
                    qtd_homens_sal += 1
                    soma_salarios_geral += salario
                    qtd_salarios_geral += 1
            elif sexo == "mulher":
                total_mulheres += 1
                if salario > 0:
                    soma_sal_mulheres += salario
                    qtd_mulheres_sal += 1
                    soma_salarios_geral += salario
                    qtd_salarios_geral += 1
            else:
                total_nao_inf += 1
                if salario > 0:
                    soma_salarios_geral += salario
                    qtd_salarios_geral += 1

        media_idade_casa = soma_idades_casa / pessoas
        media_sal_homens = soma_sal_homens / qtd_homens_sal if qtd_homens_sal > 0 else 0
        media_sal_mulheres = soma_sal_mulheres / qtd_mulheres_sal if qtd_mulheres_sal > 0 else 0

        print(f"\n--- RESIDÊNCIA {total_residencias} ---")
        print(f"Total de pessoas: {pessoas}")
        print(f"Média de idades: {media_idade_casa:.1f}")
        print(f"Média salarial (homens): R$ {media_sal_homens:.2f}")
        print(f"Média salarial (mulheres): R$ {media_sal_mulheres:.2f}")

        input("\nPressione ENTER para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    if total_pessoas > 0:
        media_idade_geral = soma_idades_geral / total_pessoas
        media_sal_geral = soma_salarios_geral / qtd_salarios_geral if qtd_salarios_geral > 0 else 0

        print("\n📈 RELATÓRIO FINAL DO CENSO 2025 📈\n")
        print(f"Total de residências pesquisadas: {total_residencias}")
        print(f"Total de pessoas analisadas: {total_pessoas}")
        print(f"Média geral de idades: {media_idade_geral:.1f}")
        print(f"Homens: {total_homens} | Mulheres: {total_mulheres} | Não informado: {total_nao_inf}")
        print(f"Média salarial geral: R$ {media_sal_geral:.2f}")
    else:
        print("\nNenhum dado foi coletado.")

    input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    censo_2025()

