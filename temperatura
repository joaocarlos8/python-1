def titulo(texto):
    print("\n" + "="*50)
    print(texto)
    print("="*50)
    
titulo("Exercício 2: Conversão de Temperatura")

while True:
    try: 
        tempC = float(input("Digite a temperatura em Celsius (ºC): "))
        tempF = (tempC * 9/5) + 32
        
        print(f"\n--- Resultado ---")
        print(f"Temperatura em Celsius: {tempC:.2f} ºC")
        print("-" * 30)
        
        print(f"A temperatura convertida é de **{tempF:.2f} ºF**")
        
        continuar = input("\nQuer converter outra temperatura? (S para continuar): ").upper()
        if continuar != "S":
            print("Programa de conversão encerrado.")
            break
    except ValueError:  
        print("\nErro: Por favor, digite apenas um valor numérico válido para a temperatura.")  