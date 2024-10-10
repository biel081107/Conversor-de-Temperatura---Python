#CONVERSOR DE TEMPERATURA

from MinhasFunções.texto import titulo,menu,linha,cronometro

temp = 0
vezes = 0
while True:
    titulo('BEM VINDO AO CONVERSOR DE TEMPERATURAS','\033[1;91m')
    opcdeinserir = ['INSERIR GRAUS CELSIUS','INSERIR GRAUS FAHRENHEIT','INSERIR GRAUS KELVIN','FINALIZAR']
    opcdeconversão = ['CONVERTER PARA GRAUS CELSIUS','CONVERTER PARA GRAUS FAHRENHEIT',
                      'CONVERTER PARA GRAUS KELVIN','FINALIZAR']
    menu(opcdeinserir,'\033[1;93m')
    linha('\033[1;94m',20)
    inserir = int(input('\033[1;93mDESEJA INSERIR QUAL TEMPERATURA: \033[m'))
    if inserir > len(opcdeinserir) - 1 or inserir < 0:
        print(f'\033[1;31mOPÇÃO INVALIDA! VERIFIQUE SE DIGITOU AS OPÇÕES CORRETAMENTE, E TENTE '
              f'NOVAMENTE')
        cronometro(5)
    else:
        if inserir == 0:
            temp = int(input('\033[1;97mINSIRA OS GRAUS CELSIUS: \033[m'))
            print(f'\033[1;92mTEMPERATURA INSERIDA COM SUCESSO!!!\033[m')
            cronometro(5,'APROVEITE A CONVERSÃO')
        elif inserir == 1:
            temp = int(input('\033[1;97mINSIRA OS GRAUS FAHRENHEIT: \033[m'))
            print(f'\033[1;92mTEMPERATURA INSERIDA COM SUCESSO!!!\033[m')
            cronometro(5,'APROVEITE A CONVERSÃO')
        elif inserir == 2:
            temp = int(input('\033[1;97mINSIRA OS GRAUS KELVIN: \033[m'))
            print(f'\033[1;92mTEMPERATURA INSERIDA COM SUCESSO!!!\033[m')
            cronometro(5,'APROVEITE A CONVERSÃO')
        elif inserir == 3:
            cronometro(5,'FINALIZADO COM SUCESSO!!!','\033[1;92m')
            break
        while True:
            titulo('MENU DE CONVERSÃO','\033[1;94m')
            menu(opcdeconversão,'\033[1;95m')
            linha('\033[1;94m',20)
            conversao = int(input('\033[1;95mPARA QUAL TEMPERATURA VOCÊ DESEJA CONVERTER: \033[m'))


            if conversao > len(opcdeconversão) - 1 or conversao < 0:
                print(f'\033[1;31mOPÇÃO INVALIDA! VERIFIQUE SE DIGITOU AS OPÇÕES CORRETAMENTE, E TENTE '
                      f'NOVAMENTE')
                cronometro(5)
            else:
                # OPÇÕES PARA CELSIUS
                if inserir == 0:
                    if conversao == 0:
                        print(f'\033[1;94mVOCÊ JA DIGITOU EM CELSIUS!!'
                              f'A TEMPERATURA EM CELSIUS É {temp}°C\033[m')
                        cronometro(5)
                    elif conversao == 1:
                        f = temp * 1.8 + 32
                        print(f'\033[1;94mA TEMPERATURA INSERIDA FOI {temp}°C'
                              f' PASSADA PARA FAHRENHEIT É {f}°F\033[m')
                        cronometro(5)
                    elif conversao == 2:
                        k = temp + 273.15
                        print(f'\033[1;94mA TEMPERATURA INSERIDA FOI {temp}°C'
                              f' PASSADA PARA KELVIN É {k}K\033[m')
                        cronometro(5)

                # OPÇÕES PARA FAHRENHEIT
                if inserir == 1:
                    if conversao == 0:
                        c = (temp - 32) * 5/9
                        print(f'\033[1;93mA TEMPERATURA INSERIDA FOI {temp}°F'
                              f' PASSADA PARA CELSIUS É {c}°C\033[m')
                        cronometro(5)
                    elif conversao == 1:
                        print(f'\033[1;93mVOCÊ JA DIGITOU EM FAHRENHEIT!!'
                              f'A TEMPERATURA EM FAHRENHEIT É {temp}°F\033[m')
                        cronometro(5)
                    elif conversao == 2:
                        k = (temp - 32) * 5/9 + 273.15
                        print(f'\033[1;94mA TEMPERATURA INSERIDA FOI {temp}°F'
                              f' PASSADA PARA KELVIN É {k}K\033[m')
                        cronometro(5)

                #OPÇÕES PARA KELVIN
                if inserir == 2:
                    if conversao == 0:
                        c = temp - 273.15
                        print(f'\033[1;93mA TEMPERATURA INSERIDA FOI {temp} K'
                              f' PASSADA PARA CELSIUS É {c:.2f}°C\033[m')
                        cronometro(5)
                    elif conversao == 1:
                        f = (temp - 273.15) * 9/5 + 32
                        print(f'\033[1;94mA TEMPERATURA INSERIDA FOI {temp}K'
                              f' PASSADA PARA FAHRENHEIT É {f:.2f}K\033[m')
                        cronometro(5)
                    elif conversao == 2:
                        print(f'\033[1;93mVOCÊ JA DIGITOU EM KELVIN!! '
                              f'A TEMPERATURA EM KELVIN É {temp}K\033[m')
                        cronometro(5)
                if conversao == 3:
                    cronometro(5, 'FINALIZADO COM SUCESSO!!!', '\033[1;92m')
                    break


linha('\033[1;97m',20)
print(f'\033[1;92mMUITO OBRIGADO!! VOLTE SEMPRE.')
