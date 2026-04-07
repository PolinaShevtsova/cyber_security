"""
KDF - Key Derivation Function
"""
from alphabet import Alphabet, ArithmeticOperations
from block_converter import BlockConverter
from hash_function import MerkleDamgardHash


class KDF:
    """Генерация ключей из парольной фразы"""

    def __init__(self):
        self.hash_func = MerkleDamgardHash()

    def _num2sym(self, num: int) -> str:
        """Преобразование числа в символ"""
        alphabet = Alphabet.ALPHABET
        if num == 0:
            return "_"
        return alphabet[(num - 1) % len(alphabet)]

    def generate(self, mat_in: str, salt_in: str, con_in: list,
                 size_in: list, iter_in: int) -> list:

        tmp = mat_in + salt_in

        for i in range(iter_in + 1):
            ext = self.hash_func.hash(tmp)
            tmp = ext + tmp

        prk = tmp
        out = []

        for i in range(len(size_in)):
            q = (size_in[i] - (size_in[i] % 64)) // 64
            rem = i
            res = ""

            while rem > 0:
                h = rem % 32
                res = self._num2sym(h) + res
                rem = (rem - h) // 32

            if q > 0:
                hash_val = prk
                for j in range(q + 1):
                    tmp2 = hash_val + con_in[i] + prk
                    hash_val = self.hash_func.hash(tmp2)
                    res = hash_val + res
            else:
                tmp2 = prk + con_in[i] + prk
                res = self.hash_func.hash(tmp2)

            out.append(res[:size_in[i]])

        return out


class BinaryConverter:
    """Класс для бинарных преобразований"""

    ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_"

    @classmethod
    def is_sym(cls, s_in: str) -> int:
        return 1 if s_in in cls.ALPHABET else -1

    @classmethod
    def sym2bin(cls, s_in: str) -> int:
        return ord(s_in) - 48

    @classmethod
    def msg2bin(cls, msg_in: str) -> list:
        tmp = []
        i = 0
        M = len(msg_in)

        # Кодируем все символы, которые есть в алфавите, как 5-битные
        while i < M:
            ch = msg_in[i]
            if ch in cls.ALPHABET:
                c = Alphabet.sym2num(ch)
                for j in range(4, -1, -1):
                    tmp.append((c >> j) & 1)
                i += 1
            else:
                # Если символ не в алфавите, проверяем是否是 '0' или '1'
                if ch == '0' or ch == '1':
                    tmp.append(int(ch))
                    i += 1
                else:
                    # Любой другой символ пропускаем или кодируем как 5-битный
                    i += 1

        return tmp

    @classmethod
    def num2str(cls, num_in: int) -> str:
        if num_in == 0:
            return "_"
        return cls.ALPHABET[(num_in - 1) % len(cls.ALPHABET)]

    @classmethod
    def bin2msg(cls, bin_in: list) -> str:
        if not bin_in:
            return ""

        out = ""
        i = 0
        B = len(bin_in)

        # Декодируем, пока есть биты
        while i < B:
            # Пытаемся прочитать 5 бит как символ алфавита
            if i + 5 <= B:
                t = 0
                for _ in range(5):
                    t = (t << 1) | bin_in[i]
                    i += 1

                # Проверяем, является ли полученное число допустимым символом
                if 0 <= t <= 32:
                    out += Alphabet.num2sym(t)
                else:
                    # Если недопустимо, интерпретируем как бинарные символы
                    # Возвращаемся назад и читаем по 1 биту
                    i -= 5
                    break
            else:
                break

        # Оставшиеся биты читаем как бинарные символы (0 или 1)
        while i < B:
            out += str(bin_in[i])
            i += 1

        return out


