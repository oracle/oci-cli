# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

"""
This is an implementation of the MD5 hash function, as specified by
RFC 1321, in pure Python.

This code is a modified version of
https://github.com/doegox/python-cryptoplus/blob/master/src/CryptoPlus/Hash/pymd5.py
by Dinu C. Gherman.  It supports python 2 and 3.

pymd5 has these methods:
 - update(arg): Update the md5 object with the string arg. Repeated calls
                are equivalent to a single call with the concatenation of all
                the arguments.
 - digest():    Return the digest of the strings passed to the update() method
                so far. This may contain non-ASCII characters, including
                NUL bytes.
 - hexdigest(): Like digest() except the digest is returned as a string of
                double length, containing only hexadecimal digits.

For example, to obtain the hexdigest of 'Hello World':
    >>> import pymd5
    >>> m = pymd5.md5()
    >>> m.update(b"Hello World")
    >>> m.hexdigest()
More condensed:
    >>> pymd5.md5(b"Hello World").hexdigest()
Shoud give the same result as:
    >>> import hashlib
    >>> hashlib.md5(b"Hello World").hexdigest()

"""
import struct
import copy
import sys

__metaclass__ = type   # or genrpy won't work

hex_constant_strings = [
    '0xD76AA478L', '0xE8C7B756L', '0x242070DBL', '0xC1BDCEEEL',
    '0xF57C0FAFL', '0x4787C62AL', '0xA8304613L', '0xFD469501L',
    '0x698098D8L', '0x8B44F7AFL', '0xFFFF5BB1L', '0x895CD7BEL',
    '0x6B901122L', '0xFD987193L', '0xA679438EL', '0x49B40821L',
    '0xF61E2562L', '0xC040B340L', '0x265E5A51L', '0xE9B6C7AAL',
    '0xD62F105DL', '0x02441453L', '0xD8A1E681L', '0xE7D3FBC8L',
    '0x21E1CDE6L', '0xC33707D6L', '0xF4D50D87L', '0x455A14EDL',
    '0xA9E3E905L', '0xFCEFA3F8L', '0x676F02D9L', '0x8D2A4C8AL',
    '0xFFFA3942L', '0x8771F681L', '0x6D9D6122L', '0xFDE5380CL',
    '0xA4BEEA44L', '0x4BDECFA9L', '0xF6BB4B60L', '0xBEBFBC70L',
    '0x289B7EC6L', '0xEAA127FAL', '0xD4EF3085L', '0x04881D05L',
    '0xD9D4D039L', '0xE6DB99E5L', '0x1FA27CF8L', '0xC4AC5665L',
    '0xF4292244L', '0x432AFF97L', '0xAB9423A7L', '0xFC93A039L',
    '0x655B59C3L', '0x8F0CCC92L', '0xFFEFF47DL', '0x85845DD1L',
    '0x6FA87E4FL', '0xFE2CE6E0L', '0xA3014314L', '0x4E0811A1L',
    '0xF7537E82L', '0xBD3AF235L', '0x2AD7D2BBL', '0xEB86D391L'
]

hex_constants = []
if sys.version_info[0] < 3:
    long_zero = eval('0L')
    ffffffffL = eval('0xffffffffL')
    x3FL = eval('0x3FL')
    constantA = eval('0x67452301L')
    constantB = eval('0xefcdab89L')
    constantC = eval('0x98badcfeL')
    constantD = eval('0x10325476L')
    for hs in hex_constant_strings:
        hex_constants.append(eval(hs))
else:
    long_zero = 0
    ffffffffL = 0xffffffff
    x3FL = 0x3F
    constantA = 0x67452301
    constantB = 0xefcdab89
    constantC = 0x98badcfe
    constantD = 0x10325476
    for hs in hex_constant_strings:
        hex_constants.append(eval(hs.rstrip("L")))

# ======================================================================
# Bit-Manipulation helpers
# ======================================================================


