class Alphabet:
    ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_"

    @classmethod
    def sym2num(cls, sym_in: str) -> int:
        if sym_in == "_":
            return 0
        return cls.ALPHABET.index(sym_in) + 1

    @classmethod
    def num2sym(cls, num_in: int) -> str:
        if num_in == 0:
            return "_"
        return cls.ALPHABET[num_in - 1]

    @classmethod
    def text2array(cls, txt_in: str) -> list[int]:
        out = []
        for ch in txt_in:
            out.append(cls.sym2num(ch))
        return out

    @classmethod
    def array2text(cls,arr_in: list[int]) -> str:
        out = ""
        for num in arr_in:
            out +=cls.num2sym(num)
        return out

    @classmethod
    def reverse_str(cls, in_str: str) -> str:
        arr = cls.text2array(in_str)
        return cls.array2text(list(reversed(arr)))


class ArithmeticOperations:
    def __init__(self, alphabet_class=Alphabet):
        self.alphabet = alphabet_class

    def add_s(self, s1: str, s2: str) -> str:
        tmp = self.alphabet.sym2num(s1) + self.alphabet.sym2num(s2)
        return self.alphabet.num2sym(tmp % 32)

    def sub_s(self, s1: str, s2: str) -> str:
        tmp = self.alphabet.sym2num(s1) - self.alphabet.sym2num(s2) + 32
        return self.alphabet.num2sym(tmp % 32)

    def add_txt(self, t1_in: str, t2_in: str) -> str:
        out = ""
        min_len = min(len(t1_in), len(t2_in))
        t_in = t1_in if len(t1_in) > len(t2_in) else t2_in

        for i in range(min_len):
            out += self.add_s(t1_in[i], t2_in[i])

        if len(t_in) > min_len:
            for i in range(min_len, len(t_in)):
                out += t_in[i]

        return out

    def sub_txt(self, t1_in: str, t2_in: str) -> str:
        out = ""
        min_len = min(len(t1_in), len(t2_in))

        if len(t1_in) > len(t2_in):
            t_in = t1_in
            flag = 0
        else:
            t_in = t2_in
            flag = 1

        for i in range(min_len):
            out += self.sub_s(t1_in[i], t2_in[i])

        if len(t_in) > min_len:
            for i in range(min_len, len(t_in)):
                t = t_in[i]
                if flag == 1:
                    out += self.sub_s("_", t)
                else:
                    out += self.sub_s(t, "_")

        return out