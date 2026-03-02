from alphabet import Alphabet, ArithmeticOperations
from c_block import CBlock
class BlockConverter:

    def __init__(self):
        self.arith = ArithmeticOperations(Alphabet)

    def block2num(self, block_in: str):
        if len(block_in) != 4:
            return "input_error"

        tmp = Alphabet.text2array(block_in)
        out = 0
        pos = 1

        for i in [3, 2, 1, 0]:
            out += pos * tmp[i]
            pos *= 32

        return out

    def num2block(self, num_in: int):
        rem = num_in
        tmp = [0] * 4

        for i in range(4):
            tmp[3 - i] = rem % 32
            rem //= 32

        return Alphabet.array2text(tmp)

    def dec2bin(self, num_in: int):
        rem = num_in
        out = [0] * 20

        for i in range(20):
            out[19 - i] = rem % 2
            rem //= 2

        return out

    def bin2dec(self, bin_in: list):
        out = 0
        for i in range(20):
            out = 2 * out + bin_in[i]
        return out

    def block2bin(self, block_in: str):
        return self.dec2bin(self.block2num(block_in))

    def bin2block(self, bin_in: list):
        return self.num2block(self.bin2dec(bin_in))


    def taps2bin(self, taps_in: list):
        taps = sorted(taps_in, reverse=True)
        last = taps[0]
        y = 20 - last
        out = [0] * 20
        j = 0
        if y > 0:
            for i in range(y):
                out[i] = 0
        for i in range(last):
            if last - i == taps[j]:
                out[y + i] = 1
                j += 1
            else:
                out[y + i] = 0
            if j > len(taps) - 1:
                break
        q = len(out)
        if q < last:
            for i in range(q, 20):
                out[i] = 0
        return out