import struct
import time

def lastbit(f):
    return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
    "Return k random bits using a relative drift of two clocks."
    # assume time.sleep() and time.clock() use different clocks
    # though it might work even if they use the same clock
    #XXX it does not produce "good" random bits, see below for details
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= lastbit(time.clock())
    return result

print(getrandbits(16))