words_dict = {} # word : int 

with open('poem.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1

for k,v in words_dict.items():
    print(k ,v)