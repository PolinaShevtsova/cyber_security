ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_"

def sym2num(sym_in: str) -> int:
    if sym_in == "_":
        return 0
    return ALPHABET.index(sym_in) + 1
# print(sym2num("О"))  # 15
# print(sym2num("Ж"))  # 7
# print(sym2num("_"))  # 0

def num2sym(num_in: int) -> str:
    if num_in == 0:
        return "_"
    return ALPHABET[num_in - 1]
# print(num2sym(7))   # Ж
# print(num2sym(14))  # Н
# print(num2sym(0))   # _

def text2array(txt_in: str) -> list[int]:
    out = []
    for ch in txt_in:
        out.append(sym2num(ch))
    return out

def array2text(arr_in: list[int]) -> str:
    out = ""
    for num in arr_in:
        out += num2sym(num)
    return out

# IN_TEXT = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_"
# OUT_ARR = text2array(IN_TEXT)
# print(OUT_ARR)
# OUT_TEXT = array2text(OUT_ARR)
# print(OUT_TEXT)

def add_s(s1: str, s2: str) -> str:
    tmp = sym2num(s1) + sym2num(s2)
    return num2sym(tmp % 32)

def sub_s(s1: str, s2: str) -> str:
    tmp = sym2num(s1) - sym2num(s2) + 32
    return num2sym(tmp % 32)

# print(add_s("Я", "Ж"))  # Е
# print(sub_s("Е", "Ж"))  # Я

def add_txt(T1_IN: str, T2_IN: str) -> str:
    out = ""
    m = min(len(T1_IN), len(T2_IN))

    if len(T1_IN) > len(T2_IN):
        T_IN = T1_IN
    else:
        T_IN = T2_IN

    M = len(T_IN)

    for i in range(m):
        t1 = T1_IN[i]
        t2 = T2_IN[i]
        out += add_s(t1, t2)

    if M > m:
        for i in range(m, M):
            out += T_IN[i]

    return out

def sub_txt(T1_IN: str, T2_IN: str) -> str:
    out = ""
    m = min(len(T1_IN), len(T2_IN))

    if len(T1_IN) > len(T2_IN):
        T_IN = T1_IN
        flag = 0
    else:
        T_IN = T2_IN
        flag = 1

    M = len(T_IN)
    for i in range(m):
        t1 = T1_IN[i]
        t2 = T2_IN[i]
        out += sub_s(t1, t2)

    if M > m:
        for i in range(m, M):
            t = T_IN[i]
            if flag == 1:
                out += sub_s("_", t)
            else:
                out += sub_s(t, "_")

    return out
# TT1 = "ЕЖИК"
# TT2 = "В_ТУМАНЕ"
# T5 = add_txt(TT1, TT2)
# print(T5)  # ИЖЬЯМАНЕ
# TT3 = "БАРОН"
# TT4 = "ВАРАН"
# TT6 = sub_txt(TT3, TT4)
# print(TT6)  # Я_Н_
# print(add_txt(TT6, TT4))  # БАРОН
# print(sub_txt(T5, TT2))   # ЕЖИК____
# print(sub_txt(T5, TT1))   # В_ТУМАНЕ

def frw_Cesar(TXT_IN: str, KEY_IN: str) -> str:
    out = ""
    key = KEY_IN[0]

    for i in range(len(TXT_IN)):
        tmp = TXT_IN[i]
        out += add_s(tmp, key)

    return out

def inv_Cesar(TXT_IN: str, KEY_IN: str) -> str:
    out = ""
    key = KEY_IN[0]

    for i in range(len(TXT_IN)):
        tmp = TXT_IN[i]
        out += sub_s(tmp, key)

    return out

