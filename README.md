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

7. main1.py
   Функциональный файл без классов
9. main2.py
    Тестовый файл для проверки внутренних функций
