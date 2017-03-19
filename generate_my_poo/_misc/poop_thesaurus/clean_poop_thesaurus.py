lines = open('poop_thesaurus.txt', 'r').readlines()

stripped = []
for line in lines:
    stripped.append(line.strip().lower())

string = ' '.join(stripped)
words = string.split(' ')
deduped = list(set(words))
clean_string = ' '.join(deduped)

f = open('poop_thesaurus_clean.txt', 'w')
f.write(clean_string)
f.close()