# IN_TEXT = "ОЛОЛО_КРИНЖ"
# K1 = "_"
# K2 = "Х"
# OUT1 = frw_Cesar(IN_TEXT, K1)
# OUT2 = frw_Cesar(IN_TEXT, K2)
# print(OUT1)  # ОЛОЛО_КРИНЖ
# print(OUT2)  # ДБДБДХЖАГЭ
# print(inv_Cesar(OUT1, K1))  # ОЛОЛО_КРИНЖ
# print(inv_Cesar(OUT2, K2))  # ОЛОЛО_КРИНЖ

def frw_poly_Caesar(TXT_IN: str, KEY_IN: str) -> str:
    out = ""
    t_k = ""
    K = len(KEY_IN)

    for i in range(len(TXT_IN)):
        t_i = TXT_IN[i]
        q = i % K
        t_k = add_s(t_k, KEY_IN[q]) if t_k else KEY_IN[q]
        out += add_s(t_i, t_k)

    return out

def inv_poly_Caesar(TXT_IN: str, KEY_IN: str) -> str:
    out = ""
    t_k = ""
    K = len(KEY_IN)

    for i in range(len(TXT_IN)):
        t_i = TXT_IN[i]
        q = i % K
        t_k = add_s(t_k, KEY_IN[q]) if t_k else KEY_IN[q]
        out += sub_s(t_i, t_k)

    return out

# IN_TEXT = "ОЛОЛО_КРИНЖ"
# K1 = "Х"
# K2 = "ПАНТЕОН"
# OUT1 = frw_poly_Caesar(IN_TEXT, K1)
# OUT2 = frw_poly_Caesar(IN_TEXT, K2)
# print(OUT1)  # ДЧРГГДАЮЙШ
# print(OUT2)  # ЯЭНЮЖЖ_ХОБН
# print(inv_poly_Caesar(OUT1, K1))  # ОЛОЛО_КРИНЖ
# print(inv_poly_Caesar(OUT2, K2))  # ОЛОЛО_КРИНЖ

def frm_S_Caesar(BLOCK_IN: str, KEY_IN: str) -> str:
    if len(BLOCK_IN) != 4 or len(KEY_IN) != 16:
        return "input_error"
    C = [1, -1, 1, 2, -2, 1, 1, 3, -1, 2]
    KEY_EXT = KEY_IN + KEY_IN
    out = BLOCK_IN
    KEY_TMP = "___"
    for i in range(8):
        start_pos = i * 2
        S_TMP = KEY_EXT[start_pos:start_pos + 4]
        B_TMP = text2array(S_TMP)
        A_TMP = [0 for i in range(4)]
        for k in range(4):
            x = (2 * i + k) % 10
            value = 64 + k + C[x] * B_TMP[k]
            A_TMP[k] = value % 32

            # Преобразование числа обратно в символ и добавление к KEY_TMP
        KEY_TMP = add_txt(KEY_TMP, array2text(A_TMP))

    # Применение полиалфавитного шифра Цезаря с полученным ключом
    out = frw_poly_Caesar(out, KEY_TMP)
    return out


def inw_S_Caesar(BLOCK_IN: str, KEY_IN: str) -> str:
    if len(BLOCK_IN) != 4 or len(KEY_IN) != 16:
        return "input_error"
    C = [1, -1, 1, 2, -2, 1, 1, 3, -1, 2]
    KEY_TMP = "___"
    KEY_EXT = KEY_IN + KEY_IN

    for i in range(8):
        start_pos = i * 2
        S_TMP = KEY_EXT[start_pos:start_pos + 4]
        B_TMP = text2array(S_TMP)
        A_TMP = [0 for i in range(4)]

        for k in range(4):
            x = (2 * i + k) % 10
            # Вычисление A_TMP = mod(64 + k + C[x] * B_TMP[k], 32)
            value = 64 + k + C[x] * B_TMP[k]
            A_TMP[k] = value % 32

            # Преобразование числа обратно в символ и добавление к KEY_TMP
        KEY_TMP = add_txt(KEY_TMP, array2text(A_TMP))

    # Применение обратного полиалфавитного шифра Цезаря с полученным ключом
    out = inv_poly_Caesar(BLOCK_IN, KEY_TMP)
    return out


