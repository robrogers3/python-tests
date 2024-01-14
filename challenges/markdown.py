class MarkDownEl:
    def __init__(self, identifier, openMatcher, opening, closingMatcher, closing = None, beginChomp = 0, endChomp = 0):
        self.identifier = identifier # P, BR
        self.openMatcher = openMatcher # def foo(i, ch, s)
        self.opening = opening
        self.closingMatcher = closingMatcher
        self.closing = closing
        self.beginChomp = beginChomp
        self.endChomp = endChomp

    def matchesOpening(self, i, ch, s):
        return self.openMatcher(i,ch, s)
    def matchesClosing(self, i,ch, s):
        if self.closingMatcher is None:
            return True
        return self.closingMatcher(i,ch,s)
    def chompsBeginning(self,ch):
        return self.beginChomp
    def chompsEnd(self,ch):
        return self.endChomp

def makeMarkDownEl(typeof):
    def startP(i,ch,s):
        if i > len(s) -2:
            return False
        if s[i] == "\n" and s[i+1] == "\n":
            return True
        return False

    def endP(i, ch, s):
        if i > len(s) - 2:
            return False
        if ch == "\n" and s[i+1] == "\n":
            return True
        return False

    def softBr(i,ch,s):
        if i == 0:
            return False
        if i == len(s) -1:
            return False
        if i > len(s) - 1:
            return False
        if s[i] == "\n" and s[i+1] != "\n":
            return True
        return False

    def startStrike(i,ch,s):
        if i + 1 > len(s) -1:
            return False
        if s[i] == '~' and s[i+1] == '~':
            return True
        return False

    def endStrike(i,ch,s):
        if i + 1 > len(s) -1:
            return False
        if ch == '~' and s[i+1] == '~':
            return True
        return False
    def startBlockQuote(i,ch,s):
        if i + 1 > len(s) -1:
            return False
        if ch == "\n" and s[i+1] == ">":
            return True
        return False

    def endBlockQuote(i,ch,s):
        if i + 1 > len(s) -1:
            return False
        if ch == "\n" and s[i+1] != ">":
            print('endblock', s[i:])
            return True
        return False

    if typeof == 'P':
        return MarkDownEl('P', startP, '<p>', endP, '</p>', 2,0)
    if typeof == 'BR':
        return MarkDownEl('BR', softBr, '<br>', None, '', 1,0)
    if typeof == 'STRIKE':
        return MarkDownEl('STRIKE', startStrike, '<del>', endStrike, '</del>', 2,2)
    if typeof == 'BLOCKQUOTE':
        return MarkDownEl('BLOCKQUOTE', startBlockQuote, '<blockquote>', endBlockQuote, '</blockquote>',1,1)
    else:
        raise Exception('unknown type')

def process(s):

    s = f"\n\n{s}"
    print(s)
    slen = len(s)
    para = makeMarkDownEl('P')
    br = makeMarkDownEl('BR')
    strike = makeMarkDownEl('STRIKE')
    blockquote = makeMarkDownEl('BLOCKQUOTE')
    blockTypes = [para]
    inlineTypes = [strike]
    markerTypes = [br]
    tokenTypes = [para,blockquote,strike,br]

    buffer = []
    tokenStack = [] # [P,BLOCK, STRIKE]
    lenS = len(s)
    i = 0
    blockEls = []
    inBlock = False
    while i < slen:
        ch = s[i]
        j = i
        while len(tokenStack) and tokenStack[-1].matchesClosing(j,ch,s):
            tokenType = tokenStack.pop()
            if tokenType.identifier == 'BLOCKQUOTE':
                inBlock = False
            j += tokenType.endChomp

        for tokenType in tokenTypes:
            if tokenType.matchesOpening(j,ch,s):
                if tokenType.identifier != 'BLOCKQUOTE' or not inBlock:
                    buffer.append(tokenType.opening)
                    if tokenType.identifier == 'BLOCKQUOTE':
                        inBlock = True
                j += tokenType.beginChomp
                if tokenType.closing:
                    tokenStack.append(tokenType)

        if i != j:
            i = j
            continue;

        buffer.append(ch)
        i += 1

    while len(tokenStack):
        tokenType = tokenStack.pop()
        buffer.append(tokenType.closing)


    return ''.join(buffer)

def goof(s):

    print(s)
    while i < lenS:
        ch = s[i]
        while len(tokenStack) and tokenStack[-1].matchesClosing(i,ch,s):
            i += 1
            buffer.append(tokenStack[-1].closing)
            ts = tokenStack.pop()

        if i >= lenS:
            break;
        for tokenType in tokenTypes:
            if tokenType.matchesOpening(i,ch,s):
                tokenStack.append(tokenType)
                buffer.append(tokenType.opening)
                print("appendeing char ", ch, tokenType.identifier,i + tokenType.endChomp)
                if i != 0:
                    i += tokenType.endChomp

        if i < lenS:
            ch = s[i]
            buffer.append(ch)

        i += 1

    while len(tokenStack):
        print('end of',tokenStack[-1].identifier, ch)
        buffer.append(tokenStack[-1].closing)
        ts = tokenStack.pop()

    return ''.join(buffer)
