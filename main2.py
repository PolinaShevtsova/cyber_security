# from alphabet import Alphabet
# from core_function import CoreFunction
# from c_block import CBlock, BlockMixer
# from hash_function import MerkleDamgardHash
# from main1 import sub_txt
#
# if __name__ == "__main__":
#     in1 = "ХОРОШО_БЫТЬ_ВАМИ"
#     in2 = "КЬЕРКЕГОР_ПРОПАЛ"
#     fun = CoreFunction()
#     print(fun.core_caesar(in1, in2))
#     print(fun.core_caesar(in2, in1))
#
#     print("===" * 15)
#
#     in_str = "ХОРОШО_БЫТЬ_ВАМИ"
#     in1 = "КЬЕРКЕГОР_ПРОПАЛ"
#     in2 = "ХОРОШО_ПРОБРОСИЛ"
#     print(fun.confuse(in_str, in1))
#     print(fun.confuse(in_str, in2))
#     print(fun.confuse(in_str, in_str))
#
#     print("===" * 15)
#
#     in1 = ["ХОРОШО_БЫТЬ_ВАМИ"]
#     in2 = ["ХОРОШО_БЫТЬ_ВАМИ", "________________", "________________", "________________"]
#     in3 = ["ХОРОШО_БЫТЬ_ВАМИ", "________А_______"]
#     in4 = ["ХОРОШО_БЫТЬ_ВАМИ", "___А____________"]
#     in5 = ["ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
#     in6 = ["ЧЕРНЫЙ_АББАТ_ПОЛ", "ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
#     c_block = CBlock()
#     print(c_block.process(in1, "16"))
#     c_block = CBlock()
#     print(c_block.process(in2, "16"))
#     c_block = CBlock()
#     print(c_block.process(in3, "16"))
#     c_block = CBlock()
#     print(c_block.process(in1, "8"))
#     c_block = CBlock()
#     print(c_block.process(in2, "8"))
#     c_block = CBlock()
#     print(c_block.process(in3, "8"))
#
#     print("===" * 15)
#     c_block = CBlock()
#     print(c_block.process(in4, "16"))
#     c_block = CBlock()
#     print(c_block.process(in4, "8"))
#     c_block = CBlock()
#     print(c_block.process(in4, "4"))
#     c_block = CBlock()
#     print(c_block.process(in5, "16"))
#     c_block = CBlock()
#     print(c_block.process(in5, "8"))
#     c_block = CBlock()
#     print(c_block.process(in5, "4"))
#
#     print("===" * 15)
#     in6 = ["______А_________", "________________", "________________", "________________"]
#     in7 = ["________________", "________________", "________________", "________________"]
#     in8 = ["_____А__________", "___________А____", "_А______________", "____________А___"]
#     c_block = CBlock()
#     A = c_block.process(in6, "16")
#     print(A)
#     c_block = CBlock()
#     print(c_block.process(in6, "8"))
#     c_block = CBlock()
#     print(c_block.process(in6, "4"))
#     c_block = CBlock()
#     B = c_block.process(in7, "16")
#     print(B)
#     c_block = CBlock()
#     print(c_block.process(in7, "8"))
#     c_block = CBlock()
#     print(c_block.process(in7, "4"))
#     C = c_block.process(in8, "16")
#     print(C)
#     c_block = CBlock()
#     print(c_block.process(in8, "8"))
#     c_block = CBlock()
#     print(c_block.process(in8, "4"))
#     print("===" * 15)
#     print(sub_txt(A, C))
#     print(sub_txt(A, B))
#     print(sub_txt(B, C))
#
#     print("===" * 15)
#
#     print(Alphabet.reverse_str("ПРОАОАРАРА"))
#
#     in2 = "КЬЕРКЕГОР_ПРОПАЛ"
#     in1 = "ХОРОШО_БЫТЬ_ВАМИ"
#     block = CoreFunction()
#     print(block.blocks_mix(in1, in2))
#     block = CoreFunction()
#     print(block.blocks_mix(in2, in1))
#
#     print("===" * 15)
#
#     s1 = "КЬЕРКЕГОР_ПРОПАЛ"
#     s2 = "ХОРОШО_БЫТЬ_ВАМИ"
#     ins = "__________" * 8
#     func = MerkleDamgardHash()
#     macro = BlockMixer()
#     in1 = func.pad_md(s1 + s2)
#     print(in1)
#     print(len(in1))
#     print(len(ins))
#     print(macro.macro_compression(in1, ins))
#
#
#     print("===" * 15)
#
#     s1 = "КЬЕРКЕГОР_ПРОПАЛ"
#     s2 = "ХОРОШО_БЫТЬ_ВАМИ"
#     func = MerkleDamgardHash()
#     in1 = func.pad_md(s1 + s2)
#     print(in1)
#     macro = BlockMixer()
#     print(func.hash(in1))
#
#     print("===" * 15)
#
#     in2 = "_" * 64
#     print(in2)
#     print(func.hash(in2))
#
#     print("===" * 15)
#
#     in3 = "______________________А_________________________________________"
#     in4 = "________А_______________________________________________________"
#     print(in3)
#     print(in4)
#     print(func.hash(in3))
#     print(func.hash(in4))
#
#     print("===" * 15)
#     print(sub_txt(func.hash(in2), func.hash(in3)))
#     print(sub_txt(func.hash(in2), func.hash(in4)))
#     print("===" * 15)
#
#     in5 = "ПЕТЯ_ПИЛ_ПИВО_В_КАЛЬЯННОЙ_И_КУРИЛ_БАМБУК_ЧЕРЕЗ_АНАНАС_ТЧК_НАСТЯ_ПИЛА_ВОДУ_И_НЕ_ПОШЛА_В_КАЛЬЯННУЮ_ЗПТ_ЧТОБЫ_ВЫСПАТЬСЯ"
#     in6 = "ЗОЛОТЫЕ_ВРЕМЕНА_ПРОШЛИ_ТЧК_НАСТАЛА_ПОРА_ГРУЗИТЬ_АПЕЛЬСИНЫ_БОЧКАМИ_И_НЕ_ОГЛЯДЫВАТЬСЯ_НАЗАД_ТЧК_КОГДАТО_СНОВА_МЫ_БУДЕМ_ТАМ_ГДЕ_НАС_ЖДУТ_ТЧК"
#     print(func.hash(in5))
#     print(func.hash(in6))
from block_converter import BlockConverter
from lfsr import LFSR, AS_LFSR
block1 = "АБВГ"
block2 = "_ЯЗЬ"
block3 = "ЯЯЯЯ"
block_converter = BlockConverter()
print(block_converter.block2num(block1))
print(block_converter.block2num(block2))
print(block_converter.block2num(block3))
print(block_converter.num2block(34916))
print(block_converter.num2block(32028))
print(block_converter.num2block(1048575))

