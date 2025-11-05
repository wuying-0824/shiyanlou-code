import sys

def Hours(minutes):
    if minutes < 0:
        raise ValueError("输入的分钟数应该是正数")
    else:
        x = int(minutes // 60)
        y = int(minutes % 60)
        print("{} H, {} M".format(x, y))
    return x, y

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
