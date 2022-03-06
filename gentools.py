from collections import Counter


def freqAnal(text, interval=1, offset=0, letterfreq=True, doub=False, trip=False, top=5, feedback=True, note=""):
    ans = []
    if letterfreq:
        print("Letter Frequencies:", note) if feedback else None
        tmp = list(Counter(text[offset::interval]).items())
        tmp.sort(key=lambda x: x[1], reverse=True)
        #TODO: add percentage values to tmp
        print(tmp) if feedback else None
        ans += tmp
    return ans


def binStrManip(string, option=0, xorkey="A", transkey="0", stegorien=0):
    # for reference: https://wiki.python.org/moin/BitwiseOperators
    if option == 0:  # straight grouping into 8, then conversion into ASCII
        tmp = string.replace("\n", "")
        tmp = [tmp[x:x + 8] for x in range(0, len(tmp), 8)]
        return ''.join(chr(int(x, base=2)) for x in tmp)
        # if(string.find("\n") == -1):
        #     tmp = [string[x:x+8] for x in range(0, len(string), 8)]
        #     return '',join(chr(int(x, base=2)) for x in string.split("\n"))
        # return ''.join(chr(int(x, base=2)) for x in string.split("\n"))
    if option == 1:  # XOR with a key
        tmp = [int(x, base=2) for x in string.split("\n")]
        tmp = list(zip(tmp, [ord(x) for x in xorkey]))
        return ''.join(chr(x ^ y) for (x, y) in tmp)
    if option == 2:  # transpositioning
        tmp = [[y for y in x] for x in string.split("\n")]
        tmp = list(map(list, zip(*tmp)))
        for indx in range(len(tmp)):
            val = -int(transkey[indx])
            tmp[indx] = tmp[indx][val:] + tmp[indx][:val]
        tmp = [''.join(x) for x in map(list, zip(*tmp))]
        return ''.join(chr(int(x, base=2)) for x in tmp)
    if option == 3:  # LSB steganography
        val = -1
        offset = 8
        tmp = [[x for x in y.split("\t")] for y in string.split("\n")]
        tmp = [[''.join(x[val:]) for x in y] for y in tmp]
        if stegorien == 0:
            tmp = [''.join(x) for x in tmp]
        else:
            tmp = [''.join(x) for x in zip(*tmp)]
        tmp = ''.join(x for x in tmp)
        tmp = [tmp[x:x + offset] for x in range(0, len(tmp), offset)]
        ans = "\n" + '  '.join(tmp)
        tmp = [int(x, base=2) for x in tmp]
        print(bin(ord(".")), bin(ord("J")))
        # print(chr(int("10001110", base=2)))
        ans += "\n   " + '       '.join(str(x) for x in tmp)
        ans += "\n   " + '         '.join(chr(x) for x in tmp)
        return ans
    if option == 4:  # messing around with the challenge hex problem
        tmp = string.split("\n")
        tmp = list(map(list, zip(*tmp)))
        tmp = [''.join(x) for x in tmp]
        # tmp = [tmp[x:x+8] for x in range(0, len(tmp), 8)]
        return ''.join(chr(int(x, base=2)) for x in tmp)


def bealeCiph(text, nums, sort=False):
    text = text.replace("\n", " ").replace("\t", " ").replace(".", " ")
    text = text.replace(",", " ").replace("-", " ").replace(";", " ")
    text = [x for x in text.split(" ") if x != ""]
    plaintxt = ""
    for each in nums:
        plaintxt += text[each - 1][0]
    if sort:
        return ''.join(sorted(plaintxt.upper()))
    else:
        return plaintxt.upper()
