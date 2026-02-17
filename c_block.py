from alphabet import Alphabet, ArithmeticOperations
from core_function import CoreFunction


class CBlock:

    def __init__(self):
        self.arith = ArithmeticOperations(Alphabet)
        self.core = CoreFunction()
        self.C = ["________________",
                  "ПРОЖЕКТОР_ЧЕПУХИ",
                  "КОЛЫХАТЬ_ПАРОДИЮ",
                  "КАРМАННЫЙ_АТАМАН"]

    def process(self, in_arr: list, out_size: str) -> str:
        r = len(in_arr)
        out = "input_error"
        flag = 1

        for i in range(r):
            if len(in_arr[i]) == 16:
                self.C[i] = self.arith.add_txt(self.C[i], in_arr[i])
            else:
                flag = 0

        if flag == 1:
            self.C[1] = self.arith.add_txt(self.C[1], in_arr[0])
            tmp1 = self.core.core_caesar(self.C[0], self.C[2])
            tmp2 = self.core.core_caesar(self.C[3], self.C[1])
            tmp3 = self.core.confuse(tmp1, tmp2)
            out = self.core.core_caesar(tmp3, tmp1)
            h1 = int(out_size)
            out = self.core.compress(out, int(out_size))

        return out


class BlockMixer:

    def __init__(self):
        self.arith = ArithmeticOperations(Alphabet)
        self.core = CoreFunction()
        self.c_block = CBlock()

    def macro_compression(self, in_str: str, state: str) -> list:
        a = self.arith.add_txt(in_str[0:16], state[0:16])
        b = self.arith.add_txt(in_str[16:32], state[16:32])
        c = self.arith.add_txt(in_str[32:48], state[32:48])
        d = self.arith.add_txt(in_str[48:64], state[48:64])
        e = state[64:80]

        con = "ААААЯЯЯЯААЯЯААЯЯ"

        for i in range(12):
            e = self.arith.add_txt(e, self.c_block.process([a, b, c, d], "16"))
            tmp = self.core.blocks_mix(c, d)
            con = self.arith.add_txt(con, "ААААЯЯЯЯААЯЯААЯЯ")
            c = tmp[0]
            d = tmp[1]
            b = self.core.block_mask(b, con)
            a, b, c, d, e = b, c, d, e, a

        return [a, b, c, d, e]