def ComparacaoImc(imc):
    print (' IMC\t\tClassificação\n\n [18.5]\t\t[Baixo Peso]\n [25 a  29.9]\t[Excesso de Peso]\n [30 a 34.9]\t[Obesidade Classe 1]\n [35 a 39.9]\t[Obesidade Classe 2]\n [≥40]\t\t[Obesidade Classe 3]')

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
    
    