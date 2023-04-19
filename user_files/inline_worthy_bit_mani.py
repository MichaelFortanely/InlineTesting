month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
