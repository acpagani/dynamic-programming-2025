from time import sleep

high_priority = []
low_priority = []

while True:
    value = input("Nome do arquivo (P para parar): ")

    if value.upper() == "P":
        break

    priority = input("Grau de prioridade do arquivo (Alta - A / Baixa - B): ")

    if priority.upper() == "A":
        high_priority.append(value)

    elif priority.upper() == "B":
        low_priority.append(value)

    else:
        print("Digite uma opção válida.")
        continue

sleep(1)
print("Parou! Imprimindo arquivos...")
sleep(3)

while high_priority:
    doc = high_priority.pop(0)

    print(f"Imprimindo arquivo {doc}")
    sleep(1)

while low_priority:
    doc = low_priority.pop(0)

    print(f"Imprimindo arquivo {doc}")
    sleep(1)