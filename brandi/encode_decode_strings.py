from inline import Here

def encode(longUrl: str) -> str:
    encodeMap = {}
    decodeMap = {}
    base = "http://tinyurl.com/"
    if longUrl not in encodeMap: 
        shortUrl = base + str(len(encodeMap) + 1)
        # inline test here
        Here().given(base, "http://tinyurl.com/").given(encodeMap, {1, 2}).check_eq(shortUrl, "http://tinyurl.com/3")
        encodeMap[longUrl] = shortUrl
        decodeMap[shortUrl] = longUrl
    return encodeMap[longUrl]

def decode(self, shortUrl: str) -> str:
    return self.decodeMap[shortUrl]
