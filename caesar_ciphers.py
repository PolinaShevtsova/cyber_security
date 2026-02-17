from alphabet import ArithmeticOperations, Alphabet


class BaseCaesarCipher:

    def __init__(self, arith_ops=None):
        self.arith = arith_ops or ArithmeticOperations(Alphabet)

    def encrypt(self, text: str, key: str) -> str:
        raise NotImplementedError

    def decrypt(self, text: str, key: str) -> str:
        raise NotImplementedError


class SimpleCaesarCipher(BaseCaesarCipher):

    def encrypt(self, text: str, key: str) -> str:
        out = ""
        key = key[0]

        for i in range(len(text)):
            tmp = text[i]
            out += self.arith.add_s(tmp, key)

        return out

    def decrypt(self, text: str, key: str) -> str:
        out = ""
        key = key[0]

        for i in range(len(text)):
            tmp = text[i]
            out += self.arith.sub_s(tmp, key)

        return out


class PolyalphabeticCaesarCipher(BaseCaesarCipher):

    def encrypt(self, text: str, key: str) -> str:
        out = ""
        t_k = "_"
        K = len(key)

        for i in range(len(text)):
            t_i = text[i]
            q = i % K
            t_k = self.arith.add_s(t_k, key[q]) if t_k else key[q]
            out += self.arith.add_s(t_i, t_k)

        return out

    def decrypt(self, text: str, key: str) -> str:
        out = ""
        t_k = "_"
        K = len(key)

        for i in range(len(text)):
            t_i = text[i]
            q = i % K
            t_k = self.arith.add_s(t_k, key[q]) if t_k else key[q]
            out += self.arith.sub_s(t_i, t_k)

        return out