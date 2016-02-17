#!/usr/bin/python3
def spellcheck(sentence):
    words = open("spell.words").readlines()
    words = list(map(lambda x: x.strip(), words))
    result = sentence.split()
    S_output = ["The mispelt words are: "]
    for item in result:
        if(item in words):
            continue
        else:
            S_output.append(item)
    return S_output
def main():
    sentence = input("Please enter a sentence\n")
    lst=[]
    lst=spellcheck(sentence)
    print(lst)
if __name__ == "__main__": main()