print("===" * 15)
bin1 = block_converter.dec2bin(34916)
bin2 = block_converter.dec2bin(32028)
bin3 = block_converter.dec2bin(1048575)
print(bin1, bin2, bin3)
print(block_converter.bin2dec(bin1),
      block_converter.bin2dec(bin2),
      block_converter.bin2dec(bin3))
print("===" * 15)
as_lfsr = AS_LFSR()
in1 = "ХОРОШО_БЫТЬ_ВАМИ"
in2 = "________________"
in4 = "___А____________"
in3 = "ХОРОШО_ВЫТЬ_ВАМИ"
print(as_lfsr.initialize_pring(in1))
print(as_lfsr.initialize_pring(in2))
print(as_lfsr.initialize_pring(in3))
print(as_lfsr.initialize_pring(in4))

print("===" * 15)
print(block_converter.block2bin("____"))
print(block_converter.block2bin("___А"))
print(block_converter.block2bin("__Б_"))
print(block_converter.block2bin("__БГ"))

print(block_converter.bin2block(block_converter.block2bin("____")))
print(block_converter.bin2block(block_converter.block2bin("___А")))
print(block_converter.bin2block(block_converter.block2bin("__Б_")))
print(block_converter.bin2block(block_converter.block2bin("__БГ")))

print("===" * 15)
lfsr = LFSR()
print(lfsr.push_reg(block_converter.block2bin("____"), 1))
print(lfsr.push_reg(block_converter.block2bin("___А"), 0))
print(lfsr.push_reg(block_converter.block2bin("__Б_"), 1))
print(lfsr.push_reg(block_converter.block2bin("__БГ"), 0))

print(block_converter.bin2block(lfsr.push_reg(block_converter.block2bin("____"), 1)))
print(block_converter.bin2block(lfsr.push_reg(block_converter.block2bin("___А"), 0)))
print(block_converter.bin2block(lfsr.push_reg(block_converter.block2bin("__Б_"), 1)))
print(block_converter.bin2block(lfsr.push_reg(block_converter.block2bin("__БГ"), 0)))

print("===" * 15)
taps1 = [20, 17]
taps2 = [19, 18,17, 4]
taps3 = [18, 11]
taps4 = [20, 19, 4, 3]
taps5 = [19, 18, 17, 13]
taps = [18, 17, 16, 13]

t1 = block_converter.taps2bin(taps1)
t2 = block_converter.taps2bin(taps2)
t3 = block_converter.taps2bin(taps3)
t4 = block_converter.taps2bin(taps4)
t5 = block_converter.taps2bin(taps5)
t6 = block_converter.taps2bin(taps)
print(t1, t2, t3, t4, t5, t6)

