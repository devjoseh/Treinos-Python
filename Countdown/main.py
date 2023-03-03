#Faz a importação do time que é do próprio python
import time

#Começa a função countdown
def countdown(t):
    while t:
        #faz a conta do tempo
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #Deixa o countdown ativo até acabar o tempo
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1

    #Envia uma mensagem no console
    print('Timer finalizado')

#Envia um input no console perguntando quanto tempo terá o countdown
timeQ = int(input('Coloque o tempo em segundos: '))

#Inicia o countdown com as informações do input
countdown(timeQ)