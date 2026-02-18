from alphabet import Alphabet
from core_function import CoreFunction
from c_block import CBlock, BlockMixer
from hash_function import MerkleDamgardHash
from main1 import sub_txt

if __name__ == "__main__":
    in1 = "ХОРОШО_БЫТЬ_ВАМИ"
    in2 = "КЬЕРКЕГОР_ПРОПАЛ"
    fun = CoreFunction()
    print(fun.core_caesar(in1, in2))
    print(fun.core_caesar(in2, in1))

    print("===" * 15)

    in_str = "ХОРОШО_БЫТЬ_ВАМИ"
    in1 = "КЬЕРКЕГОР_ПРОПАЛ"
    in2 = "ХОРОШО_ПРОБРОСИЛ"
    print(fun.confuse(in_str, in1))
    print(fun.confuse(in_str, in2))
    print(fun.confuse(in_str, in_str))

    print("===" * 15)

    in1 = ["ХОРОШО_БЫТЬ_ВАМИ"]
    in2 = ["ХОРОШО_БЫТЬ_ВАМИ", "________________", "________________", "________________"]
    in3 = ["ХОРОШО_БЫТЬ_ВАМИ", "________А_______"]
    in4 = ["ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
    in5 = ["ЧЕРНЫЙ_АББАТ_ПОЛ", "ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
    c_block = CBlock()
    print(c_block.process(in1, "16"))
    c_block = CBlock()
    print(c_block.process(in2, "16"))
    c_block = CBlock()
    print(c_block.process(in3, "16"))
    c_block = CBlock()
    print(c_block.process(in1, "8"))
    c_block = CBlock()
    print(c_block.process(in2, "8"))
    c_block = CBlock()
    print(c_block.process(in3, "8"))

    print("===" * 15)
    c_block = CBlock()
    print(c_block.process(in4, "16"))
    c_block = CBlock()
    print(c_block.process(in4, "8"))
    c_block = CBlock()
    print(c_block.process(in4, "4"))
    c_block = CBlock()
    print(c_block.process(in5, "16"))
    c_block = CBlock()
    print(c_block.process(in5, "8"))
    c_block = CBlock()
    print(c_block.process(in5, "4"))

    print("===" * 15)
    in6 = ["______А_________", "________________", "________________", "________________"]
    in7 = ["________________", "________________", "________________", "________________"]
    in8 = ["_____А__________", "___________А____", "_А______________", "____________А___"]
    c_block = CBlock()
    A = c_block.process(in6, "16")
    print(A)
    c_block = CBlock()
    print(c_block.process(in6, "8"))
    c_block = CBlock()
    print(c_block.process(in6, "4"))
    c_block = CBlock()
    B = c_block.process(in7, "16")
    print(B)
    c_block = CBlock()
    print(c_block.process(in7, "8"))
    c_block = CBlock()
    print(c_block.process(in7, "4"))
    C = c_block.process(in8, "16")
    print(C)
    c_block = CBlock()
    print(c_block.process(in8, "8"))
    c_block = CBlock()
    print(c_block.process(in8, "4"))
    print("===" * 15)
    print(sub_txt(A, C))
    print(sub_txt(A, B))
    print(sub_txt(B, C))

    print("===" * 15)

    print(Alphabet.reverse_str("ПРОАОАРАРА"))

    in2 = "КЬЕРКЕГОР_ПРОПАЛ"
    in1 = "ХОРОШО_БЫТЬ_ВАМИ"
    block = CoreFunction()
    print(block.blocks_mix(in1, in2))
    block = CoreFunction()
    print(block.blocks_mix(in2, in1))

    print("===" * 15)

    s1 = "КЬЕРКЕГОР_ПРОПАЛ"
    s2 = "ХОРОШО_БЫТЬ_ВАМИ"
    ins = "__________" * 8
    func = MerkleDamgardHash()
    macro = BlockMixer()
    in1 = func.pad_md(s1 + s2)
    print(in1)
    print(len(in1))
    print(len(ins))
    print(macro.macro_compression(in1, ins))


    print("===" * 15)

    s1 = "КЬЕРКЕГОР_ПРОПАЛ"
    s2 = "ХОРОШО_БЫТЬ_ВАМИ"
    func = MerkleDamgardHash()
    in1 = func.pad_md(s1 + s2)
    print(in1)
    macro = BlockMixer()
    print(func.hash(in1))

    print("===" * 15)

    in2 = "_" * 64
    print(in2)
    print(func.hash(in2))

    print("===" * 15)

    in3 = "______________________А_________________________________________"
    in4 = "________А_______________________________________________________"
    print(in3)
    print(in4)
    print(func.hash(in3))
    print(func.hash(in4))

    print("===" * 15)
    print(sub_txt(func.hash(in2), func.hash(in3)))
    print(sub_txt(func.hash(in2), func.hash(in4)))
    print("===" * 15)

    in5 = "ПЕТЯ_ПИЛ_ПИВО_В_КАЛЬЯННОЙ_И_КУРИЛ_БАМБУК_ЧЕРЕЗ_АНАНАС_ТЧК_НАСТЯ_ПИЛА_ВОДУ_И_НЕ_ПОШЛА_В_КАЛЬЯННУЮ_ЗПТ_ЧТОБЫ_ВЫСПАТЬСЯ"
    in6 = "ЗОЛОТЫЕ_ВРЕМЕНА_ПРОШЛИ_ТЧК_НАСТАЛА_ПОРА_ГРУЗИТЬ_АПЕЛЬСИНЫ_БОЧКАМИ_И_НЕ_ОГЛЯДЫВАТЬСЯ_НАЗАД_ТЧК_КОГДАТО_СНОВА_МЫ_БУДЕМ_ТАМ_ГДЕ_НАС_ЖДУТ_ТЧК"
    print(func.hash(in5))
    print(func.hash(in6))