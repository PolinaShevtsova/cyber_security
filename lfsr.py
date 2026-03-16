from alphabet import ArithmeticOperations, Alphabet
from block_converter import BlockConverter
from  c_block import CBlock
class LFSR:

    def __init__(self):
        self.converter = BlockConverter()
        self.arith = ArithmeticOperations(Alphabet)

    def push_reg(self, bin_in: list, new_bit: int):
        out = bin_in[1:] + [new_bit]
        return out

    def LFSR_push(self, state_in: list, taps_in: list):
        tmp = 0
        n = min(len(state_in), len(taps_in))

        for i in range(n):
            tmp += state_in[i] * taps_in[i]

        new_bit = tmp % 2
        return self.push_reg(state_in, new_bit)

    def LFSR_next(self, state_in: list, taps_in: list):
        state = state_in
        stream = []

        for _ in range(20):
            state = self.LFSR_push(state, taps_in)
            stream.append(state[19])

        return [stream, state]


class AS_LFSR:

    def __init__(self):
        self.lfsr = LFSR()
        self.converter = BlockConverter()
        self.arith = ArithmeticOperations(Alphabet)

    def seed2bins(self, array_in: list):
        return [self.converter.block2bin(array_in[i]) for i in range(3)]

    def initialize_pring(self, seed_in: str):
        const = ["ПЕРВОЕ_АКТЕРСТВО", "ВТОРОЙ_ДАЛЬТОНИК",
                 "ТРЕТЬЯ_САДОВНИЦА", "ЧЕТВЕРТЫЙ_ГОБЛИН"]
        value = [None] * 4
        out = [None] * 4
        for i in range(4):
            value[i] = (CBlock().process([const[i], seed_in], "16"))
        secret = CBlock().process(value, "16")
        for i in range(4):
            tmp = value[i]
            TMP = ""
            for j in range(4):
                tmp = self.arith.add_txt(tmp, const[i])
                TMP = TMP + CBlock().process([tmp, secret], "4")
                tmp = self.arith.add_txt(tmp, TMP)
            out[i] = TMP[4:4 + 12]
        return out

    def AS_LFSR_push(self, state_in: list, taps_in: list):
        l0 = self.lfsr.LFSR_push(state_in[0], taps_in[0])
        l1 = self.lfsr.LFSR_push(state_in[1], taps_in[1])
        l2 = self.lfsr.LFSR_push(state_in[2], taps_in[2])

        if l0[19] == 0:
            stream = l1[19]
        else:
            stream = l2[19]

        return stream, [l0, l1, l2]

    def AS_LFSR_next(self, state_in: list, taps_in: list):
        state = state_in
        stream = []

        for _ in range(20):
            bit, state = self.AS_LFSR_push(state, taps_in)
            stream.append(bit)

        return stream, state

    def C_AS_LFSR_next(self, init_flag, state_in, seed_in, set_in):

        out = "something_wrong"
        stream = ""
        check = 0
        state = [None] * 4

        if init_flag == "up":
            INIT = self.initialize_pring(seed_in)

            for i in range(4):
                state[i] = self.seed2bins([
                    INIT[i][0:4],
                    INIT[i][4:8],
                    INIT[i][8:12]
                ])
            check = 1

        elif init_flag == "down":
            state = state_in
            check = 1

        if check:
            for j in range(4):
                for k in range(4):
                    T = self.AS_LFSR_next(state[k], set_in)
                    state[k] = T[1]

                    if k == 0:
                        tmp = T[0]
                    else:
                        for i in range(20):
                            tmp[i] = (T[0][i] + tmp[i]) % 2

                stream = stream + self.converter.bin2block(tmp)

            out = [stream, state]

        return out

    def init_generator(self, seed_in):

        INIT = self.initialize_pring(seed_in)

        state = [None] * 4

        for i in range(4):
            state[i] = self.seed2bins([
                INIT[i][0:4],
                INIT[i][4:8],
                INIT[i][8:12]
            ])

        return state

    def generate(self, state, set_in):

        stream = ""

        for j in range(4):

            for k in range(4):

                T = self.AS_LFSR_next(state[k], set_in)
                state[k] = T[1]

                if k == 0:
                    tmp = T[0]
                else:
                    for i in range(20):
                        tmp[i] = (T[0][i] + tmp[i]) % 2

            stream += self.converter.bin2block(tmp)

        return stream, state


