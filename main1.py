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

def frw_S_Caesar(BLOCK_IN: str, KEY_IN: str) -> str:
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
#     OUT11 = frw_S_Caesar(IN1, K1)
#     OUT21 = frm_S_Caesar(IN1, K2)
#
#     print(f"IN1 = '{IN1}'")
#     print(f"OUT11 = frw_S_Caesar(IN1, K1) = '{OUT11}' (ожидается 'АЗЩЯ')")
#     print(f"OUT21 = frw_S_Caesar(IN1, K2) = '{OUT21}' (ожидается 'СЮАЖ')")
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
#     test1 = frw_S_Caesar("БЛО", K1)  # Слишком короткий блок
#     test2 = frw_S_Caesar("БЛОК", "короткий_ключ")  # Слишком короткий ключ
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
    tmp = frw_S_Caesar(tmp, KEY_IN)
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

def core_Caesar(in_prime, in_aux):
    if len(in_prime) != 16 or len(in_aux) != 16:
        return "input_error"
    C1 = [1, 1, -1]
    C2 = [4, 3, 2, 1, -1, -2, -3, -4]
    aux = text2array(in_aux)
    prime = text2array(in_prime)
    tmp = 0
    c1 = prime[2] % 3
    c2 = prime[10 + c1] % 8
    c3 = prime[c2 + 3] % 16
    arr = []
    for i in range(32):
        q = (c1 + i) % 3
        j = (c2 + i) % 8
        p = (c3 + i) % 16
        l = i % 16
        tmp = (tmp + 64 +prime[p] + C1[q] * aux[l] + C2[j]) % 32
        arr[l] = tmp
    out = array2text(arr)

    return out

def confuse(in1, in2):
    arr1 = text2array(in1)
    arr2 = text2array(in2)
    for i in range(16):
        if arr1[i] > arr2[i]:
            arr1[i] = (arr1[i] + i) % 32
        else:
            arr1[i] = (arr2[i] + i) % 32
    out = array2text(arr1)

    return out

def compress(in_16, out_n):
    out = "input_error"
    if out_n != 16:
        a1 = in_16[0::4]
        a2 = in_16[4::4]
        a3 = in_16[8::4]
        a4 = in_16[12::4]
        if out_n == 8:
            a13 = a1 + a3
            a24 = a2 + a4
            out = add_txt(a13, a24)
        if out_n == 4:
            a13 = sub_txt(a1, a3)
            a24 = sub_txt(a2, a4)
            out = add_txt(a13, a24)
    else:
        out = in_16

    return out

def c_block(in_arr, out_size):
    out = "input_error"
    r = len(in_arr)
    C = ["________________", "ПРОЖЕКТОР_ЧЕПУХИ",
         "КОЛЫХАТЬ_ПАРОДИЮ", "КАРМАННЫЙ_АТАМАН"]
    flag = 1
    for i in range(r):
        if len(in_arr[i]) != 16:
            C[i] = add_txt(C[i], in_arr[i])
        else:
            flag = 0
    if flag == 1:
        C[1] = add_txt(C[1], in_arr[0])
        tmp1 = core_Caesar(C[0], C[2])
        tmp2 = core_Caesar(C[1], C[3])
        tmp3 = confuse(tmp1, tmp2)
        out = core_Caesar(out, out_size)

    return out

def reverse_str(in_str):
    in_str = text2array(in_str)
    tmp = list(reversed(in_str))
    out = array2text(tmp)
    return out

def blocks_mix(in1, in2):
    in1 = reverse_str(in1)
    out = []
    out[0] = add_txt(in1, in2)
    out[1] = sub_txt(in1, in2)

    return out

def block_mask(in_str, const):
    arr = text2array(in_str)
    con = text2array(const)
    out = []
    for i in range(16):
        if arr[i] > (con[i] + i):
            out[i] = (64 - (con[i] - i)) % 32
        else:
            out[i] = (arr[i] + i) % 32
    out = array2text(out)

    return out

def pad_MD(in_str):
    out = in_str
    l = len(in_str)
    rem = 64 - (l % 64)
    if rem != 64:
        for i in range(rem):
            out += "_"
    return out

def macro_compression(in_str, state):
    a = add_txt(in_str[0::16], state[0::16])
    b = add_txt(in_str[16::16], state[16::16])
    c = add_txt(in_str[32::16], state[32::16])
    d = add_txt(in_str[48::16], state[48::16])
    e = state[64::16]
    con = "ААААЯЯЯЯЯААЯЯААЯЯ"
    for i in range(12):
        e = add_txt(e, c_block([a, b, c, d], "16"))
        tmp = blocks_mix(c, d)
        con = add_txt(con, "ААААЯЯЯЯААЯЯААЯЯ")
        c = tmp[0]
        d = tmp[1]
        b = block_mask(b, con)
        a, b, c, d, e = b, c, d, e, a
    out = [a, b, c, d, e]

    return out

def MerDam_hash(msg):
    data = pad_MD(msg)
    temp = ""
    n = len(data) // 64
    a, b, c, d, e = ("________________", "________________",
                     "________________", "________________",
                     "________________")
    for i in range(n):
        tmp = data[i*64::64]
        state = macro_compression(tmp, (a + b + c + d + e))
        a, b, c, d, e = state
    p1 = c_block([a, e], "16")
    p2 = c_block([b, e], "16")
    p3 = c_block([c, e], "16")
    p4 = c_block([d, e], "16")
    out = p1 + p2 + p3 + p4

    return out
