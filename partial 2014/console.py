from controller import *
ctrl=controller()
ctrl.repo.incarca_din_fisier()

def show_menu():
    print('1-sterge tip')
    print('2-sterge max')
    print('3-exit')
    alegere=int(input('Alegeti optiunea: '))
    return alegere
def sterge_tip():
    tip=raw_input('Alegeti tipul: ')
    ctrl.sterge_biciclete_tip(tip)
    

while True:
    alegere=show_menu()
    if alegere==3:
        break
    if alegere==2:
        ctrl.sterge_max()
        ctrl.repo.salveaza()
    if alegere==1:
        sterge_tip()
        ctrl.repo.salveaza()
        
        
