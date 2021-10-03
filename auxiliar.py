def pausa():
    input("Tecle <ENTER> para continuar...\n")

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
