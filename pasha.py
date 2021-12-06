def pasha(god: int, st: bool) -> list:
    # god - год, в который хотим узнать каогда будет Пасха
    # st - старый стиль (0), новый стиль (1)
    # вывод списком [a, b] a - число, b - месяц
    ps = [0, ""]
    d = (god % 19 * 19 + 15) % 30
    e = (god % 4 * 2 + god % 7 * 4 + 6 * d + 6) % 7
    if (d + e) > (10 + st * 16):
        ps[0] = d + e - 9 - st * 17
        ps[1] = "апреля (ст.ст.)" if st == 0 else "мая (н.ст.)"
    else:
        ps[0] = d + e + 22 - st * 18
        ps[1] = "марта (ст.ст.)" if st == 0 else "апреля (н.ст.)"
    return ps


if __name__ == '__main__':
    god_pashi = int(input("Введите год, в который хотите узнать дату Пасхи"))
    inp_st = input("По новому стилю? Y/N")
    styl = 0 if inp_st == "N" or inp_st == "n" else 1
    pas = pasha(god_pashi, styl)
    print(f"Пасха в {god_pashi} будет {pas[0]} {pas[1]}")
