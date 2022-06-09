#PROGRAMA CRIPTOGRAFIA/DESCRIPTOGRAFIA

#GUSTAVO BEZERRA
#JULIO LEITE
#LUCCA ROCHA
#MATHEUS TAVEIRA
#WEDER DE OLIVEIRA FILHO

#FUNÇÃO TRASFORMAR TEXTO EM MATRIZ
def transformarMatriz(txt):
    txt.strip()
    if len(txt) % 2 != 0:
        txt = txt + " "
    linha1 = []
    linha2 = []
    for i in range(len(txt)):
        if i % 2 == 0:
            linha1.append(dicionarioVariaveis[txt[i]])
        else:
            linha2.append(dicionarioVariaveis[txt[i]])
    matrizcripto = [linha1, linha2]
    return matrizcripto


#FUNÇÃO CRIPTOGRAFIA
def Criptografia(matriz):
    matriz = transformarMatriz(matriz)
    linha1 = []
    linha2 = []
    matrizchave = [[1, 1], [1, 2]]
    for j in range(len(matriz[0])):
        linha1.append(((matrizchave[0][0]*matriz[0][j])+(matrizchave[0][1]*matriz[1][j]))%qtdutilizavel)
        linha2.append(((matrizchave[1][0]*matriz[0][j])+(matrizchave[1][1]*matriz[1][j]))%qtdutilizavel)
    matrizcriptografada = [linha1, linha2]
    return matrizcriptografada


#FUNÇÃO DESCRIPTOGRAFIA
def Descriptografia(matriz):
    linha1 = []
    linha2 = []
    matrizchave = [[2, 101], [101, 1]]
    for j in range(len(matriz[0])):
        linha1.append(((matrizchave[0][0]*matriz[0][j])+(matrizchave[0][1]*matriz[1][j]))%qtdutilizavel)
        linha2.append(((matrizchave[1][0]*matriz[0][j])+(matrizchave[1][1]*matriz[1][j]))%qtdutilizavel)
    return [linha1, linha2]


#FUNÇÃO TRANSFORMAR MATRIZ EM TEXTO
def transformarTxt(txt):
    texto = ""
    for transformar in range(len(txt[0])):
        texto = texto + dicionarioNum[txt[0][transformar]]
        texto = texto + dicionarioNum[txt[1][transformar]]
    while texto[len(texto) - 1] == " ":
        texto = texto[:-1]
    return texto


#MAIN
if __name__ == '__main__':
    print('=' * 60 + '\n\tPROGRAMA CRIPTOGRAFIA/DESCRIPTOGRAFIA\t\n' + '='*60)
    utilizavel = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZãâáêéèõôóÃÂÁÊÉÈÕÔÓabcdefghijklmnopqrstuvwxyz,.@!#$%¨&*-_() +=;/?\|"
    qtdutilizavel = len(utilizavel)
    dicionarioVariaveis = {}
    dicionarioNum = {}
    for i in range(qtdutilizavel):
        dicionarioVariaveis[utilizavel[i]] = i
        dicionarioNum[i] = utilizavel[i]
    cripto = Criptografia(input("Digite algo: "))
    transtxtcripto = transformarTxt(cripto)
    descripto = Descriptografia(cripto)
    transtxtdescripto = transformarTxt(descripto)
    if transtxtdescripto[len(transtxtdescripto) - 1] == " ":
        transtxtdescripto = transtxtdescripto[:-1]
    print(cripto) 
    print(transtxtcripto) 
    print(descripto) 
    print(transtxtdescripto) 