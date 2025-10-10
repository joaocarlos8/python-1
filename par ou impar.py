def titulo(texto):
    print("\n" + "="*50)
    print(texto)
    print("="*50)

titulo ("Exercicio 5: par ou impar")

while True:
    try:
       num = int(input("Digite um número inteiro: "))
       e_par = (num % 2) == 0
     
       print(f"\n--- Resultado ---")
       print(f"Número digitado: {num}")
       print(f"É par? {e_par}")
       
       continuar = input("Quer ver outro numero: ").upper()
       if continuar != "S":
           break
    except ValueError:
        print("\nErro: Por favor, digite apenas um número inteiro válido.")

  