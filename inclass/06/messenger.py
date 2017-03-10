import random
import videomash


nouns = open('nouns.txt', 'r').readlines()
word1 = random.choice(nouns).strip()
word2 = random.choice(nouns).strip()

print word1, word2

videomash.mash(word1, word2)
