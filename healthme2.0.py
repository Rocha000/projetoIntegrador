
def CalculoIMC(peso,altura):
    imc = peso/(altura*altura)
    return imc
def ComparacaoImc(imc):
    print (' IMC\tClassificação\n\n [18.5]\t\t\t[Baixo Peso]\n [25 a  29.9]\t[Excesso de Peso]\n [30 a 34.9]\t[Obesidade Classe 1]\n [35 a 39.9]\t[Obesidade Classe 2]\n [>=40]\t\t\t[Obesidade Classe 3]\n\n')

    if imc<18.5:
        print('Baixo peso')
    elif  18.5 <= imc <= 24.9:
        print('Peso normal')
    elif  25 <= imc <= 29.9:
        print ('excesso de peso')
    elif 30 <= imc <= 34.9:
        print ('obesidade classe 1')
    elif 35 <= imc <= 39.9:
        print ('Obesidade classe 2')
    else:
        print ('Obesidade classe 3')
def CalculoCalorias(peso,altura,idade):
    taxaAtividade = " "
    while taxaAtividade not in "SLMAE":
        taxaAtividade = str(input("\nConsiderndo as seguintes informações: \n"
                                "[S] Sedentário (faz pouco ou nenhum exercício)\n"
                                "[L] Leventente ativo (faz exercícios leves de 1 a 3 vezes por semana)\n"
                                "[M] Moderadamente ativo (faz exercícios moderados de 3 a 5 vezes por semana)\n"
                                "[A] Altamente ativo (faz exercícios pesados de 5 a 6 vezes por semana)\n"
                                "[E] Extremamente ativo (faz exercícios pesados diariamente (até 2 vezes por dia)\n"
                                "\nVocê se considera ? ")).strip().upper()
        if taxaAtividade == "S":
            fatorAtividade = 1.2
        if taxaAtividade == "L":
            fatorAtividade = 1.375
        if taxaAtividade == "M":
            fatorAtividade = 1.55
        if taxaAtividade == "A":
            fatorAtividade = 1.725
        if taxaAtividade == "E":
            fatorAtividade = 1.9

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Informe seu sexo: [M/F] ? ")).strip().upper()
        if sexo == "M":

            totalCalorias = fatorAtividade * (66 + (5 * altura) + (13.7 * peso) - (6.8 * idade))

        if sexo == "F":

            totalCalorias = fatorAtividade * (655.1 + (1.8 * altura) + (9.6 * peso) - (4.7 * idade))

    print("\n\nSão necessárias {:.2f} calorias por dia".format(totalCalorias))
    return totalCalorias
def ComparacaoCalorias (caloriasNes):
    caloriasTotal = 0
    digitouCorretamente = False
    while not digitouCorretamente :
        try:
            refeicoes = int(input('\n\nInsira a quantas refeições você fez: '))
            if (refeicoes > 0):
                digitouCorretamente = True
            else:
                print('Valor inválido!') 
                digitouCorretamente = False 
        except ValueError:
            print('Valor inválido!')  
    digitouCorretamente = False
    while not digitouCorretamente:     
        i = 1    
        while i <= refeicoes:
            try:    
                calorias = int(input(f'Insira a quantidade de calorias, em kcal, que vc ingeriu na {i}ª refeição: '))
                if (calorias > 0):
                    digitouCorretamente = True
                    i+=1
                    caloriasTotal += calorias
                else:
                    print('Valor inválido!')    
            except ValueError:
                print('Valor inválido!')          
    print(f'\n\nO valor total de calorias consumidas foi {caloriasTotal:.2f} kcal')       
    ideal = caloriasNes-caloriasTotal
    if ideal<0:
        ideal=ideal*-1
        print(f"\nVocê ingeriu {ideal:.2f} kcal a mais que o nescesario")
    else:
        print(f"\nVocê deveria ingerir mais {ideal:.2f} kcal")



if __name__ == '__main__':
    digitouCorretamente = False
    while not digitouCorretamente:
        try:
            altura = float(input("\nInforme sua altura: "))

            if (altura < 2.5):
                altura = altura * 100
                digitouCorretamente = True

            if (altura <= 0):
                print("Por gentileza, informe sua altura novamente\n")
            else:
                digitouCorretamente = True
        except ValueError:
            print("Por gentileza, informe sua altura novamente\n")

    digitouCorretamente = False
    while not digitouCorretamente:
        try:
            peso = float(input("Informe seu peso: "))

            if (peso <= 0):
                print("Por gentileza, informe seu peso novamente\n")
            else:
                digitouCorretamente = True
        except ValueError:
            print("Por gentileza, informe seu peso novamente\n")

    digitouCorretamente = False
    while not digitouCorretamente:
        try:
            idade = int(input("Informe sua idade: "))
    
            if (idade <= 0):
                print("Por gentileza, informe sua idade novamente\n")
            else:
                digitouCorretamente = True
        except ValueError:
            print("Por gentileza, informe sua idade novamente\n")
    ComparacaoImc(CalculoIMC(peso,altura))
    ComparacaoCalorias(CalculoCalorias(peso,altura,idade))
