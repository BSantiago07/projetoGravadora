from musica import *
from cantor import *
from gravacao import * 
from auxiliar import *

BDmusica = {}
BDcantor = {}
BDgravacao = {}

rec_musica(BDmusica)
rec_dados(BDcantor)
rec_gravacao(BDgravacao)

opc = 0
   
while opc != 5:
    
    print('➊ Submenu de Músicas')
    print('➋ Submenu de Cantores')
    print('➌ Submenu de Gravações')
    print('➍ Finalizar programa')
    print('')

    opc = int(input('❐ Opção escolhida: '))
    print('')
        
    if opc == 1:
        menu_musica(BDmusica)
        print("\n\n\n\n")
            
    elif opc == 2:
        menu_dados(BDcantor)
        print("\n\n\n\n")
            
    elif opc == 3:
        menu_gravacao(BDmusica, BDcantor, BDgravacao)
        print("\n\n\n\n")
        

print("\n\n ░░░░░░░░░░░░░░░ Fim do programa ░░░░░░░░░░░░░░░\n\n")
