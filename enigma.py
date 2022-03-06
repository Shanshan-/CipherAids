
class EnigmaMachine:

    def __init__(self, scramblers, reflector, swaps=[]):
        self.scramblers = []
        for each in scramblers:
            tmp = [[x for x in y] for y in each.split("\n")]
            self.scramblers.append(tmp)
        self.reflector = [[x for x in y] for y in reflector.split("\n")]
        self.printReflector = True
        self.offset = [0, 0, 0]
        self.io = [chr(x) for x in range(65, 91)]
        for i, o in swaps:
            inp = self.io.index(i)
            out = self.io.index(o)
            self.io[inp], self.io[out] = self.io[out], self.io[inp]

    def __str__(self):
        ans = "Input/output:\t\t"
        for each in self.io:
            ans += each
        ans += "\n"
        for x, scrambler in enumerate(self.scramblers):
            ans += "Scrambler " + str(x + 1) + " State:\t"
            for each in scrambler[0]:
                ans += each
            ans += "\n\t\t\t"
            for each in scrambler[1]:
                ans += each
            ans += "\n"
        ans = ans[:-1]
        if (not self.printReflector):
            return ans
        ans += "\nReflector State:\t"
        for each in self.reflector[0]:
            ans += each
        ans += "\n\t\t\t"
        for each in self.reflector[1]:
            ans += each
        return ans

    def rotScrambler(self, times=1, disk=0):
        for _ in range(times):
            tmp0 = self.scramblers[disk][0].pop(0)
            tmp1 = self.scramblers[disk][1].pop(0)
            self.scramblers[disk][0].append(tmp0)
            self.scramblers[disk][1].append(tmp1)
            # TODO: chang to using list slicing
        # TODO: handle when len(message) > 26
        self.offset[0] += times

    def setScramblers(self, positions):
        if (len(positions) != len(self.scramblers)):
            print("Incorrect number of positions; There are %d scramblers" % (len(self.scramblers)))
            return
        for x, val in enumerate(positions):
            self.rotScrambler(val, x)
        self.offset = positions

    def resetScramblers(self):
        for x, val in enumerate(self.offset):
            for _ in range(val):
                tmp0 = self.scramblers[x][0].pop()
                tmp1 = self.scramblers[x][1].pop()
                self.scramblers[x][0].insert(0, tmp0)
                self.scramblers[x][1].insert(0, tmp1)
        # TODO: this can be done faster than individually
        self.offset = [0, 0, 0]

    def decode(self, ciphertext):
        plaintxt = ""
        for letter in ciphertext:
            self.rotScrambler()
            curIndx = self.io.index(letter)
            for each in self.scramblers:
                curChr = each[0][curIndx]
                curIndx = each[1].index(curChr)
            curChr = self.reflector[0][curIndx]
            curIndx = self.reflector[1].index(curChr)
            for each in reversed(self.scramblers):
                curChr = each[1][curIndx]
                curIndx = each[0].index(curChr)
            # plaintxt += chr(curIndx + 65)
            plaintxt += self.io[curIndx]
        return plaintxt

