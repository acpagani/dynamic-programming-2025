from time import sleep


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



car_ex = register_cars()

remove_cars(car_ex)
