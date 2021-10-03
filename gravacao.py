from auxiliar import *
from musica import *
from cantor import *

def existe_gravacao(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

####################################################

def ins_gravacao(dicM, dicC, dicG):
    
    # Insere dados de gravação através da confirmação de existência da música e do cantor #
    print('♫ ♪ ♬ ♩ '*5)
    print('Por favor, informe os seguintes dados: ')
    titulo = input('➢ Título da música: ').strip()
    
    if existe_musica(dicM, titulo):

        nome_ar = input('➢ Nome artístico do cantor: ')
        
        if existe_cantor(dicC, nome_ar):
            data = input('➢ Data --> dd/mm/aaaa: ').strip()
            
            # Validação de uma data na estrutura da mesma e seu tipo primitivo #
            dat = dt.split('/')
            if len(dat) == 3:
                for cont in range(len(dat)):
                    if not dat[cont].isnumeric():
                        data = input('Data inválida! Digite outra data: ').strip()
            else:
                data = input('Data inválida! Digite outra data: ').strip()

            chave = (titulo, nome_ar, data)
            
            if existe_gravacao(dicG, chave):

                print('Esta gravação já existe!')
                pausa()

            else:
                alb = input('➢ Álbum: ')
                faixa = input('➢ Faixa: ')
                tempo = input('➢ Duração: ')
                
                # Validação de uma duração na estrutura da mesma e seu tipo primitivo #
                tp = tempo.split(':')
                for cont in range(len(tp)):
                    if not tp[cont].isnumeric():
                        tempo = input('Duração inválida! Digite outra duração: ').strip()

                estilo = input('➢ Estilo: ')

                # Criação de lista que recebe mais de uma informação #
                ins_mus = []
                instrumento = input('➢ Instrumento musical: ').strip()
                while instrumento != '' :
                    ins_mus.append(instrumento)
                    instrumento = input('➤ Digite mais um instrumento musical: ').strip()
                if len(compositor) == 0 :
                    ins_mus.append('Esta música não tem instrumentos musicais')
                valor = (alb, faixa, tempo, estilo, ins_mus)

                dicG[chave] = valor
                print('♫ ♪ ♬ ♩ '*5)
                print('')
                print('Dados inseridos com sucesso!')
                pausa()

        else:
            print('Este cantor não existe!')
            pausa()

    else:
        print('Este título não existe!')
        pausa()

####################################################################

def mos_gravacao(dicM, dicC, dicG, titulo, nome_ar, data):

    # Mostra os dados de uma gravação em específico #
    chave = (titulo, nome_ar, data)
    
    if existe_gravacao(dicG,chave):
        
        dados = dicG[chave]

        print('♪ Dados da gravação:')
        print("-----------------\n")

        print('♫ Música:')
        print('-------')
        mos_musica(dicM, titulo)
        print()

        print('♫ Cantor:')
        print('-------')
        mos_dados(dicC, nome_ar)
        print()

        print(f'Álbum: {dados[0]}')
        print(f'Faixa: {dados[1]}')
        print(f'Tempo: {dados[2]}')
        print(f'Estilo:{dados[3]}')
        print(f'Instrumentos musicais:{dados[4]}')
        
    else:
        print("A gravação informada não existe")

######################################################################

def alt_gravacao(dicM, dicC, dicG, titulo, nome_ar, data):

    # Alterar dados da respectiva gravação #
    chave = (titulo, nome_ar, data)
    
    if existe_gravacao(dicG, chave):
        mos_gravacao(dicM, dicC, dicG, titulo, nome_ar, data)
        confirma = input("Tem certeza que deseja alterá-la? (S/N): ").upper().strip()
        
        if confirma == 'S':
            alb = input('➢ Álbum: ').strip()
            faixa = input('➢ Faixa: ').strip()

            # Validação de uma duração na estrutura da mesma e seu tipo primitivo #
            tempo = input('➢ Duração --> hh:mm:ss: :').strip()
            tp = tempo.split(':')
            for cont in range(len(tp)):
                if not tp[cont].isnumeric():
                    tempo = input('Duração inválida! Digite outra duração: ').strip()
            estilo = input('➢ Estilo: ').strip()

            # Criação de lista que recebe mais de uma informação #
            ins_mus = []
            instrumento = input('➢ Instrumento musical: ').strip()
            while instrumento != '' :
                ins_mus.append(instrumento)
                instrumento = input('➤ Digite mais um instrumento musical: ').strip()
                
            valor = (alb, faixa, tempo, estilo, ins_mus)
            dicG[ chave ] = valor
            print('♫ ♪ ♬ ♩ '*5)
            print('')
            print("Dados inseridos com sucesso!")
            pausa()
                        
        else:
            print("Alteração cancelada!")
            pausa()

    else:
        print("Esta gravação não está cadastrada!")
        pausa()

#########################################################################

def rem_gravacao(dicM, dicC, dicG, titulo, nome_ar, data):

    # Remover determinada gravação #
    chave = (titulo, nome_ar, data)    
    
    if existe_gravacao(dicG,chave):
        mos_gravacao(dicM, dicC, dicG, titulo, nome_ar, data)
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper().strip()
        
        if confirma == 'S':
            del dicG[chave]
            print("Dados apagados com sucesso!")
            pausa()
            
        else:
            print("Exclusão cancelada!")
            pausa()

    else:
        print("Esta gravação não está cadastrada!")
        pausa()

#########################################################################

def toda_gravacao(dicM, dicC, dicG):

    # Mostra todas as gravações e seus dados #
    print("✔ Relatório: Todas as gravações")
    print("----------------------------\n")

    for chave in dicG:
        titulo = chave[0]
        nome_ar = chave[1]
        data = chave[2]
        
        mos_gravacao(dicM, dicC, dicG, titulo, nome_ar, data)

        print("----------------------------\n")
    print("")
    pausa()

############################################################################

def gra_gravacao(dic):

    # Grava os dados da gravação no arquivo #
    arq = open("gravacao3.txt", "w")
    
    for chave in dic:
        titulo = chave[0]
        nome_ar = chave[1]
        data = chave[2]
        
        tupla = dic[chave]
        
        alb = tupla[0]
        faixa = tupla[1]
        tempo = tupla[2]
        estilo = tupla[3]
        instrumento = '#'.join(tupla[4])

        frase = titulo + ";" + nome_ar + ";" + data + ";" + alb + ';' + faixa + ';' + tempo + ';' + estilo + ';' + instrumento + "\n"
        arq.write(frase)
    arq.close()

###########################################################################
    
def rec_gravacao(dic):

    if existe_arquivo("gravacao3.txt"):
        arq = open("gravacao3.txt", "r")

        for frase in arq:

            frase = frase[:len(frase)-1]
            lista = frase.split(";")
            
            titulo = lista[0]
            nome_ar = lista[1]
            data = lista[2]
            alb = lista[3]
            faixa = lista[4]
            tempo = lista[5]
            estilo = lista[6]
            instrumento = lista[7]

            ins_mus = instrumento.split("#")

            chave = (titulo, nome_ar, data)

            dic[chave] = (alb, faixa, tempo, estilo, ins_mus)
            
############################################################################

def menu_gravacao(dicM, dicC, dicG):
    
    opc = 0
    while ( opc != 6 ):
        print("➀ Inserir Gravação")
        print("➁ Alterar Gravação")
        print("➂ Remover Gravação")
        print("➃ Mostrar uma Gravação")
        print("➄ Mostrar todas as Gravações")
        print("➅ Sair do menu de Gravações")

        opc = int( input("❐ Opção escolhida: ") )

        if opc == 1:
            ins_gravacao(dicM, dicC, dicG)
            
        elif opc == 2:
            titulo = input('Digite o titulo: ')
            nome_ar = input('Digite o nome artístico: ')
            data = input('Digite a data: ')
            alt_gravacao(dicM, dicC, dicG, titulo, nome_ar, data)
            
        elif opc == 3:
            titulo = input('Digite o titulo: ')
            nome_ar = input('Digite o nome artístico: ')
            data = input('Digite a data: ')
            rem_gravacao(dicM, dicC, dicG, titulo, nome_ar, data)
            
        elif opc == 4:
            titulo = input('Digite o titulo: ')
            nome_ar = input('Digite o nome artístico: ')
            data = input('Digite a data: ')
            mos_gravacao(dicM, dicC, dicG, titulo, nome_ar,data)
            pausa()
            
        elif opc == 5:
            toda_gravacao(dicM, dicC, dicG)
            
        elif opc == 6:
            gra_gravacao(dicG)

##################################################################