def _bytelist2long(list):
    "Transform a list of characters into a list of longs."

    imax = int(len(list) / 4)
    hl = [long_zero] * imax

    j = 0
    i = 0
    while i < imax:
        if sys.version_info[0] < 3:
            b0 = long(ord(list[j]))                 # noqa: F821
            b1 = (long(ord(list[j + 1]))) << 8      # noqa: F821
            b2 = (long(ord(list[j + 2]))) << 16     # noqa: F821
            b3 = (long(ord(list[j + 3]))) << 24     # noqa: F821
        else:
            b0 = list[j]
            if isinstance(b0, str):
                b0 = ord(list[j])
            if isinstance(list[j + 1], str):
                b1 = (ord(list[j + 1])) << 8
            else:
                b1 = list[j + 1] << 8
            if isinstance(list[j + 2], str):
                b2 = (ord(list[j + 2])) << 16
            else:
                b2 = list[j + 2] << 16
            if isinstance(list[j + 3], str):
                b3 = (ord(list[j + 3])) << 24
            else:
                b3 = list[j + 3] << 24
        hl[i] = b0 | b1 | b2 | b3
        i = i + 1
        j = j + 4

    return hl


def _rotateLeft(x, n):
    "Rotate x (32 bit) left n bits circularly."

    return (x << n) | (x >> (32 - n))


# ======================================================================
# The real MD5 meat...
#
#   Implemented after "Applied Cryptography", 2nd ed., 1996,
#   pp. 436-441 by Bruce Schneier.
# ======================================================================

# F, G, H and I are basic MD5 functions.

def F(x, y, z):
    return (x & y) | ((~x) & z)


def G(x, y, z):
    return (x & z) | (y & (~z))


def H(x, y, z):
    return x ^ y ^ z


def I(x, y, z):  # noqa: E743
    return y ^ (x | (~z))


def XX(func, a, b, c, d, x, s, ac):
    """Wrapper for call distribution to functions F, G, H and I.
    This replaces functions FF, GG, HH and II from "Appl. Crypto."
    Rotation is separate from addition to prevent recomputation
    (now summed-up in one function).
    """

    res = long_zero
    res = res + a + func(b, c, d)
    res = res + x
    res = res + ac
    res = res & ffffffffL
    res = _rotateLeft(res, s)
    res = res & ffffffffL
    res = res + b

    return res & ffffffffL


