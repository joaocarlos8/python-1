import os
import time

def eleicoes_grantiete():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗳️ ELEIÇÕES GRANTIETÊ 2025 - URNA ELETRÔNICA 🗳️\n")
        print("1 - Iniciar votação")
        print("0 - Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            iniciar_votacao()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida, tente novamente!")
            time.sleep(1.5)


def iniciar_votacao():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Candidatos disponíveis para votação
    candidatos = {
        13: ("Márcio", "Partido da Tecnologia (PT)"),
        35: ("Capella", "Partido dos Matemáticos (PM)"),
        51: ("Galto", "Partido da Coordenação (PC)"),
        60: ("José Mangili", "Partido das Arquiteturas de Computador (PAC)")
    }

    # Contadores de votos
    votos = {13: 0, 35: 0, 51: 0, 60: 0}
    votos_brancos = 0
    votos_nulos = 0
    alunos_votaram = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗳️ ELEIÇÕES GRANTIETÊ 2025 - URNA ELETRÔNICA 🗳️\n")

        num_aluno = input("Digite o número do aluno (0 para encerrar a votação): ")

        # Validação do número digitado
        if not num_aluno.isdigit():
            print("\n⚠️ Por favor, digite apenas números.")
            time.sleep(1.5)
            continue

        num_aluno = int(num_aluno)

        # Encerrar votação
        if num_aluno == 0:
            break

        # Impedir voto duplicado
        if num_aluno in alunos_votaram:
            print("\n⚠️ Este aluno já votou! Cada aluno só pode votar uma vez.")
            time.sleep(1.5)
            continue

        # Coleta do voto
        try:
            voto = int(input("Digite o número do seu candidato: "))
        except ValueError:
            print("\n⚠️ Valor inválido. Digite um número de candidato.")
            time.sleep(1.5)
            continue

        # Verifica tipo de voto
        if voto in candidatos:
            nome, partido = candidatos[voto]
            confirmacao = input(f"Confirma o voto em {nome} ({partido})? (sim/não): ").strip().lower()
            if confirmacao == "sim":
                votos[voto] += 1
                alunos_votaram.append(num_aluno)
                print("\n✅ Voto confirmado com sucesso!")
            else:
                print("\n⚠️ Voto cancelado, tente novamente.")
                time.sleep(1.5)
                continue

        elif voto == 0:
            confirmacao = input("Confirma voto em BRANCO? (sim/não): ").strip().lower()
            if confirmacao == "sim":
                votos_brancos += 1
                alunos_votaram.append(num_aluno)
                print("\n✅ Voto em branco registrado.")
            else:
                print("\n⚠️ Voto cancelado.")
                time.sleep(1.5)
                continue

        else:
            confirmacao = input("Confirma voto NULO? (sim/não): ").strip().lower()
            if confirmacao == "sim":
                votos_nulos += 1
                alunos_votaram.append(num_aluno)
                print("\n✅ Voto nulo registrado.")
            else:
                print("\n⚠️ Voto cancelado.")
                time.sleep(1.5)
                continue

        time.sleep(1.5)

    # Exibição do resultado final
    os.system('cls' if os.name == 'nt' else 'clear')
    total_votos = sum(votos.values()) + votos_brancos + votos_nulos
    votos_validos = sum(votos.values()) + votos_brancos

    print("📊 RESULTADO DAS ELEIÇÕES GRANTIETÊ 2025 📊\n")
    print(f"Total de votos registrados: {total_votos}\n")
    print("Votos por candidato:\n")

    for numero, (nome, partido) in candidatos.items():
        qtd = votos[numero]
        percentual = (qtd / votos_validos * 100) if votos_validos > 0 else 0
        print(f"{nome} ({partido}): {qtd} voto(s) - {percentual:.1f}%")

    print(f"\nVotos em branco: {votos_brancos}")
    print(f"Votos nulos: {votos_nulos}")

    # Determinar vencedor
    if sum(votos.values()) > 0:
        vencedor = max(votos, key=votos.get)
        nome_vencedor, _ = candidatos[vencedor]
        print(f"\n🏆 Candidato mais votado: {nome_vencedor} com {votos[vencedor]} voto(s)!")
    else:
        print("\nNenhum voto válido foi computado.")

    input("\nPressione ENTER para retornar ao menu...")


# Execução direta do programa
if __name__ == "__main__":
    eleicoes_grantiete()