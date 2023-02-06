def encode(longUrl: str) -> str:
    encodeMap = {}
    decodeMap = {}
    base = "http://tinyurl.com/"
    if longUrl not in encodeMap: 
        shortUrl = base + str(len(encodeMap) + 1)
        encodeMap[longUrl] = shortUrl
        decodeMap[shortUrl] = longUrl
    return encodeMap[longUrl]

def decode(self, shortUrl: str) -> str:
    return self.decodeMap[shortUrl]
