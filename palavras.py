# -*- coding: utf-8 -*-

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

def readDict():
    print "Reading all words..."
    dicionario = open("palavras.txt", 'r')
    palavras = []
    for line in dicionario:
        line = line.rstrip("\n")
        if len(str(line)) > 8:
            continue
        if len(str(line)) < 3:
            continue
        elif "-" in line:
            continue
        else:
            palavras.append(line)

    print "Read %d words valid for the game!" % len(palavras)

    return palavras

def readLetters(inStr):
    print "Reading user letters..."
    return inStr.split(" ")

def calculateWords(palavras, letters):
    print "Starting to calculate possible words..."
    words = []
    for palavra in palavras:
        flag = True
        letras = letters[:]
        for letra in palavra:
            if letra in letras:
                letras.remove(letra)
                continue
            else:
                flag = False
                break
        if flag == True:
            words.append(palavra)

    print "Found %d possible words!" % len(words)

    return words


def readUserInput():
    if len(sys.argv) > 9:
        raise Exception("To much characters!!")
    elif sys.argv[8] != None:
        userInput = sys.argv[1:9]
        print userInput
        return userInput
    else:
        raise Exception("Invalid user input!!")

def main():
    print "Starting word calculation..."
    palavras = readDict()

    userInput = readUserInput()
    letters = userInput
    #letters = readLetters(userInput)

    words = calculateWords(palavras, letters)

    pp.pprint(words)


if __name__ == '__main__':
    main()


