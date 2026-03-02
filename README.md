# cyber_security
Классы криптографической библиотеки
1. alphabet.py
Alphabet - преобразование символ-число (алфавит 32 символа)
ArithmeticOperations - сложение/вычитание строк по модулю 32

2. caesar_ciphers.py
BaseCaesarCipher - абстрактный базовый класс для шифров Цезаря
SimpleCaesarCipher - простой шифр Цезаря (один символ ключа)
PolyalphabeticCaesarCipher - полиалфавитный шифр Цезаря (ключ любой длины)

3. block_ciphers.py
BlockCipher - базовый класс для блочных шифров (размер блока 4, ключа 16)
SCaesarCipher - S-блок на основе шифра Цезаря с генерацией промежуточного ключа
MergeBlockCipher - блочный шифр с перестановкой на основе ключа
SCaesarMergeCipher - комбинированный шифр (S-Цезарь + слияние блоков)

4. core_function.py
CoreFunction - ядро односторонней функции: core_caesar(), confuse(), compress(), block_mask(), blocks_mix()

5. c_block.py
CBlock - компрессирующий блок с внутренним состоянием
BlockMixer - смешивание блоков для макро-сжатия

6. hash_function.py
MerkleDamgardHash - хеш-функция на архитектуре Меркла-Дамгора

7. 7. block_converter.py

BlockConverter — преобразование данных между форматами:
текстовый блок (4 символа)
число
20-битовый двоичный вектор
маска отводов LFSR
Методы:
block2num(), num2block()
dec2bin(), bin2dec()
block2bin(), bin2block()
taps2bin()

8. lfsr.py
LFSR — линейный регистр сдвига с обратной связью
Методы:
push_reg() — сдвиг регистра
LFSR_push() — один шаг LFSR
LFSR_next() — генерация 20 бит выходной последовательности

9. as_lfsr.py
AS_LFSR — асинхронный каскадный генератор на основе трёх LFSR
Методы:
initialize_pring() — инициализация состояний от seed
seed2bins() — перевод начальных блоков в бинарные регистры
AS_LFSR_push() — шаг трёх LFSR с управляющим выбором выхода
AS_LFSR_next() — генерация 20-битовой последовательности
C_AS_LFSR_next() — каскадная генерация текстового потока

10. main1.py
   Функциональный файл без классов
11. main2.py
    Тестовый файл для проверки внутренних функций
