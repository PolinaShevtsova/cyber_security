from alphabet import Alphabet, ArithmeticOperations

class CoreFunction:

    def __init__(self):
        self.arith = ArithmeticOperations(Alphabet)
        self.C1 = [1, -1, 1, -1, 1, -1, 1]
        self.C2 = [1, -1, 1, -1, 1]

    def core_caesar(self, in_prime: str, in_aux: str) -> str:
        if len(in_prime) != 16 or len(in_aux) != 16:
            return "input_error"

        aux = Alphabet.text2array(in_aux)
        prime = Alphabet.text2array(in_prime)
        tmp = 0
        t1 = 0
        for i in range(16):
            t1 = t1 + aux[i]
        c1 = t1 % 7
        c2 = prime[2 * c1 + 1] % 5
        c3 = (prime[2 * c2] + prime[2 * c1]) % 16
        arr = [0] * 16

        for i in range(16):
            q = (c1 + i) % 7
            j = (c2 + i) % 5
            p = (c3 + i) % 16
            l_val = i % 16
            tmp = (tmp + 64 + prime[p] + self.C1[q] * aux[l_val] * self.C2[j]) % 32
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

        tmp = Alphabet.array2text(arr1)
        return self.arith.add_txt(self.arith.add_txt(tmp, in1), in2)

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

    def mixinputs(self, in_val: list) -> list:
        out1 = self.arith.add_txt(in_val[0], in_val[1])
        out2 = self.arith.sub_txt(in_val[0], in_val[1])
        out3 = self.arith.add_txt(out2, self.arith.add_txt(in_val[2], in_val[3]))
        out4 = self.arith.add_txt(out1, self.arith.sub_txt(in_val[2], in_val[3]))
        out = [out1, out2, out3, out4]
        return out