message = input("Send message: ")
message = message.lower()

counter = {}

for letter in message:
    if letter in counter.keys():
        counter[letter] += 1
    else:
        counter[letter] = 1

for k, v in counter.items():
    print( k, ":", v)


D = {1:20, 3:50, 6:90, True: False, None : "kEK", (1,2,3) : [1,2,3]}
print(D[None])
print(D[(1,2,3)])