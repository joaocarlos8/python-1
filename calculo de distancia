def titulo(texto):
    print("\n" + "="*50)
    print(texto)
    print("="*50)

titulo ("Exercicio 4: Cálculo de Distancia")
while True:
    try:
        velocidade = float(input("Informe a velocidade (em km/h): "))
        tempo = float(input("Informe o tempo percorrido (em horas): "))
        distancia = velocidade * tempo
        
        print(f"\n--- Resultado ---")
        print(f"Velocidade usada: {velocidade:.2f} km/h")
        print(f"Tempo de percurso: {tempo:.2f} horas")
        print("-" * 30)
        print(f"A **Distância percorrida** é de **{distancia:.2f} km**")
        
        continuar = input("\nQuer calcular outra distância? (S para continuar): ").upper()
        if continuar != "S":
            print("Programa de cálculo de distância encerrado.")
            break
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos para a velocidade e o tempo.")
        
        