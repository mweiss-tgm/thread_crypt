import threading

def getMode():
    while True:
        print("Type '0' to exit the program, '1' to encrypt or '2' to decrypt")
        mode = int(input())
        if mode == 1 or mode == 2:
            return mode
        elif mode == 0:
            quit()
        else:
            print("")

def getTextAndThread():
    while True:
        print("Enter your message:")
        msg = input()
        if len(msg) < 1:
            print("Please type something bigger than '0' in")
        else:
            text = msg
            break

    threadnumber = 0

    while True:
        print("How many Threads should encrypt your message?")
        mess = input()
        if int(mess) > 0:
            if mess.isdigit():
                if len(text) / int(mess) < 1:
                    print("That are to many threads")
                else:
                    threadnumber += int(mess)
                    break
            else:
                print("Please type only digits")
        else:
            print("Type in a number of threads bigger than '0'")

    threadnumber += threadnumber
    return text, threadnumber

def getKey():
    key = 0
    while True:
        print("Enter the key number (1-26)")
        key = int(input())
        if (key >= 1 and key <= 26):
            return key

def getTranslatedMessage(mode, message, key):
    if mode == 2:
        key = -key
    translated = ""

    for symbol in message.lower():
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if num > ord("z"):
                num -= 26
            elif num < ord("a"):
                num += 26

            translated += chr(num)
        else:
            translated += symbol

    threads = []
    whole = len(message)
    thpart = len(message) / thnumber
    threads = [message[i:i + thpart] for i in range(0, whole, thpart)]

    for i in range(1, thnumber + 1):
        thread = EncryptThread(i, threads[i - 1])
        threads += [thread]
        thread.start()

    for x in threads:
        x.join()
        translated += x.result

    print("Your translated text is:" + translated)

mode = getMode()
message = getTextAndThread()
key = getKey()


#print(getTranslatedMessage(mode, message, key, thnumber))

class EncryptThread(threading.Thread):

    __anzahl = 0

    def __init__(self, th_number, text):#
        threading.Thread.__init__(self)
        self.th_number = th_number
        self.text = text
        self.result = ""
        EncryptThread.__anzahl += 1

    def run(self):
        getTranslatedMessage(mode, message, key)
