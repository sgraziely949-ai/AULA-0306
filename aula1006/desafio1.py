# Criar um programa que leia uma variável nota com input e mostre na tela:
# > 90 "conceito A"
# Entre 89 e 71 "Conceito B"
# Entre 70 e 61 "conceito C"
# Entre 60 e 50 "Conceito D"
# < 49 "Conceito E"

nota = int(input("Digite uma nota: "))
if nota > 90:
    print("conceito A")
elif nota <= 89 and nota >= 71:
    print("conceito B")
elif nota <= 70 and nota >= 61:
    print("conceito C")
elif nota <= 60 and nota >= 50:
    print("conceito D")
else:
    print("conceito E")