from auxiliar import *

def existe_musica(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

####################################################

def ins_musica(dic):

    # Inserir nova música #
    print('♫ ♪ ♬ ♩ '*5)
    print('Por favor, informe os seguintes dados: ')
    titulo = input('➢ Título da música: ').strip()
    
    if existe_musica(dic,titulo):
        print('Música já cadastrada!')
        pausa()
        
    else:
        dt = input('➢ Data de registro --> dd/mm/aaaa: ').strip()

        # Validação de uma data na estrutura da mesma e seu tipo primitivo #
        dat = dt.split('/')
        if len(dat) == 3:
            for cont in range(len(dat)):
                if not dat[cont].isnumeric():
                    dt = input('Data inválida! Digite outra data: ').strip()
        else:
            dt = input('Data inválida! Digite outra data: ').strip()
        est = input('➢ Estilo musical: ').strip()
        temp = input('➢ Duração da música --> hh:mm:ss : ').strip()

        # Validação de uma duração na estrutura da mesma e seu tipo primitivo #
        tp = temp.split(':')
        for cont in range(len(tp)):
            if not tp[cont].isnumeric():
                temp = input('Duração inválida! Digite outra duração: ').strip()

        # Criação de lista que recebe mais de uma informação #
        cp = []
        compositor = input('➢ Compositor: ').strip()
        while compositor != '' :
            cp.append(compositor)
            compositor = input('➤ Digite mais um compositor: ').strip()
        if len(compositor) == 0 :
            cp.append('Esta música não tem compositores')
        dic[titulo]=(dt, est, temp, cp)
        print('♫ ♪ ♬ ♩ '*5)
        print('')

        print('Dados inseridos com sucesso!')
        pausa()

####################################################################
        
def mos_musica(dic,chave):
    
    # Mostra uma respectiva música já gravada (ou não) e seus possíveis dados #
    if existe_musica(dic,chave):
        dados = dic[chave]
        print(f"Data de registro: {dados[0]}")
        print(f"Estilo: {dados[1]}")
        print(f"Tempo de duração: {dados[2]}")
        print(f"Compositor(es): {dados[3]}")   
    else:
        print("Música não cadastrada!")

######################################################################

def alt_musica(dic,chave):

    # Alterar dados de uma música # 
    if existe_musica(dic,chave):   
        mos_musica(dic,chave)
        confirma = input('Certeza que deseja alterá-la? (S/N): ').upper().strip()
        
        if confirma == 'S':
            print('♫ ♪ ♬ ♩ '*5)
            dt = input('➢ Data de registro --> dd/mm/aaaa : ').strip()

            # Validação de uma data na estrutura da mesma e seu tipo primitivo #
            dat = dt.split('/')           
            for cont in range(len(dat)):
                if not dat[cont].isnumeric():
                    dt = input('Data inválida! Digite outra data: ').strip()
            est = input('➢ Estilo musical: ').strip()
            temp = input('➢ Duração da música --> hh:mm:ss : ').strip()

            # Validação de uma duração na estrutura da mesma e seu tipo primitivo #
            tp = temp.split(':')
            for cont in range(len(tp)):
                if not tp[cont].isnumeric():
                    temp = input('Duração inválida! Digite outra duração: ').strip()

            # Criação de lista que recebe mais de uma informação #
            cp = []
            compositor = input('➢ Compositor: ').strip()
            while compositor != '' :
                cp.append(compositor)
                compositor = input('➤ Digite mais um compositor: ').strip()
                
            if len(compositor) == 0 :
                cp.append('Esta música não tem compositores')
                
            dic[chave]=(dt, est, temp, cp)
            print('♫ ♪ ♬ ♩ '*5)
            print('')
            print('Dados inseridos com sucesso!')
            pausa()            
        else:
            print("Alteração cancelada!")
            pausa()
    else:
        print('Música não cadastrada!')
        pausa()

#########################################################################

def rem_musica(dic,chave):

    # Remoção de uma música #
    if existe_musica(dic,chave):    
        mos_musica(dic,chave)
        
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper().strip()
        if confirma == 'S':
            del dic[chave]
            print('Dados apagados com sucesso!')
            pausa()
        else:
            print('Exclusão cancelada!')
            pausa()
    else:
        print('Música não cadastrada!')
        pausa()

#########################################################################

def tod_musica(dic):

    # Mostrar todas as músicas e seus dados gravados #
    print('✔ Relatório:\n')
    print('Título ◈ Data de registro ◈ Estilo ◈ Tempo ◈ Compositores\n')

    for titulo in dic:
        lista = dic[titulo]
        compositor = '/'.join(lista[3])
        frase = titulo + ' ◈ ' + lista[0] + ' ◈ ' + lista[1] + ' ◈ ' + lista[2] + ' ◈ ' + compositor
        print(frase)
    print('')
    pausa()

############################################################################

def gra_musica(dic):

    # Gravação da música num arquivo #
    arq = open("gravacao1.txt", "w")
    
    for titulo in dic:
        lista = dic[titulo]
        compositor = '*'.join(lista[3])

        frase = titulo + ';' + lista[0] + ';' + lista[1] + ';' + lista[2] + ';' + compositor + '\n'
        arq.write(frase)
    arq.close()

###########################################################################
    
def rec_musica(dic):
    if existe_arquivo("gravacao1.txt") :
        arq = open("gravacao1.txt", "r")
        
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")

            titulo = lista[0]
            dt = lista[1]
            est = lista[2]
            temp = lista[3]
            compositor = lista[4]

            liscp = compositor.split("#")
            
            dic[titulo] = (dt, est, temp, liscp)


############################################################################

def menu_musica(dic_musica):
                               
    opc = 0
    
    while opc != 6:
        print("➀ Inserir Música")
        print("➁ Alterar Música")
        print("➂ Remover Música")
        print("➃ Mostrar uma Música")
        print("➄ Mostrar todas as Músicas")
        print("➅ Sair do menu de Músicas")
        print('')

        opc = int( input("❐ Opção escolhida: ") )
        print('')

        if opc == 1:
            ins_musica(dic_musica)
            
        elif opc == 2:
            titulo = input("Música a ser alterada: ")
            alt_musica(dic_musica, titulo)
            
        elif opc == 3:
            titulo =input("Música a ser removida: ")
            rem_musica(dic_musica, titulo)
            
        elif opc == 4:
            titulo = input("Música ser consultada: ")
            mos_musica(dic_musica, titulo)
            pausa()
            
        elif opc == 5:
            tod_musica(dic_musica)
            
        elif opc == 6:
            gra_musica(dic_musica)

##################################################################
