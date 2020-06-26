# Specificare i 2 numeri prima di farlo partire
n1 = int(input('numero1: '))
n2 = int(input('numero2: '))
n3 = int(input('numero3: '))

# Specificare i 2 colori prima di farlo partire
c1 = input('colore1: ')
c2 = input('colore2: ')

from turtle import *
title('Disegno Custom')
color(c1, c2)

begin_fill()
while True:
    forward(n1)
    left(n2)
    circle(n3)
    if abs(pos()) < 1:
        break
end_fill()
done()
