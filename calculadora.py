def calculadora():
    while True:
        print("Calculadora Simples\n")
        print("1. SOMA")
        print("2. SUBTRAÇÃO")
        print("3. MULTIPLICAÇÃO")
        print("4. DIVISÃO")
        print("S. SAIR")
        operacao = input("\nSelecione uma opção ou 's' para sair:")

        if operacao == 's' or operacao == 'S':
            print("Obrigada por utilizar a Calculadora Simples!")
            break

        if operacao not in ['1','2','3','4']:
            print("Opção inválida! Tente Novamente")
            continue

        numero_um = float(input("Primeiro Número:"))
        numero_dois = float(input("Segundo Número:"))

        if operacao == '1':
            resultado = numero_um + numero_dois
            print("O resultado da operação soma é:", resultado)
        elif operacao == '2':
            resultado = numero_um - numero_dois
            print("O resultado da operação subtração é:",resultado)
        elif operacao == '3':
            resultado = numero_um * numero_dois
            print("O resultado da operação multiplicação é:",resultado)
        else:
            if numero_dois == '0':
                print("divisões por zero não são possíveis, tente novamente!")
                continue
            else:
                resultado = numero_um / numero_dois
                print("O resultado da operação divisão é:",resultado)
calculadora()