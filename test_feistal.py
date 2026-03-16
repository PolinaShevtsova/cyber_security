from feistel import *
from alphabet import ArithmeticOperations
inA = "АГАТ"
inB = "ТАГА"
inA1 = "КОЛЕНЬКА"
inB1 = "МТВ_ТЛЕН"
inA2 = "ТОРТ_ХОЧЕТ_ГОРКУ"
inB2 = "МТВ_ВСЕ_ЕЩЕ_ТЛЕН"
operations = BlockOperations()
arith = ArithmeticOperations()
print(operations.subblocks_xor(inA, inB))
print(operations.block_xor(inA, inB))
print(arith.add_txt(inA, inB))
print(operations.block_xor(inA1, inB1))
print(arith.add_txt(inA1, inB1))
out = operations.block_xor(inA2, inB2)
print(out)
print(arith.add_txt(inA2, inB2))
print(operations.block_xor(out, inB2))
print(operations.block_xor(out, inA2))

print("=====" * 5)

generator  = KeyGenerator()
lfsr_set = generator.make_lfsr_set()
print(lfsr_set)

key = "ПОЛИМАТ_ТЕХНОБОГ"
print(generator.produce_round_keys(key, 6, lfsr_set))

print("=====" * 5)
skitala = SkitalaPermutation()
print(skitala.frw_P_skitala("ДЖИГУРДА"))
print(skitala.frw_P_skitala("ДЖИГУРДАЯ"))
print(skitala.frw_P_skitala("АЭРОСМИТ"))
print(skitala.frw_P_skitala("БАЭРОСМИТ"))
print(skitala.inv_P_skitala("ДУРЖИДАГ"))
print(skitala.inv_P_skitala("ДРДЖИЯАГУ"))
print(skitala.inv_P_skitala("АСМЭРИТО"))
print(skitala.inv_P_skitala("БСМАЭИТРО"))

print("=====" * 5)
feistal = FeistelCipher()
key = "ЗОЛОТУХА_ПИКЕТКА"
in1 = "ГОР_СВЕТ"
in2 = "ЕГОР_КОТ"
in3 = "АААААААА"
in4 = "ААААААА_"
out1 = feistal.frw_routine_Feistel(in1, key)
out2 = feistal.frw_routine_Feistel(in2, key)
print(out1, out2)
out3 = feistal.frw_routine_Feistel(in3, key)
out4 = feistal.frw_routine_Feistel(in4, key)
print(out3, out4)
lout1 = feistal.inv_routine_Feistel(out1, key)
lout2 = feistal.inv_routine_Feistel(out2, key)
print(lout1, lout2)
lout3 = feistal.inv_routine_Feistel(out3, key)
lout4 = feistal.inv_routine_Feistel(out4, key)
print(lout3, lout4)

print("=====" * 5)
out1 = feistal.frw_inner_Feistel(in1, key, 2)
out2 = feistal.frw_inner_Feistel(in2, key, 2)
print(out1, out2)
out3 = feistal.frw_inner_Feistel(in3, key, 2)
out4 = feistal.frw_inner_Feistel(in4, key, 2)
print(out3, out4)
lout1 = feistal.inv_inner_Feistel(out1, key, 2)
lout2 = feistal.inv_inner_Feistel(out2, key, 2)
print(lout1, lout2)
lout3 = feistal.inv_inner_Feistel(out3, key, 2)
lout4 = feistal.inv_inner_Feistel(out4, key, 2)
print(lout3, lout4)

print("=====" * 5)
in1 = "КОРЫСТЬ_СЛОНА_ЭХ"
in2 = "НУЖНО_БОЛЬШЕ_ПЫЩ"
key = "МТВ_ВСЕ_ЕЩЕ_ТЛЕН"
out1 = feistal.round_Feistel(in1, key)
out2 = feistal.round_Feistel(in2, key)
print(out1, out2)
tmp1 = feistal.swap_blocks(out1)
tmp2 = feistal.swap_blocks(out2)
print(tmp1, tmp2)
ltmp1 = feistal.round_Feistel(tmp1, key)
ltmp2 = feistal.round_Feistel(tmp2, key)
print(ltmp1, ltmp2)
lout1 = feistal.swap_blocks(ltmp1)
lout2 = feistal.swap_blocks(ltmp2)
print(lout1, lout2)

print("=====" * 5)

generator  = KeyGenerator()
lfsr_set = generator.make_lfsr_set()
print(lfsr_set)

key = "МТВ_ВСЕ_ЕЩЕ_ТЛЕН"
print(generator.produce_round_keys(key, 8, lfsr_set))
