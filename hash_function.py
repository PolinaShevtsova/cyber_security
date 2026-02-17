from alphabet import Alphabet
from c_block import CBlock, BlockMixer


class MerkleDamgardHash:

    def __init__(self, block_size: int = 64, initial_state: str = None):
        self.block_size = block_size
        self.initial_state = initial_state or ("________________" * 5)
        self.c_block = CBlock()
        self.block_mixer = BlockMixer()

        # Константы для инициализации
        self.A = "________________"
        self.B = "________________"
        self.C = "________________"
        self.D = "________________"
        self.E = "________________"

    def pad_md(self, message: str) -> str:
        out = message
        l = len(message)
        rem = self.block_size - (l % self.block_size)

        if rem != self.block_size:
            for i in range(rem):
                out += "_"

        return out

    def hash(self, message: str) -> str:
        data = self.pad_md(message)
        a = self.A
        b = self.B
        c = self.C
        d = self.D
        e = self.E
        n = len(data) // self.block_size

        # Обработка блоков
        for i in range(n):
            tmp = data[i * self.block_size::self.block_size]
            state = self.block_mixer.macro_compression(tmp, a + b + c + d + e)
            a, b, c, d, e = state

        p1 = self.c_block.process([a, e], "16")
        p2 = self.c_block.process([b, e], "16")
        p3 = self.c_block.process([c, e], "16")
        p4 = self.c_block.process([d, e], "16")

        return p1 + p2 + p3 + p4