class MessagePadder:
    """Класс для дополнения сообщений"""

    def __init__(self):
        self.converter = BinaryConverter()

    def _check_padding(self, binmsg_in: list) -> list:
        bins = binmsg_in
        M = len(bins)

        if M % 80 != 0:
            return [0, [0, 0]]

        blocks = M // 80

        # последние 20 бит
        tb = bins[M - 20:M]

        PL = tb[0:7]  # pad length (7 бит)
        NB = tb[7:17]  # num blocks (10 бит)
        ender = tb[17:20]  # последние 3 бита

        # проверка маркера конца
        if ender != [0, 0, 1]:
            return [0, [0, 0]]

        # декодируем числа
        padlength = 0
        for bit in PL:
            padlength = (padlength << 1) | bit

        numblocks = 0
        for bit in NB:
            numblocks = (numblocks << 1) | bit

        # проверки
        if numblocks != blocks or not (23 <= padlength < 103):
            return [0, [0, 0]]

        if padlength > M:
            return [0, [0, 0]]

        # проверка паддинга
        pad = bins[M - padlength:M - 20]

        if len(pad) == 0 or pad[0] != 1:
            return [0, [0, 0]]

        # все остальные должны быть 0
        for bit in pad[1:]:
            if bit != 0:
                return [0, [0, 0]]

        return [1, [numblocks, padlength]]

    def _produce_padding(self, rem_in: int, blocks_in: int) -> list:
        """Генерация дополнения"""
        if rem_in == 0:
            b = blocks_in + 1
            r = 80
        elif rem_in <= 57:
            r = 80 - rem_in
            b = blocks_in + 1
        else:
            b = blocks_in + 2
            r = 160 - rem_in

        pad = [0] * r
        pad[0] = 1

        rt = r
        for i in range(6, -1, -1):
            pad[r - 20 + i] = rt % 2
            rt = rt // 2

        for i in range(9, -1, -1):
            pad[r - 13 + i] = b % 2
            b = b // 2

        pad[r - 3] = 0
        pad[r - 2] = 0
        pad[r - 1] = 1

        return pad

    def pad_message(self, msg_in: str) -> str:
        """Дополнение сообщения"""
        bins = self.converter.msg2bin(msg_in)
        M = len(bins)
        blocks = M // 80
        remainder = M % 80

        if remainder == 0:
            f = self._check_padding(bins)[0]
        else:
            f = 1

        if f == 1:
            pad = self._produce_padding(remainder, blocks)
            bins.extend(pad)

        return self.converter.bin2msg(bins)

    def unpad_message(self, msg_in: str) -> str:
        """Удаление дополнения"""
        bins = self.converter.msg2bin(msg_in)
        T = self._check_padding(bins)
        M = len(bins)
        if T[0] == 1:
            pl = T[1][1]
            tmp = bins[:M - pl] if M - pl > 0 else []
            out = self.converter.bin2msg(tmp)
        else:
            out = msg_in

        return out


class PacketHandler:
    """Класс для обработки пакетов"""

    def __init__(self):
        self.converter = BinaryConverter()
        self.padder = MessagePadder()
        self.arith = ArithmeticOperations(Alphabet)

    def prepare_packet(self, data_in: list, iv_in: str, msg_in: str) -> list:
        data = data_in
        iv = self.arith.add_txt("________________", iv_in)
        msg = self.padder.pad_message(msg_in)
        L = len(self.converter.msg2bin(msg))
        a = ""
        for i in range(5):
            a = Alphabet.num2sym(L % 32) + a
            L = L // 32
        data.append(a)
        mac = ""
        return [data, iv, msg, mac]
    def validate_packet(self, packet_in: list) -> int:
        [data, iv, msg, mac] = packet_in
        f = 1
        t = data[0][0:1]
        s = data[0][1:2]
        ml = len(mac)
        if t != "В":
            f = 0
        elif ((s == "А") or (s == "Б")) and (ml != 16):
            f = 0
        elif (s == "_") and (ml != 0):
            f = 0
        return f

    def transmit(self, packet_in: list) -> list:
        [data, iv, msg, mac] = packet_in
        out = data[0] + data[1] + data[2] + data[3] + data[4]
        out = self.converter.msg2bin(out + iv + msg + mac)
        return out

    def receive(self, stream_in: list) -> list:
        p = self.converter.bin2msg(stream_in)
        M = len(p)
        type = p[0:2]
        sender = p[2:10]
        reciever = p[10:18]
        session = p[18:27]
        length = p[27:32]
        iv = p[32:48]
        L = 0
        for i in range(5):
            t = length[i:i + 1]
            l = Alphabet.sym2num(t)
            L = 32 * L + l
        L = L // 5
        message = p[48:48 + L]
        mac = p[48 + L:48 + L + M - (48 + L)]
        return [[type, sender, reciever, session, length], iv, message, mac]


