from block_ciphers import SCaesarMergeCipher
from block_converter import BlockConverter
from lfsr import AS_LFSR
from alphabet import ArithmeticOperations, Alphabet


class BlockOperations:

    def __init__(self):
        self.converter = BlockConverter()

    def subblocks_xor(self, blocka_in, blockb_in):

        decA = self.converter.block2num(blocka_in)
        decB = self.converter.block2num(blockb_in)

        binA = self.converter.dec2bin(decA)
        binB = self.converter.dec2bin(decB)

        binO = []

        for i in range(len(binA)):
            binO.append((binA[i] + binB[i]) % 2)

        decO = self.converter.bin2dec(binO)

        return self.converter.num2block(decO)

    def block_xor(self, blocka_in, blockb_in):

        nb = len(blocka_in) // 4
        out = ""

        for i in range(nb):

            tmpA = blocka_in[i * 4:(i + 1) * 4]
            tmpB = blockb_in[i * 4:(i + 1) * 4]

            out += self.subblocks_xor(tmpA, tmpB)

        return out

class KeyGenerator:

    def __init__(self):
        self.converter = BlockConverter()
        self.generator = AS_LFSR()

    def make_lfsr_set(self):

        out = []

        out.append(self.converter.taps2bin([20, 17]))
        out.append(self.converter.taps2bin([20, 19, 16, 14]))
        out.append(self.converter.taps2bin([20, 9, 5, 3]))

        return out

    def produce_round_keys(self, key_in, num_in, SET):
        out = []

        stream, state = self.generator.C_AS_LFSR_next("up", -1, key_in, SET)
        out.append(stream)
        if num_in > 1:
            for i in range(1, num_in):
                stream, state = self.generator.C_AS_LFSR_next("down", state, -1, SET)
                out.append(stream)

        return out

class SkitalaPermutation:

    def frw_P_skitala(self, block_in):

        import math

        q = math.floor(len(block_in) / 2)
        f = len(block_in) % 2

        tmpA = block_in[0:q + f]
        tmpB = block_in[q + f:q + f + q]

        out = ""

        for i in range(q + 1):

            if i % 2 == 0:
                out += tmpA[i:i + 1]
                out += tmpB[i:i + 1]
            else:
                out += tmpB[i:i + 1]
                out += tmpA[i:i + 1]

        if f == 1:
            out += tmpA[q + f:q + f + 1]

        return out

    def inv_P_skitala(self, block_in):

        import math

        q = math.floor(len(block_in) / 2)
        f = len(block_in) % 2

        tmpA = ""
        tmpB = ""

        for i in range(q):

            if i % 2 == 0:
                tmpA += block_in[2 * i:2 * i + 1]
                tmpB += block_in[2 * i + 1:2 * i + 2]
            else:
                tmpB += block_in[2 * i:2 * i + 1]
                tmpA += block_in[2 * i + 1:2 * i + 2]

        if f == 1:
            tmpA += block_in[2 * q:2 * q + 1]

        return tmpA + tmpB

class FeistelCipher:

    def __init__(self):
        self.perm = SkitalaPermutation()
        self.blocks = BlockOperations()
        self.arith = ArithmeticOperations(Alphabet)
        self.S_block = SCaesarMergeCipher()

    def frw_routine_Feistel(self, block_in, key_in):

        left = block_in[0:4]
        right = block_in[4:8]

        tmp = self.S_block.encrypt(right, key_in)

        left = self.arith.add_txt(tmp, left)

        return right + left

    def inv_routine_Feistel(self, block_in, key_in):

        l = len(block_in)

        left = block_in[0:l // 2]
        right = block_in[l // 2:l]

        tmp = self.S_block.encrypt(left, key_in)

        right = self.arith.sub_txt(right, tmp)

        return right + left

    def frw_inner_Feistel(self, block_in, key_in, r_in):

        tmp = self.perm.frw_P_skitala(block_in)

        for i in range(r_in):
            tmp = self.frw_routine_Feistel(tmp, key_in)

        return self.perm.frw_P_skitala(tmp)

    def inv_inner_Feistel(self, block_in, key_in, r_in):

        tmp = self.perm.inv_P_skitala(block_in)

        for i in range(r_in):
            tmp = self.inv_routine_Feistel(tmp, key_in)

        return self.perm.inv_P_skitala(tmp)

    def round_Feistel(self, block_in, key_in):

        left = block_in[0:8]
        right = block_in[8:16]

        tmp = self.frw_inner_Feistel(right, key_in, 3)

        left = self.blocks.block_xor(tmp, left)

        return right + left

    def swap_blocks(self, block_in):

        left = block_in[0:8]
        right = block_in[8:16]

        return right + left
