from auxiliar import *

def existe_cantor(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False
    
#####################################################

def ins_dados(dic):

    # Inserir novo cantor #
    print('♫ ♪ ♬ ♩ '*5)
    print('Por favor, informe os seguintes dados: ')
    nome_ar = input('➢ Nome artístico: ').strip()
    
    if existe_cantor(dic,nome_ar):
        print('Cantor já cadastrado!')
        pausa()
        
    else:
        n = input('➢ Nome real: ').strip()
        dt_ns = input('➢ Data de nascimento --> dd/mm/aaaa: ').strip()

        # Validação de uma data na estrutura da mesma e seu tipo primitivo #
        dat = dt_ns.split('/')
        if len(dat) == 3:
            for cont in range(len(dat)):
                if not dat[cont].isnumeric():
                    dt_ns = input('Data inválida! Digite outra data: ').strip()
        else:
            dt_ns = input('Data inválida! Digite outra data: ').strip()

        # Criação de lista que recebe mais de uma informação #
        tels = []
        e_mail = []
        telefone = input('➢ Telefone: ').strip()
        while telefone != '' :
            tels.append(telefone)
            telefone = input('➤ Digite mais um telefone: ').strip()
        email = input('➢ E-mail: ').strip()
        while email != '':
            e_mail.append(email)
            email = input('➤ Digite mais um e-mail: ').strip()

        if len(tels) == 0 :
            tels.append('Este cantor não tem telefone')
        if len(e_mail) == 0:
            e_mail.append('Este cantor não tem e-mail')

        dic[nome_ar]=(n, dt_ns, e_mail, tels)
        print('♫ ♪ ♬ ♩ '*5)
        print('')

        print('Dados inseridos com sucesso!')
        pausa()

####################################################################

def mos_dados(dic,chave):

    # Mostra um respectivo cantor já gravado (ou não) e seus possíveis dados #
    if existe_cantor(dic,chave):
        dados = dic[chave]
        
        print(f'Nome Real: {dados[0]}')
        print(f'Data de Nascimento: {dados[1]}')
        email = ' - '.join(dados[2])
        print(f'E-mails: {email}')
        telefones = " - ".join(dados[3])
        print(f"Telefones: {telefones}")
        
    else:
        print('Cantor não cadastrado!')

######################################################################

def alt_dados(dic,chave):

    # Alterar dados de um cantor # 
    if existe_cantor(dic,chave):
        mos_dados(dic,chave)

        confirma = input('Certeza que deseja alterar? (S/N): ').upper().strip()
        if confirma == 'S':
            n = input('➢ Nome real: ')
            dt_ns = input('➢ Data de nascimento: ').strip()

            # Validação de uma data na estrutura da mesma e seu tipo primitivo #
            dat = dt_ns.split('/')
            if len(dat) == 3:
                for cont in range(len(dat)):
                    if not dat[cont].isnumeric():
                        dt_ns = input('Data inválida! Digite outra data: ').strip()
            else:
                dt_ns = input('Data inválida! Digite outra data: ').strip()

            # Criação de lista que recebe mais de uma informação #
            tels = []
            e_mail = []
            telefone = input('➢ Telefone: ').strip()
            while telefone != '':
                tels.append(telefone)
                telefone = input('➤ Digite mais um telefone: ').strip()
            email = input('➢ E-mail: ').strip()
            while email != '':
                e_mail.append(email)
                email = input('➤ Digite mais um e-mail: ').strip()

            if len(tels) == 0:
                tels.append('Este cantor não tem telefone!')
            if len(e_mail) == 0:
                e_mail.append('Este cantor não tem e-mail!')
                
            dic[chave]=(n, dt_ns, e_mail, tels)
            print('♫ ♪ ♬ ♩ '*5)
            print('')
            print('Dados alterados com sucesso!')
            pausa()
            
        else:
            print('Alteração cancelada!')
            pausa()

    else:
        print('Cantor não cadastrado!')
        pausa()

#########################################################################

def rem_dados(dic,chave):

    # Remoção de um cantor #
    if existe_cantor(dic,chave):    
        mos_dados(dic,chave)

        confirma = input('Tem certeza que deseja apagar? (S/N): ').upper().strip()
        if confirma == 'S':
            del dic[chave]
            print('Dados apagados com sucesso!')
            pausa()
        else:
            print('Exclusão cancelada!')
            pausa()
    else:
        print('Cantor não cadastrado!')
        pausa()

#########################################################################

def mos_cantor(dic):
    
    # Mostrar todos os cantores e seus dados gravados #
    print('✔ Relatório: \n')
    print('Nome Artístico ◈ Nome Real ◈ Data de Nascimento ◈ Email ◈ Tel: \n')

    for nome_ar in dic:
        lista = dic[nome_ar]
        email = '/'.join(lista[2])
        telefones = "/".join(lista[3])

        frase = nome_ar + ' ◈ ' + lista[0] + ' ◈ ' + lista[1] + ' ◈ ' + email + ' ◈ ' + telefones
        print(frase)

    print('')
    pausa()

############################################################################

def gra_dados(dic):

    # Gravação do cantor num arquivo #
    arq = open("gravacao2.txt", "w")
    
    for nome_ar in dic:
        lista = dic[nome_ar]

        email = '*'.join(lista[2])
        telefones = '*'.join(lista[3])

        frase = nome_ar + ';' + lista[0] + ';' + lista[1] + ';' + email + ';' + telefones + '\n'
        arq.write(frase)
    arq.close()

###########################################################################
    
def rec_dados(dic):
    if ( existe_arquivo("gravacao2.txt") ):
        arq = open("gravacao2.txt", "r")

        for lista in arq:
            lista = lista[:len(lista)-1]
            lista = lista.split(";")
            
            nome_ar = lista[0]
            n = lista[1]
            dt_ns = lista[2]
            email = lista [3]
            telefones = lista[4]

            lisemail = email.split("#")
            listel = telefones.split("#")
            
            dic[nome_ar] = (n, dt_ns, lisemail, listel)


############################################################################

def menu_dados(dic_cantor):
    opc = 0
    
    while ( opc != 6 ):
        print("➀ Inserir Cantor")
        print("➁ Alterar Cantor")
        print("➂ Remover Cantor")
        print("➃ Mostrar um Cantor")
        print("➄ Mostrar todos os Cantores")
        print("➅ Sair do menu de Cantor")
        print('')
        opc = int( input("❐ Opção escolhida: ") )
        print('')
        if opc == 1:
            ins_dados(dic_cantor)
            
        elif opc == 2:
            nome_ar = input('Nome artístico do cantor a ser alterado: ')
            alt_dados(dic_cantor, nome_ar)
            
        elif opc == 3:
            nome_ar = input('Nome artístico do cantor a ser removido: ')
            rem_dados(dic_cantor, nome_ar)
            
        elif opc == 4:
            nome_ar = input('Nome artístico do cantor a ser consultado: ')
            mos_dados(dic_cantor, nome_ar)
            pausa()
            
        elif opc == 5:
            mos_cantor(dic_cantor)
            
        elif opc == 6:
            gra_dados(dic_cantor)

##################################################################