class CFBCipher:
    """CFB режим шифрования"""

    def __init__(self):
        self.converter = BinaryConverter()
        self.arith = ArithmeticOperations(Alphabet)
        self.converter2 = BlockConverter()
        self.feistel = FeistelCipher()

    def _textxor(self, a_in: str, b_in: str) -> str:
        """XOR двух строк"""
        out = ""
        for i in range(4):
            a = a_in[i * 4:i * 4 + 4]
            b = b_in[i * 4:i * 4 + 4]
            A = self.converter2.dec2bin(self.converter2.block2num(a))
            B = self.converter2.dec2bin(self.converter2.block2num(b))
            C = [(A[j] + B[j]) % 2 for j in range(20)]
            c = self.converter2.bin2dec(C)
            out += self.converter2.num2block(c)
        return out

    def frw_cfb(self, msg_in: str, iv_in: str, key_in: str, mac_in: int) -> str:
        """Прямой CFB режим"""
        R = 6  # 8 - 2
        m = len(msg_in) // 16
        feedback = iv_in
        out = ""
        cont = "________________"

        for i in range(m):
            inp = msg_in[i * 16:(i + 1) * 16]
            cont = self._textxor(inp, cont)
            keystream = self.feistel.frw_feistel(feedback, key_in, R)
            feedback = self._textxor(inp, keystream)
            out += feedback

        keystream = self.feistel.frw_feistel(feedback, key_in, R)
        mac = self._textxor(cont, keystream)

        if mac_in == 1:
            out += mac
        elif mac_in == -1:
            out = mac

        return out

    def inv_cfb(self, msg_in: str, iv_in: str, key_in: str, mac_in: int) -> str:
        """Обратный CFB режим"""
        R = 6
        m = len(msg_in) // 16
        feedback = iv_in
        out = ""
        cont = "________________"

        for i in range(m - mac_in):
            inp = msg_in[i * 16:(i + 1) * 16]
            keystream = self.feistel.frw_feistel(feedback, key_in, R)
            feedback = inp
            text = self._textxor(inp, keystream)
            cont = self._textxor(cont, text)
            out += text

        if mac_in != 0:
            mac = msg_in[(m - 1) * 16:(m - 1) * 16 + 16]
            keystream = self.feistel.frw_feistel(feedback, key_in, R)
            text = self._textxor(mac, keystream)
            cont = self._textxor(cont, text)

            if mac_in == 1:
                out += cont
            else:
                out = cont

        return out


from feistel import KeyGenerator, FeistelCipher


