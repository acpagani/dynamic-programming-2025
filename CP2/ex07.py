from time import sleep


# Ex04
def binary_search(target, search_list):
    l = 0
    h = len(search_list) - 1

    while l <= h:
        m = (l + h) // 2

        if target == search_list[m]:
            print(f"Alvo {target} encontrado! Índice {m}")
            sleep(1.5)
            return m

        elif target > search_list[m]:
            l = m + 1
            print(f"Alvo localizado na ramificação à direita: {search_list[l:(h + 1)]}")
            sleep(1.5)

        elif target < search_list[m]:
            h = m - 1
            print(f"Alvo localizado na ramificação à esquerda: {search_list[l:(h + 1)]}")
            sleep(1.5)

    return "Alvo não encontrado!"


# Ex05
def take_orders():
    people = []

    for c in range(10):
        name = input(f"Nome da pessoa que vai fazer o pedido: ")
        people.append(name)

    return people


def serve_queue(people_queue):
    print("\nAtendendo pessoas...")
    while people_queue:
        served_person = people_queue.pop(0)
        print(f"{served_person} atendido(a) com sucesso!")
        sleep(1.5)

    print("\nTodas as pessoas foram atendidas com sucesso!\n")
    sleep(1.5)


# Ex06
def register_cars():
    cars = []

    for c in range(10):
        license_plate = input(f"Registrar placa do carro n° {c + 1}: ")
        cars.append(license_plate)

    return cars


def remove_cars(cars_stack):
    print("\nRetirando carros...")
    while cars_stack:
        removed_car = cars_stack.pop()
        print(f"Carro retirado com sucesso! Placa {removed_car}")
        sleep(1.5)
    print("\nTodos os carros foram retirados com sucesso!\n")
    sleep(1.5)


# MENU
def menu():
    print("=" * 30)
    print("ALGORITMO A SER UTILIZADO".center(30))
    print("=" * 30)

    option = int(input("""\t1. Buscar um determinado item da lista [3, 5, 7, 8, 11, 14, 15] (Busca binária)
    2. Registro e retirada de carros de um estacionamento (LIFO)
    3. Atender clientes em uma fila (FIFO)

    Opção (Para sair, digite 0): """))
    print()

    return option


###

while True:
    opt = menu()
    match opt:
        case 0:
            break

        case 1:
            search_num = int(input("Digite um número a ser buscado: "))
            binary_search(search_num, [3, 5, 7, 8, 11, 14, 15])

        case 2:
            car_ex = register_cars()
            remove_cars(car_ex)

        case 3:
            pessoas_exemplo = take_orders()
            serve_queue(pessoas_exemplo)

        case _:
            print("Opção inválida! Tente novamente")

print("PROGRAMA ENCERRADO")

