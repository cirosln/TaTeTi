import time as tm
from colorama import Fore, Style

figuras = ['❌', '🔵']
fila = []
turnoA = 0
turnoR = 0
ganador = 0
rojo = Fore.RED
azul = Fore.BLUE
amarillo = Fore.YELLOW
reinicio = Style.RESET_ALL

tm.sleep(1)
print(f"""
{rojo}████████╗{azul} █████╗ {rojo}████████╗{azul}███████╗{rojo}████████╗{azul}██╗
{rojo}╚══██╔══╝{azul}██╔══██╗{rojo}╚══██╔══╝{azul}██╔════╝{rojo}╚══██╔══╝{azul}██║
{rojo}   ██║   {azul}███████║{rojo}   ██║   {azul}█████╗  {rojo}   ██║   {azul}██║
{rojo}   ██║   {azul}██╔══██║{rojo}   ██║   {azul}██╔══╝  {rojo}   ██║   {azul}██║
{rojo}   ██║   {azul}██║  ██║{rojo}   ██║   {azul}███████╗{rojo}   ██║   {azul}██║
{rojo}   ╚═╝   {azul}╚═╝  ╚═╝{rojo}   ╚═╝   {azul}╚══════╝{rojo}   ╚═╝   {azul}╚═╝
""")

tm.sleep(1.2)
while True:
    print(amarillo + f'Elige con que figura empezar')
    tm.sleep(0.8)
    print(rojo + "Presiona '1' si empieza ❌")
    tm.sleep(0.8)
    print(azul + "Presiona '2' si empieza 🔵")
    tm.sleep(0.8)
    choice = input(amarillo + 'Presiona aquí: ' + reinicio)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            break
        elif choice == 2:
            figuras.reverse()
            break
        else:
            tm.sleep(0.5)
            print(amarillo + 'Elige un número válido')
            tm.sleep(0.8)
    else:
        tm.sleep(0.5)
        print(amarillo + 'Solamente elige números')
        tm.sleep(0.8)

for i in range(10):
    fila.append(i)

while True:
    if all(fila[i] == '🔵' for i in [1, 2, 3]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [4, 5, 6]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [7, 8, 9]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [1, 4, 7]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [2, 5, 8]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [3, 6, 9]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [1, 5, 9]):
        ganador = '🔵'
    elif all(fila[i] == '🔵' for i in [3, 5, 7]):
        ganador = '🔵'
    elif all(fila[i] == '❌' for i in [1, 2, 3]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [4, 5, 6]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [7, 8, 9]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [1, 4, 7]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [2, 5, 8]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [3, 6, 9]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [1, 5, 9]):
        ganador = '❌'
    elif all(fila[i] == '❌' for i in [3, 5, 7]):
        ganador = '❌'
    
    if ganador not in figuras and all(fila[i] in figuras for i in range(1, 10)):
        tm.sleep(0.5)
        print(amarillo)
        for i in range(9):
            print(fila[i+1], end=' | ')
            if i == 2 or i == 5:
                print()
        
        tm.sleep(0.8)
        print()
        print('\nEmpate.')
        tm.sleep(0.8)
        reiniciar = input('Quieres reiniciar el juego? \nSi/No: ' + reinicio).lower()
        if reiniciar == 'si':
            fila = []
            for i in range(10):
                fila.append(i)
            turnoA = 0
            turnoR = 0
            ganador = 0
        else:
            break
    
    elif ganador not in figuras:
        if turnoA > 0 or turnoR > 0:
            if turnoA != turnoR:
                if figuras[1] == '🔵':
                    tm.sleep(0.5)
                    print(azul + f'Turno de {figuras[1]}')
                    turnoA += 1
                else:
                    tm.sleep(0.5)
                    print(rojo + f'Turno de {figuras[1]}')
                    turnoR += 1
            else:
                if figuras[0] == '🔵':
                    tm.sleep(0.5)
                    print(azul + f'Turno de {figuras[0]}')
                    turnoA += 1
                else:
                    tm.sleep(0.5)
                    print(rojo + f'Turno de {figuras[0]}')
                    turnoR += 1
        elif turnoR == 0 and turnoA == 0:
            if figuras[0] == '🔵':
                tm.sleep(0.5)
                print(azul + f'Elige un número del tablero para reemplazar con la forma {figuras[0]}')
                turnoA += 1
            else:
                tm.sleep(0.5)
                print(rojo + f'Elige un número del tablero para reemplazar con la forma {figuras[0]}')
                turnoR += 1
        
        tm.sleep(0.5)
        print(amarillo)
        for i in range(9):
            print(fila[i+1], end=' | ')
            if i == 2 or i == 5:
                print()
    
        tm.sleep(0.3)
        print()
        resp = input('\nIngrese el número aquí: ' + reinicio)
        
        if resp.isdigit():
            resp = int(resp)
            if resp >= 1 and resp <= 9:
                if fila[resp] not in figuras:
                    if turnoA != turnoR:
                        fila[resp] = figuras[0]
                    else:
                        fila[resp] = figuras[1]
                else:
                    tm.sleep(0.5)
                    print(amarillo + 'Esa posición ya está ocupada')
                    if turnoA != turnoR:
                        if figuras[0] == '🔵':
                            turnoA -= 1
                        else:
                            turnoR -= 1
                    else:
                        if figuras[1] == '🔵':
                            turnoA -= 1
                        else:
                            turnoR -= 1
                
            else:
                tm.sleep(0.5)
                print(amarillo + 'Ingresa un número válido')
                if turnoA != turnoR:
                    if figuras[0] == '🔵':
                        turnoA -= 1
                    else:
                        turnoR -= 1
                else:
                    if figuras[1] == '🔵':
                        turnoA -= 1
                    else:
                        turnoR -= 1
        else:
            tm.sleep(0.5)
            print(amarillo + 'Solamente ingresa un número')
            if turnoA != turnoR:
                if figuras[0] == '🔵':
                    turnoA -= 1
                else:
                    turnoR -= 1
            else:
                if figuras[1] == '🔵':
                    turnoA -= 1
                else:
                    turnoR -= 1
    elif ganador == '🔵':
        tm.sleep(0.5)
        print(amarillo)
        for i in range(9):
            print(fila[i+1], end=' | ')
            if i == 2 or i == 5:
                print()
        
        tm.sleep(0.8)
        print()
        print(azul + '\nEl jugador 🔵 gana.')
        tm.sleep(0.8)
        reiniciar = input(amarillo + 'Quieres reiniciar el juego? \nSi/No: ' + reinicio).lower()
        if reiniciar == 'si':
            fila = []
            for i in range(10):
                fila.append(i)
            turnoA = 0
            turnoR = 0
            ganador = 0
        else:
            break
    else:
        tm.sleep(0.5)
        print(amarillo)
        for i in range(9):
            print(fila[i+1], end=' | ')
            if i == 2 or i == 5:
                print()
        
        tm.sleep(0.8)
        print()
        print(rojo + '\nEl jugador ❌ gana.')
        tm.sleep(0.8)
        reiniciar = input(amarillo + 'Quieres reiniciar el juego? \nSi/No: ' + reinicio).lower()
        if reiniciar == 'si':
            fila = []
            for i in range(10):
                fila.append(i)
            turnoA = 0
            turnoR = 0
            ganador = 0
        else:
            break
tm.sleep(0.8)
print(amarillo + 'Fin del juego!' + reinicio)