from time import sleep


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


target_ex = 11
list_ex = [3, 5, 7, 8, 11, 14, 15]

print(binary_search(target_ex, list_ex))