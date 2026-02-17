from alphabet import Alphabet, ArithmeticOperations
from caesar_ciphers import PolyalphabeticCaesarCipher

class BlockCipher:
    BLOCK_SIZE = 4
    KEY_SIZE = 16

    def __init__(self, arith_ops=None):
        self.arith = arith_ops or ArithmeticOperations(Alphabet)
        self.poly_caesar = PolyalphabeticCaesarCipher(self.arith)

    def _validate_input(self, block: str, key: str) -> bool:
        return len(block) == self.BLOCK_SIZE and len(key) == self.KEY_SIZE


class SCaesarCipher(BlockCipher):

    def __init__(self, arith_ops=None):
        super().__init__(arith_ops)
        self.C = [1, -1, 1, 2, -2, 1, 1, 3, -1, 2]

    def _generate_key_tmp(self, key: str) -> str:
        key_ext = key + key
        key_tmp = "___"

        for i in range(8):
            start_pos = i * 2
            s_tmp = key_ext[start_pos:start_pos + 4]
            b_tmp = Alphabet.text2array(s_tmp)
            a_tmp = [0 for _ in range(4)]

            for k in range(4):
                x = (2 * i + k) % 10
                value = 64 + k + self.C[x] * b_tmp[k]
                a_tmp[k] = value % 32

            key_tmp = self.arith.add_txt(key_tmp, Alphabet.array2text(a_tmp))

        return key_tmp

    def encrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        key_tmp = self._generate_key_tmp(key)
        return self.poly_caesar.encrypt(block, key_tmp)

    def decrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        key_tmp = self._generate_key_tmp(key)
        return self.poly_caesar.decrypt(block, key_tmp)


class MergeBlockCipher(BlockCipher):

    def _generate_permutation(self, key: str) -> list:
        M = [0, 1, 2, 3]
        array = Alphabet.text2array(key)
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

        return M

    def encrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        M = self._generate_permutation(key)
        inp = Alphabet.text2array(block)

        for j in range(4):
            b = M[(j + 1) % 4]
            a = M[j % 4]
            inp[b] = (inp[b] + inp[a]) % 32

        return Alphabet.array2text(inp)

    def decrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        M = self._generate_permutation(key)
        inp = Alphabet.text2array(block)

        for j in range(3, -1, -1):
            b = M[(j + 1) % 4]
            a = M[j % 4]
            inp[b] = (32 - inp[a] + inp[b]) % 32

        return Alphabet.array2text(inp)


class SCaesarMergeCipher(BlockCipher):

    def __init__(self, arith_ops=None):
        super().__init__(arith_ops)
        self.s_caesar = SCaesarCipher(arith_ops)
        self.merge_cipher = MergeBlockCipher(arith_ops)

    def encrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        tmp = self.merge_cipher.encrypt(block, key)
        tmp = self.s_caesar.encrypt(tmp, key)
        return self.merge_cipher.encrypt(tmp, key)

    def decrypt(self, block: str, key: str) -> str:
        if not self._validate_input(block, key):
            return "input_error"

        tmp = self.merge_cipher.decrypt(block, key)
        tmp = self.s_caesar.decrypt(tmp, key)
        return self.merge_cipher.decrypt(tmp, key)