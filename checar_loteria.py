import requests
import json
import os
#import optparse

minhas_apostas = [
                    ['02','07','11','16','25','51'],
                    ['06','17','22','26','43','59'],
                    ['03','13','17','28','38','49'],
                    ['19','27','35','45','48','60']
                ]

def obter_numeros(myLoteria,myToken,myConcurso):
    response = requests.get("https://apiloterias.com.br/app/resultado?loteria={}&token={}&concurso={}".format(myLoteria,myToken,myConcurso))
    return response

def is_winner(resultado):
    for nums in minhas_apostas:
        if nums == resultado:
            return True
        else:
            return False

def qtos_acertos(resultado):
    print('Jogos com numeros sorteados :')
    for jogos in minhas_apostas:
        for j in jogos:
            if j in resultado:
                print(' '.join(jogos))
                break



os.system("clear")
conc = input("QUAL O CONCURSO VC DESEJA CONFERIR : ")
if conc != '':
    print('[+] Conferindo resultado da MEGA-SENA.\n')
    resultado_megasena =  json.loads(obter_numeros('megasena','3NP3NC2xaGiIXpY',conc).text)

    ganhou = is_winner(resultado_megasena['dezenas'])

    if ganhou:
        print("*" * 30)
        print('VOCE GANHOU NA MEGA-SENA')
        print('Numeros sorteados : ',end=" ")
        for n in resultado_megasena['dezenas']:
            print(''.join(n),end=" ")
        print("\n")
        print('*' * 30)
    else:
        print ('voce nao ganhou na mega sena.Tente novamente!')
        print('Numeros sorteados : ',end=" ")
        for n in resultado_megasena['dezenas']:
            print(''.join(n),end=" ")
        print("\n")
        qtos_acertos(resultado_megasena['dezenas'])

else:
    print('[-] Entre com o numero do concurso como argumento')

input()

#
# parser = optparse.OptionParser()
# parser.add_option("-c","--concurso",dest="concurso",help="Numero do concurso a ser checado")
#
# (options,arguments) = parser.parse_args()
# conc = options.concurso
# print(conc)

# a = ['02','07','11','16','25','51']
# b = ['02','11','16','20','30','51']
# c = list(set(a).intersection(b))
# print(c)