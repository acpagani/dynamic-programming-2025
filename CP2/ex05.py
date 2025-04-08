from time import sleep


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


people_ex = take_orders()

serve_queue(people_ex)
