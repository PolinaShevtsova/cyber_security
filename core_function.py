from alphabet import Alphabet, ArithmeticOperations

class CoreFunction:

    def __init__(self):
        self.arith = ArithmeticOperations(Alphabet)
        self.C1 = [1, 1, -1]
        self.C2 = [4, 3, 2, 1, -1, -2, -3, -4]

    def core_caesar(self, in_prime: str, in_aux: str) -> str:
        if len(in_prime) != 16 or len(in_aux) != 16:
            return "input_error"

        aux = Alphabet.text2array(in_aux)
        prime = Alphabet.text2array(in_prime)
        tmp = 0
        c1 = prime[2] % 3
        c2 = prime[10 + c1] % 8
        c3 = prime[c2 + 3] % 16
        arr = [0] * 16

        for i in range(32):
            q = (c1 + i) % 3
            j = (c2 + i) % 8
            p = (c3 + i) % 16
            l_val = i % 16
            tmp = (tmp + 64 + prime[p] + self.C1[q] * aux[l_val] + self.C2[j]) % 32
            arr[l_val] = tmp

        return Alphabet.array2text(arr)

    def confuse(self, in1: str, in2: str) -> str:
        arr1 = Alphabet.text2array(in1)
        arr2 = Alphabet.text2array(in2)

        for i in range(16):
            if arr1[i] > arr2[i]:
                arr1[i] = (arr1[i] + i) % 32
            else:
                arr1[i] = (arr2[i] + i) % 32

        return Alphabet.array2text(arr1)

    def compress(self, in_16: str, out_n: int) -> str:
        out = "input_error"
        if out_n != 16:
            a1 = in_16[0:0 + 4]
            a2 = in_16[4:4 + 4]
            a3 = in_16[8:8 + 4]
            a4 = in_16[12:12 + 4]

            if out_n == 8:
                a13 = a1 + a3
                a24 = a2 + a4
                out = self.arith.add_txt(a13, a24)

            if out_n == 4:
                a13 = self.arith.sub_txt(a1, a3)
                a24 = self.arith.sub_txt(a2, a4)
                out = self.arith.add_txt(a13, a24)

        else:
            out = in_16

        return out

    def block_mask(self, in_str: str, const: str) -> str:
        arr = Alphabet.text2array(in_str)
        con = Alphabet.text2array(const)
        out = [0] * 16

        for i in range(16):
            if arr[i] < (con[i] + i):
                out[i] = (64 - (con[i] - i)) % 32
            else:
                out[i] = (arr[i] + i) % 32

        return Alphabet.array2text(out)

    def blocks_mix(self, in1: str, in2: str) -> list:
        in1 = Alphabet.reverse_str(in1)
        return [
            self.arith.add_txt(in1, in2),
            self.arith.sub_txt(in1, in2)
        ]
