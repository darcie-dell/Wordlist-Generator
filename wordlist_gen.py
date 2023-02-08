#Simple wordlist generator from given words and numbers and sends to a text file. 

from itertools import product

userInput = input("Input words for a wordlist separated by a space: \n") 

IndWords =  userInput.split()

words_for_wordlist = IndWords

def allwords(chars, length):
    for inputwords in product(chars, repeat=length):
        yield ''.join(inputwords)


def main():
    with open("words.txt", "a+") as f:
        inputwords = words_for_wordlist
        for wordlen in range(2, 5):
            for word in allwords(inputwords, wordlen):
                if len(word)>5:
                    f.write(word)
                    f.write("\n")

if __name__ == "__main__":
    main()
    