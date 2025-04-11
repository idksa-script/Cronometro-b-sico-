import time

hora = 0
minutos = 0
segundos = 0

while True:

    print(f"{hora:02}:{minutos:02}:{segundos:02}")
    segundos+=1
    time.sleep(1)

    if hora > 24:
        print("Llego a 24 horas, fin del cronometro")
        exit()
    if minutos == 60:
        hora+=1
        minutos = 0
    if segundos == 60:
        minutos+=1
        segundos = 0