# # Тестирование функций с примерами из MathCAD
# if __name__ == "__main__":
#     # Ключи из примера
#     K1 = "ХОРОШО_БЫТЬ_ВАМИ"
#     K2 = "ЧЕРНОВОЙ_АХИЛЛЕС"
#
#     # Тестовые данные
#     IN1 = "БЛОК"
#
#     # Прямое преобразование
#     OUT11 = frm_S_Caesar(IN1, K1)
#     OUT21 = frm_S_Caesar(IN1, K2)
#
#     print(f"IN1 = '{IN1}'")
#     print(f"OUT11 = frm_S_Caesar(IN1, K1) = '{OUT11}' (ожидается 'АЗЩЯ')")
#     print(f"OUT21 = frm_S_Caesar(IN1, K2) = '{OUT21}' (ожидается 'СЮАЖ')")
#     print()
#
#     # Обратное преобразование
#     INr11 = inw_S_Caesar(OUT11, K1)
#     INe11 = inw_S_Caesar(OUT11, K2)
#     INr21 = inw_S_Caesar(OUT21, K2)
#     INe21 = inw_S_Caesar(OUT21, K1)
#
#     print(f"INr11 = inw_S_Caesar(OUT11, K1) = '{INr11}' (ожидается 'БЛОК')")
#     print(f"INe11 = inw_S_Caesar(OUT11, K2) = '{INe11}' (ожидается 'РХЗВ')")
#     print(f"INr21 = inw_S_Caesar(OUT21, K2) = '{INr21}' (ожидается 'БЛОК')")
#     print(f"INe21 = inw_S_Caesar(OUT21, K1) = '{INe21}' (ожидается 'ТБХТ')")
#     print()
#
#     # Проверка на неверные входные данные
#     test1 = frm_S_Caesar("БЛО", K1)  # Слишком короткий блок
#     test2 = frm_S_Caesar("БЛОК", "короткий_ключ")  # Слишком короткий ключ
#
#     print(f"Тест с коротким блоком: '{test1}' (ожидается 'input_error')")
#     print(f"Тест с коротким ключом: '{test2}' (ожидается 'input_error')")

def frw_merge_block(BLOCK_IN: str, KEY_IN: str) -> str:
    if len(BLOCK_IN) != 4 or len(KEY_IN) != 16:
        return "input_error"
    M = [0, 1, 2, 3]
    array = text2array(KEY_IN)
    sum_val = 0

    for i in range(16):
        term = (-1) ** i * array[i]
        sum_val = (24 + sum_val + term) % 24

    for k in range(3):
        t = sum_val % (4 - k)
        sum_val = (sum_val - t) // (4 - k)
        tmp = M[k]
        M[k] = M[k + t]
        M[k + t] = tmp

    inp = text2array(BLOCK_IN)
    for j in range(4):
        b = M[(j + 1) % 4]
        a = M[j % 4]
        inp[b] = (inp[b] + inp[a]) % 32
    out = array2text(inp)

    return out


def inv_merge_block(BLOCK_IN: str, KEY_IN: str) -> str:
    if len(BLOCK_IN) != 4 or len(KEY_IN) != 16:
        return "input_error"
    M = [0, 1, 2, 3]
    array = text2array(KEY_IN)
    sum_val = 0
    for i in range(16):
        term = (-1) ** i * array[i]
        sum_val = (24 + sum_val + term) % 24

    for k in range(3):
        t = sum_val % (4 - k)
        sum_val = (sum_val - t) // (4 - k)
        tmp = M[k]
        M[k] = M[k + t]
        M[k + t] = tmp

    inp = text2array(BLOCK_IN)
    for j in range(3, -1, -1):
        b = M[(j + 1) % 4]
        a = M[j % 4]
        inp[b] = (32 - inp[a] + inp[b]) % 32
    out = array2text(inp)

    return out

