from inline import Here

def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        # inline test here
        Here().given(n, 0b1111).given(i, 1).check_eq(bit, 1)
        res += (bit << (31 - i))
    return res