class MD5Type:
    "An implementation of the MD5 hash function in pure Python."

    def __init__(self):
        "Initialisation."

        # Initial message length in bits(!).
        self.length = long_zero
        self.count = [0, 0]

        # Initial empty message as a sequence of bytes (8 bit characters).
        self.input = []

        # Call a separate init function, that can be used repeatedly
        # to start from scratch on the same object.
        self.init()

    def init(self):
        "Initialize the message-digest and set all fields to zero."

        self.length = long_zero
        self.count = [0, 0]
        self.input = []

        # Load magic initialization constants.
        self.A = constantA
        self.B = constantB
        self.C = constantC
        self.D = constantD

    def _transform(self, inp):
        """Basic MD5 step transforming the digest based on the input.
        Note that if the Mysterious Constants are arranged backwards
        in little-endian order and decrypted with the DES they produce
        OCCULT MESSAGES!
        """
        a, b, c, d = A, B, C, D = self.A, self.B, self.C, self.D

        # Round 1.
        S11, S12, S13, S14 = 7, 12, 17, 22
        a = XX(F, a, b, c, d, inp[0], S11, hex_constants[0])  # 1
        d = XX(F, d, a, b, c, inp[1], S12, hex_constants[1])  # 2
        c = XX(F, c, d, a, b, inp[2], S13, hex_constants[2])  # 3
        b = XX(F, b, c, d, a, inp[3], S14, hex_constants[3])  # 4
        a = XX(F, a, b, c, d, inp[4], S11, hex_constants[4])  # 5
        d = XX(F, d, a, b, c, inp[5], S12, hex_constants[5])  # 6
        c = XX(F, c, d, a, b, inp[6], S13, hex_constants[6])  # 7
        b = XX(F, b, c, d, a, inp[7], S14, hex_constants[7])  # 8
        a = XX(F, a, b, c, d, inp[8], S11, hex_constants[8])  # 9
        d = XX(F, d, a, b, c, inp[9], S12, hex_constants[9])  # 10
        c = XX(F, c, d, a, b, inp[10], S13, hex_constants[10])  # 11
        b = XX(F, b, c, d, a, inp[11], S14, hex_constants[11])  # 12
        a = XX(F, a, b, c, d, inp[12], S11, hex_constants[12])  # 13
        d = XX(F, d, a, b, c, inp[13], S12, hex_constants[13])  # 14
        c = XX(F, c, d, a, b, inp[14], S13, hex_constants[14])  # 15
        b = XX(F, b, c, d, a, inp[15], S14, hex_constants[15])  # 16

        # Round 2.
        S21, S22, S23, S24 = 5, 9, 14, 20
        a = XX(G, a, b, c, d, inp[1], S21, hex_constants[16])  # 17
        d = XX(G, d, a, b, c, inp[6], S22, hex_constants[17])  # 18
        c = XX(G, c, d, a, b, inp[11], S23, hex_constants[18])  # 19
        b = XX(G, b, c, d, a, inp[0], S24, hex_constants[19])  # 20
        a = XX(G, a, b, c, d, inp[5], S21, hex_constants[20])  # 21
        d = XX(G, d, a, b, c, inp[10], S22, hex_constants[21])  # 22
        c = XX(G, c, d, a, b, inp[15], S23, hex_constants[22])  # 23
        b = XX(G, b, c, d, a, inp[4], S24, hex_constants[23])  # 24
        a = XX(G, a, b, c, d, inp[9], S21, hex_constants[24])  # 25
        d = XX(G, d, a, b, c, inp[14], S22, hex_constants[25])  # 26
        c = XX(G, c, d, a, b, inp[3], S23, hex_constants[26])  # 27
        b = XX(G, b, c, d, a, inp[8], S24, hex_constants[27])  # 28
        a = XX(G, a, b, c, d, inp[13], S21, hex_constants[28])  # 29
        d = XX(G, d, a, b, c, inp[2], S22, hex_constants[29])  # 30
        c = XX(G, c, d, a, b, inp[7], S23, hex_constants[30])  # 31
        b = XX(G, b, c, d, a, inp[12], S24, hex_constants[31])  # 32

        # Round 3.
        S31, S32, S33, S34 = 4, 11, 16, 23
        a = XX(H, a, b, c, d, inp[5], S31, hex_constants[32])  # 33
        d = XX(H, d, a, b, c, inp[8], S32, hex_constants[33])  # 34
        c = XX(H, c, d, a, b, inp[11], S33, hex_constants[34])  # 35
        b = XX(H, b, c, d, a, inp[14], S34, hex_constants[35])  # 36
        a = XX(H, a, b, c, d, inp[1], S31, hex_constants[36])  # 37
        d = XX(H, d, a, b, c, inp[4], S32, hex_constants[37])  # 38
        c = XX(H, c, d, a, b, inp[7], S33, hex_constants[38])  # 39
        b = XX(H, b, c, d, a, inp[10], S34, hex_constants[39])  # 40
        a = XX(H, a, b, c, d, inp[13], S31, hex_constants[40])  # 41
        d = XX(H, d, a, b, c, inp[0], S32, hex_constants[41])  # 42
        c = XX(H, c, d, a, b, inp[3], S33, hex_constants[42])  # 43
        b = XX(H, b, c, d, a, inp[6], S34, hex_constants[43])  # 44
        a = XX(H, a, b, c, d, inp[9], S31, hex_constants[44])  # 45
        d = XX(H, d, a, b, c, inp[12], S32, hex_constants[45])  # 46
        c = XX(H, c, d, a, b, inp[15], S33, hex_constants[46])  # 47
        b = XX(H, b, c, d, a, inp[2], S34, hex_constants[47])  # 48

        # Round 4.
        S41, S42, S43, S44 = 6, 10, 15, 21
        a = XX(I, a, b, c, d, inp[0], S41, hex_constants[48])  # 49
        d = XX(I, d, a, b, c, inp[7], S42, hex_constants[49])  # 50
        c = XX(I, c, d, a, b, inp[14], S43, hex_constants[50])  # 51
        b = XX(I, b, c, d, a, inp[5], S44, hex_constants[51])  # 52
        a = XX(I, a, b, c, d, inp[12], S41, hex_constants[52])  # 53
        d = XX(I, d, a, b, c, inp[3], S42, hex_constants[53])  # 54
        c = XX(I, c, d, a, b, inp[10], S43, hex_constants[54])  # 55
        b = XX(I, b, c, d, a, inp[1], S44, hex_constants[55])  # 56
        a = XX(I, a, b, c, d, inp[8], S41, hex_constants[56])  # 57
        d = XX(I, d, a, b, c, inp[15], S42, hex_constants[57])  # 58
        c = XX(I, c, d, a, b, inp[6], S43, hex_constants[58])  # 59
        b = XX(I, b, c, d, a, inp[13], S44, hex_constants[59])  # 60
        a = XX(I, a, b, c, d, inp[4], S41, hex_constants[60])  # 61
        d = XX(I, d, a, b, c, inp[11], S42, hex_constants[61])  # 62
        c = XX(I, c, d, a, b, inp[2], S43, hex_constants[62])  # 63
        b = XX(I, b, c, d, a, inp[9], S44, hex_constants[63])  # 64

        A = (A + a) & ffffffffL
        B = (B + b) & ffffffffL
        C = (C + c) & ffffffffL
        D = (D + d) & ffffffffL

        self.A, self.B, self.C, self.D = A, B, C, D

    # Down from here all methods follow the Python Standard Library
    # API of the md5 module.
    def update(self, inBuf):
        """Add to the current message.
        Update the md5 object with the string arg. Repeated calls
        are equivalent to a single call with the concatenation of all
        the arguments, i.e. m.update(a); m.update(b) is equivalent
        to m.update(a+b).
        The hash is immediately calculated for all full blocks. The final
        calculation is made in digest(). This allows us to keep an
        intermediate value for the hash, so that we only need to make
        minimal recalculation if we call update() to add moredata to
        the hashed string.
        """

        if sys.version_info[0] < 3:
            leninBuf = long(len(inBuf))     # noqa: F821
        else:
            leninBuf = len(inBuf)

        # Compute number of bytes mod 64.
        index = (self.count[0] >> 3) & x3FL

        # Update number of bits.
        self.count[0] = self.count[0] + (leninBuf << 3)
        if self.count[0] < (leninBuf << 3):
            self.count[1] = self.count[1] + 1
        self.count[1] = self.count[1] + (leninBuf >> 29)

        partLen = 64 - index

        if leninBuf >= partLen:
            self.input[index:] = list(inBuf[:partLen])
            self._transform(_bytelist2long(self.input))
            i = partLen
            while i + 63 < leninBuf:
                self._transform(_bytelist2long(list(inBuf[i:i + 64])))
                i = i + 64
            else:
                self.input = list(inBuf[i:leninBuf])
        else:
            i = 0
            self.input = self.input + list(inBuf)

    def digest(self):
        """Terminate the message-digest computation and return digest.
        Return the digest of the strings passed to the update()
        method so far. This is a 16-byte string which may contain
        non-ASCII characters, including null bytes.
        """

        A = self.A
        B = self.B
        C = self.C
        D = self.D
        input = [] + self.input
        count = [] + self.count

        index = (self.count[0] >> 3) & x3FL

        if index < 56:
            padLen = 56 - index
        else:
            padLen = 120 - index

        padding = ['\200'] + ['\000'] * 63
        self.update(padding[:padLen])

        # Append length (before padding).
        bits = _bytelist2long(self.input[:56]) + count

        self._transform(bits)

        # Store state in digest.
        digest = struct.pack("<IIII", self.A, self.B, self.C, self.D)

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.input = input
        self.count = count

        return digest

    def hexdigest(self):
        """Terminate and return digest in HEX form.
        Like digest() except the digest is returned as a string of
        length 32, containing only hexadecimal digits. This may be
        used to exchange the value safely in email or other non-
        binary environments.
        """
        if sys.version_info[0] < 3:
            return ''.join(['%02x' % ord(c) for c in self.digest()])
        else:
            digest = []
            for c in self.digest():
                if isinstance(c, str):
                    val = ord(c)
                else:
                    val = c
                digest.append(val)
            return ''.join(['%02x' % c for c in digest])

    def copy(self):
        """Return a clone object.
        Return a copy ('clone') of the md5 object. This can be used
        to efficiently compute the digests of strings that share
        a common initial substring.
        """
        if 0:   # set this to 1 to make the flow space crash
            return copy.deepcopy(self)
        clone = self.__class__()
        clone.length = self.length
        clone.count = [] + self.count[:]
        clone.input = [] + self.input
        clone.A = self.A
        clone.B = self.B
        clone.C = self.C
        clone.D = self.D
        return clone


# ======================================================================
# Mimic Python top-level functions from standard library API
# for consistency with the md5 module of the standard library.
# ======================================================================

digest_size = 16


def new(arg=None):
    """Return a new md5 crypto object.
    If arg is present, the method call update(arg) is made.
    """
    crypto = MD5Type()
    if arg:
        crypto.update(arg)

    return crypto


def md5(arg=None):
    """Same as new().
    For backward compatibility reasons, this is an alternative
    name for the new() function.
    """
    return new(arg)
