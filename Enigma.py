alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


rotor1pairing = [15, 4, 25, 20, 14, 7, 23, 18, 2, 21, 5, 12, 19,  1, 6, 11, 17, 8, 13, 16, 9, 22, 0, 24, 3, 10]
rotor2pairing = [25, 14, 20, 4, 18, 24, 3, 10, 5, 22, 15, 2, 8, 16, 23, 7, 12, 21, 1, 11, 6, 13, 9, 17, 0, 19]
rotor3pairing = [4, 7, 17, 21, 23, 6, 0, 14, 1, 16, 20, 18, 8, 12, 25, 5, 11, 24, 13, 22, 10, 19, 15, 3, 9, 2]


#-----------------------------------------------
#
#resets rotor cycle if necessary
#

def rotor(key, t):
    if key+t > 25:
        return key+t-26
    else:
        return key+t

#-----------------------------------------------
#
#encrypts the string
#

def enigmaScramble(message, t1, t2, t3):
    eMessage = ""
    for letter in message:
        key = 0
        for l in alphabet:
            if letter == " ":
                key = " "
                break
            if letter == l:
                break
            else:
                key += 1

        if t1 > 25:
            t1 = t1 - 26
            t2 += 1
        if t2 > 25:
            t2 = t2 - 26
            t3 += 1
        if t3 > 25:
            t3 = t3 - 26
        if key != " ":
            eMessage = eMessage + alphabet[rotor3pairing[rotor(rotor2pairing[rotor(rotor1pairing[rotor(key, t1)], t2)], t3)]]
            t1 += 1
        else:
            eMessage = eMessage + " "

    return eMessage


#-----------------------------------------------
#
#translates the encrypted message
#


def enigmaUnscramble(message, t1, t2, t3):
    x = 0
    decryption = ""
    for letter in message:
        x = x + 1
        aKey = 0
        r3Key = 0
        r2Key = 0
        r1Key = 0
        for l in alphabet:
            if letter == l:
                break
            else:
                aKey += 1

        for m in rotor3pairing:
            if m == aKey:
                break
            else:
                r3Key += 1

        if t3 != 0:
            r3Key = r3Key - t3

        if r3Key < 0:
            r3Key = r3Key + 26

        for n in rotor2pairing:
            if n == r3Key:
                break
            else:
                r2Key += 1

        if t2 != 0:
            r2Key = r2Key - t2

        if r2Key < 0:
            r2Key = r2Key + 26

        for o in rotor1pairing:
            if o == r2Key:
                break
            else:
                r1Key += 1

        if t1 != 0:
            r1Key = r1Key - t1

        if r1Key < 0:
            r1Key = r1Key + 26

        if letter == " ":
            r1Key = " "

        if r1Key == " ":
            decryption = decryption + " "
        else:
            decryption = decryption + alphabet[r1Key]
            t1 += 1

        if t1 > 25:
            t1 = t1 - 26
            t2 += 1
        if t2 > 25:
            t2 = t2 - 26
            t3 += 1
        if t3 > 25:
            t3 = t3 - 26


    return decryption
