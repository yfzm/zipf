import random


def main(num, out):
    dic = open("dictionary.txt", "r")
    words = dic.readlines()
    dic.close()
    random.shuffle(words)
    with open(out, 'w') as f:
        for word in words[0:num]:
            f.write(word)


if __name__ == '__main__':
    main(num=1000, out="sample_word.txt")
