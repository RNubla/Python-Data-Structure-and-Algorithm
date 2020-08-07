def romanToInt(s: str) -> int:
    keyVal = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 100
              }
    for i in range(len(s)):
        t = s[i]
        # tmp = 0
        for t in keyVal:
            tmp = 0
            if t == 'I':
                tmp = tmp + keyVal[t]
        return tmp


romanToInt('II')
