import re

sysdir = "abcdefghijklmnopqrstuvwxyz"
m = re.match(r".+/([a-f0-9]{4}:[a-f0-9]{2}:[0|1][a-f0-9]\.[0-7])/", sysdir)


