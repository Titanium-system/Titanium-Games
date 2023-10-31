#modules

import sys,time,random

#functions

typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

catalog = ['AutoWeaken.exe', 'PortCrackV1.exe']
Dinput = 'null'
balance = 10000
programs = []
def darkwebFunc():
    price = 0
    i = 0
    while i != 3:

        Dinput = input('darkweb >>> ')
        if Dinput == 'catalog':
           print(catalog)
        elif Dinput == 'buy':
            parameter = input('server <<< buy item:')
            if parameter in catalog:
                if parameter == 'AutoWeaken.exe':
                    print('server <<< bought AutoWeaken.exe')
                    programs.append('AutoWeaken.exe')
                    price += 3000
                elif parameter == PortCrackV1.exe:
                    print('server <<< bought PortCrackV1.exe')
                    programs.append('PortCrackV1.exe')
                    price += 5000
            elif Dinput != 'home':
                print('darkweb server does not support this function or function does not exist')
            elif Dinput == 'home':
                print(123)
                break
        Dinput = 'null'
        i = i + 1
    print('Thank you for visiting the darkweb')


#Initialize

RAM = 8.00
server = 'home'
commandList = ['hack', 'weaken', 'grow,' 'scan', 'free', 'helper', 'connect', 'home', 'darkweb']
parameter = 'null'

#main

print('Welcome to a GigaBitGames game')
print('This is a hacking game that is a simpler version of bitburner .search bitburner to see what this is ')
print('\n \n')

while True:
    mainInput = input(server + '  >>>  ')

    if mainInput in commandList :
        if mainInput == 'helper':
            print(commandList)
        if mainInput == 'weaken':
            if server == 'home':
                print('Cannot weaken home')
            else:
                print('Weakening ' + server)
                slow_type('###############')
                print('DONE')
        if mainInput == 'connect':
            parameter = input('Connect to what server')
            server = parameter
            print('Connected to ' + server)
        if mainInput == 'home':
            print('Connected to home')
            server = 'home'
        if mainInput == 'darkweb':

            darkwebFunc()

    else:
        print('Syntax Error please try a command in the command list Type helper to display this')