def frw_S_CaesarM(BLOCK_IN: str, KEY_IN: str) -> str:
    tmp = frw_merge_block(BLOCK_IN, KEY_IN)
    tmp = frm_S_Caesar(tmp, KEY_IN)
    out = frw_merge_block(tmp, KEY_IN)
    return out


def inv_S_CaesarM(BLOCK_IN: str, KEY_IN: str) -> str:
    tmp = inv_merge_block(BLOCK_IN, KEY_IN)
    tmp = inw_S_Caesar(tmp, KEY_IN)
    out = inv_merge_block(tmp, KEY_IN)
    return out

# if __name__ == "__main__":
#     K1 = "ХОРОШО_ВЫТЬ_ВАМИ"
#     K2 = "ХОРОШО_БЫТЬ_ВАМИ"
#     K3 = "ХОРОШО_ВЫТЬ_ВАМИ"
#
#     IN1 = "БЛОК"
#     IN2 = "БРОК"
#
#     print("Тестирование frw_merge_block:")
#     print("=" * 60)
#
#     # Тест 1
#     OUT1 = frw_merge_block(IN1, K1)
#     print(f"OUT1 = frw_merge_block('{IN1}', K1) = '{OUT1}' (ожидается 'Ь3ЦЩ')")
#
#     # Тест 2
#     OUT2 = frw_merge_block(IN2, K1)
#     print(f"OUT2 = frw_merge_block('{IN2}', K1) = '{OUT2}' (ожидается 'ЬMЬЩ')")
#
#     # Тест 3
#     OUT3 = frw_merge_block(IN1, K2)
#     print(f"OUT3 = frw_merge_block('{IN1}', K2) = '{OUT3}' (ожидается 'МЗЬТ')")
#
#     # Тест 4
#     OUT4 = frw_merge_block(IN2, K2)
#     print(f"OUT4 = frw_merge_block('{IN2}', K2) = '{OUT4}' (ожидается 'MMbЧ')")
#
#     print("\n" + "=" * 60)
#     print("Тестирование inv_merge_block:")
#     print("=" * 60)
#
#     # Обратные преобразования
#     print(f"inv_merge_block('{OUT1}', K1) = '{inv_merge_block(OUT1, K1)}' (ожидается 'БЛОК')")
#     print(f"inv_merge_block('{OUT2}', K1) = '{inv_merge_block(OUT2, K1)}' (ожидается 'БРОК')")
#     print(f"inv_merge_block('{OUT3}', K1) = '{inv_merge_block(OUT3, K1)}' (ожидается 'ЩЫУЯ')")
#     print(f"inv_merge_block('{OUT4}', K1) = '{inv_merge_block(OUT4, K1)}' (ожидается 'Ф_ОИ')")
#
#     print(f"inv_merge_block('{OUT1}', K2) = '{inv_merge_block(OUT1, K2)}' (ожидается 'ЙРЫС')")
#     print(f"inv_merge_block('{OUT2}', K2) = '{inv_merge_block(OUT2, K2)}' (ожидается 'ОР_М')")
#     print(f"inv_merge_block('{OUT3}', K2) = '{inv_merge_block(OUT3, K2)}' (ожидается 'БЛОК')")
#     print(f"inv_merge_block('{OUT4}', K2) = '{inv_merge_block(OUT4, K2)}' (ожидается 'БРОК')")
#
#     print("\n" + "=" * 60)
#     print("Тестирование frw_S_CaesarM:")
#     print("=" * 60)
#
#     # Тестирование модифицированной функции
#     OUT1M = frw_S_CaesarM(IN1, K1)
#     print(f"OUT1M = frw_S_CaesarM('{IN1}', K1) = '{OUT1M}' (ожидается 'УЫ_Ш')")
#
#     # Обратное преобразование
#     IN1M = inv_S_CaesarM(OUT1M, K1)
#     print(f"inv_S_CaesarM('{OUT1M}', K1) = '{IN1M}' (ожидается 'БЛОК')")