class EAXCFB:
    """EAX-CFB режим"""

    def __init__(self):
        self.cfb = CFBCipher()
        self.packet_handler = PacketHandler()
        self.arith = ArithmeticOperations(Alphabet)
        self.generator = KeyGenerator()
        self.converter = BlockConverter()


    def eax_cfb_frw(self, packet_in: list, cmac_in: str, key_in: str,
                    sec_in: str, onlymac: int) -> list:
        """Прямой EAX-CFB"""
        assdata_in, iv_in, msg_in, tmp = packet_in
        tmp = assdata_in[0] + assdata_in[3] + assdata_in[4]
        civ = self.cfb.frw_cfb(sec_in + tmp, iv_in, key_in, -1)

        if onlymac == 1:
            tmp = self.cfb.frw_cfb(msg_in, civ, key_in, -1)
            mac = self.cfb._textxor(self.cfb._textxor(tmp, civ), cmac_in)
            msg = msg_in
        else:
            tmp = self.cfb.frw_cfb(msg_in, civ, key_in, 1)
            m = tmp[len(msg_in):len(msg_in) + 16]
            mac = self.cfb._textxor(self.cfb._textxor(m, civ), cmac_in)
            msg = tmp[0:len(msg_in)]

        return [assdata_in, iv_in, msg, mac]

    def eax_cfb_inv(self, packet_in: list, key_in: str,
                    sec_in: str, onlymac: int) -> list:
        """Обратный EAX-CFB"""
        ad_in, iv_in, msg_in, mac_in = packet_in
        tmp = ad_in[0] + ad_in[3] + ad_in[4]
        data = ad_in[0] + ad_in[1] + ad_in[2] + ad_in[3] + "_____"
        cmac = self.cfb.frw_cfb(data, sec_in, key_in, -1)
        civ = self.cfb.frw_cfb(sec_in + tmp, iv_in, key_in, -1)

        if onlymac == 1:
            tmp = self.cfb.frw_cfb(msg_in, civ, key_in, -1)
            mac = self.cfb._textxor(mac_in, self.cfb._textxor(self.cfb._textxor(tmp, civ), cmac))
            msg = msg_in
        else:
            cont = self.cfb._textxor(self.cfb._textxor(mac_in, civ), cmac)
            tmp = self.cfb.inv_cfb(msg_in + cont, civ, key_in, 1)
            m = tmp[len(msg_in):len(msg_in) + 16]
            mac = m
            msg = tmp[0:len(msg_in)]

        return [ad_in, iv_in, msg, mac]

    def eax_cfb(self, ass_data: list, msg_array: list, key_in: str,
                nonce: str, type_val: str) -> list:
        """Основная функция EAX-CFB"""
        mtype, sender, receiver, transmission = ass_data
        t1 = receiver + sender
        t2 = mtype + transmission + "_____"
        cad = self.arith.add_txt(t1, t2)
        iv0 = self.arith.add_txt(self.arith.add_txt(t1, t2), nonce)[:12]

        if receiver < sender:
            t3 = t1
        else:
            t3 = sender + receiver

        msg_counter = -1
        keyset = self.generator.produce_round_keys(key_in, 8, self.generator.make_lfsr_set())
        secret = self.cfb.frw_cfb(t3 + t2, key_in, keyset, -1)
        data = mtype + sender + receiver + transmission + "_____"
        data_mac = self.cfb.frw_cfb(data, secret, keyset, -1)

        out = []

        if type_val == "send":
            for i in range(len(msg_array)):
                msg_sec = mtype
                msg_counter += 1
                iv = iv0 + self.converter.num2block(msg_counter)
                tmp_packet = self.packet_handler.prepare_packet(
                    [msg_sec, sender, receiver, transmission], iv, msg_array[i]
                )

                if msg_sec == "В_":
                    out.append(self.packet_handler.transmit(tmp_packet))
                elif msg_sec == "ВА":
                    sec_packet = self.eax_cfb_frw(tmp_packet, data_mac, keyset, secret, 1)
                    out.append(self.packet_handler.transmit(sec_packet))
                elif msg_sec == "ВБ":
                    sec_packet = self.eax_cfb_frw(tmp_packet, data_mac, keyset, secret, 0)
                    out.append(self.packet_handler.transmit(sec_packet))

        elif type_val == "recieve":
            last = -1
            for i in range(len(msg_array)):
                tmp_packet = self.packet_handler.receive(msg_array[i])
                rdata = tmp_packet[0]
                current = self.converter.block2num(tmp_packet[1][12:16])

                if current > last:
                    if rdata[0] == "ВБ":
                        rec_packet = self.eax_cfb_inv(tmp_packet, keyset, secret, 0)
                        rec_packet[2] = self.packet_handler.padder.unpad_message(rec_packet[2])
                        if rec_packet[3] == "________________":
                            last = current
                            rec_packet[3] = "ОК"
                    elif (rdata[0] == "ВА") and (mtype != "ВБ"):
                        rec_packet = self.eax_cfb_inv(tmp_packet, keyset, secret, 1)
                        rec_packet[2] = self.packet_handler.padder.unpad_message(rec_packet[2])
                        if rec_packet[3] == "________________":
                            last = current
                            rec_packet[3] = "ОК"
                    elif (rdata[0] == "В_") and (mtype == "В_"):
                        rec_packet = tmp_packet
                        rec_packet[2] = self.packet_handler.padder.unpad_message(rec_packet[2])
                        if rec_packet[3] == "":
                            last = current
                            rec_packet[3] = "N/A"
                    else:
                        rec_packet = tmp_packet

                    out.append(rec_packet)

        return out