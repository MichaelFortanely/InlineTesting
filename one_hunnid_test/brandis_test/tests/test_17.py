from inline import Here

def convert(self, s: str, numRows: int) -> str:
    template = list(range(numRows)) + list(range(numRows - 2, 0, -1))
    # inline test here
    Here().given(numRows, 5).check_eq(template, [0, 1, 2, 3, 4, 3, 2, 1])
    result = [''] * numRows
    for i, char in enumerate(s):
        result[template[i % len(template)]] += char
    return ''.join(result)
