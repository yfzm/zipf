import random


class ZipFGenerator:
    def __init__(self, word_count, alpha):
        # self.word_count = word_count
        # self.out = out
        self.ps = [1.0 / (i + 1) ** alpha for i in range(word_count)]
        s = sum(self.ps)
        self.ps = map(lambda x: x / s, self.ps)
        dic = open('sample_word.txt', 'r')
        self.all_words = dic.readlines()
        dic.close()

    def generate(self, size, out):
        words = size * 91500
        # words = size
        num_per_word = map(lambda x: x * words, self.ps)
        index_list = []
        for index, n in enumerate(num_per_word):
            for i in range(int(n)):
                index_list.append(index)
        random.shuffle(index_list)

        with open(out, 'w') as f:
            for word in index_list:
                f.write(self.all_words[word].strip() + '\n')


if __name__ == '__main__':
    generator = ZipFGenerator(word_count=1000, alpha=1)
    generator.generate(size=100, out='./output/data_100M')