print("===" * 15)
s = [None] * 10
s[1] = [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
s[2] = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1]
s[3] = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
s[4] = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]
s[5] = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1]
s[6] = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
s[7] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
s[8] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0]
s[9] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
seed = block_converter.block2bin("КУБА")
print(seed)
t1 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s[0] = lfsr.LFSR_push(seed, t1)
tst = [None] * 20
tst[0] = block_converter.bin2block(s[0])
print(tst[0])

s[0] = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]

for i in range(1, 10):
      s[i] = lfsr.LFSR_push(s[i - 1], t1)
      print(s[i])

print("===" * 15)
seed = block_converter.block2bin("ОРИМ")
print(seed)

t1 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t2 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
tmp1 = lfsr.LFSR_next(seed, t1)
tmp2 = lfsr.LFSR_next(seed, t2)

st1 = [0] * 20
st2 = [0] * 20
seq1 = [0] * 20
seq2 = [0] * 20
st1[0] = tmp1[1]
st2[0] = tmp2[1]
seq1[0] = tmp1[0]
seq2[0] = tmp2[0]
print(block_converter.bin2block(st1[0]), block_converter.bin2block(st2[0]))
print(block_converter.bin2block(seq1[0]), block_converter.bin2block(seq2[0]))

for i in range(1, 10):
      seq1[i] = lfsr.LFSR_next(seq1[i - 1], t1)[1]
      seq2[i] = lfsr.LFSR_next(seq2[i - 1], t2)[1]
      print(block_converter.bin2block(seq1[i]), block_converter.bin2block(seq2[i]))

print("===" * 15)
seed1 = "ЛЕРА"
seed2 = "КЛОН"
seed3 = "КОНЯ"

s1 = block_converter.block2bin(seed1)
s2 = block_converter.block2bin(seed2)
s3 = block_converter.block2bin(seed3)
print(s1, s2, s3)
t1 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t2 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
t3 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

t_set = [t1, t2, t3]
s_set = [s1, s2, s3]
as_lfsr = AS_LFSR()
out1 = as_lfsr.AS_LFSR_push(s_set, t_set)
print(out1)
out2 = as_lfsr.AS_LFSR_push(out1[1], t_set)
print(out2)
out3 = as_lfsr.AS_LFSR_push(out2[1], t_set)
print(out3)

print("===" * 15)
print(as_lfsr.seed2bins(["ЛЕРА", "КЛОН", "КОНЯ"]))
print("===" * 15)

seed1 = "ЛЕРА"
seed2 = "КЛОН"
seed3 = "КОНЯ"

s1 = block_converter.block2bin(seed1)
s2 = block_converter.block2bin(seed2)
s3 = block_converter.block2bin(seed3)
print(s1, s2, s3)
t1 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t2 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
t3 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

t_set = [t1, t2, t3]
s_set = [s1, s2, s3]
res = [0] * 20
res[0] = as_lfsr.AS_LFSR_next(s_set, t_set)
print(block_converter.bin2block(res[0][0]))
for i in range(1, 10):
      res[i] = as_lfsr.AS_LFSR_next(res[i - 1][1], t_set)
      print(block_converter.bin2block(res[i][0]))

print("===" * 15)
set1 = [0] * 3
set2 = [0] * 3
set3 = [0] * 3
set4 = [0] * 3
set1[0] = block_converter.taps2bin([19, 18])
set1[1] = block_converter.taps2bin([18, 7])
set1[2] = block_converter.taps2bin([17, 3])

set2[0] = block_converter.taps2bin([19, 18])
set2[1] = block_converter.taps2bin([18, 7])
set2[2] = block_converter.taps2bin([16, 14, 13, 11])

set3[0] = block_converter.taps2bin([19, 18])
set3[1] = block_converter.taps2bin([18, 7])
set3[2] = block_converter.taps2bin([15, 13, 12, 10])

set4[0] = block_converter.taps2bin([19, 18])
set4[1] = block_converter.taps2bin([18, 7])
set4[2] = block_converter.taps2bin([14, 5, 3, 1])
SET = [set1, set2, set3, set4]

seed = "АБВГДЕЖЗИЙКЛМНОП"
out = [0] * 10
intern = [0] * 10
out[0], intern[0] = as_lfsr.C_AS_LFSR_next("up", -1, seed, SET)
print (out[0], intern[0])

print("===" * 15)
for i in range(1, 9):
      out[i], intern[i] = as_lfsr.C_AS_LFSR_next("down", intern[i - 1], -1, SET)
print(out)

