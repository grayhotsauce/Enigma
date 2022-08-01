import Enigma
import time

testCases = ["foolsball", "mother", "fives", "your mother", "mom is awesome", "geg", "smolensk", "moscow"]


def tester():
    #---------------------------
    #initialized start variables
    #

    counter = 0
    grade = 0
    start = time.time()

    #-------------------------------
    # 3 disk start settings per test
    #

    for x in range(0, 25):
        for y in range(0, 25):
            for z in range(0, 25):

                #--------------------------------------------------------------------------------------------
                # counter keeps track of amount of tests
                # encryption takes in the test words and start settings and returns the encrypted version
                # decryption takes in the encrypted result and returns the plain text
                # the original text is compared to the decryption result and if it is the same, it is tallied

                for cases in testCases:
                    counter += 1
                    encryption = Enigma.enigmaScramble(cases, z, y, x)
                    decryption = Enigma.enigmaUnscramble(encryption, z, y, x)
                    '''
                    print("\nOriginal message:", cases)
                    print("Settings:", z, y, x)
                    print("Encryption:", encryption)
                    print("Decryption:", decryption)
                    '''
                    if cases == decryption:
                        grade += 1
                        #print(cases+" is equivalent to "+decryption, "SUCCESS!")
                    #else:
                     #   print(cases+" is not equivalent to "+decryption, "FAILED!")

    #-------------------
    # Final results tallied
    # Time taken,
    # Success rate,
    # Number of tests

    stop = time.time()
    timeTaken = stop-start
    grade = (grade/counter)*100
    print("\nSuccess rate:", str(grade)+"%")
    print("Total number of encryptions:", counter)
    print(timeTaken, "secs")


tester()
