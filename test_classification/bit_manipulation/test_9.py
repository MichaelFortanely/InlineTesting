from inline import Here

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def toggle_kth_bit(n, k):
    return n ^ (1 << (k - 1))

def main():
    num = 5
    print(bin(num)) # binary representation of num
    print("Number of set bits:", count_set_bits(num))
    # hardcode the inputs and outputs
    new_num_2 = toggle_kth_bit(num, 1)
    Here().given(num, 9).check_eq(new_num_2, 8)
    for i in range(10):
        new_num_2 = toggle_kth_bit(num, 1)
    print(bin(num)) # binary representation after toggling 2nd bit
    print("Number of set bits:", count_set_bits(num))

if __name__ == '__main__':
    main()
