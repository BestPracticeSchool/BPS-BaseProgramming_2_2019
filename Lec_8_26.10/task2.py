def add_and_pow(n):
    return n + n ** 3 + n ** 5


answers = []

work_file = open("numbers.txt", 'r')
for num in work_file:
    num = num.rstrip()
   
    answer = add_and_pow(float(num))
    answers.append(answer)
    print(answers)
work_file.close()


work_file = open('numbers_answers.txt', 'w')
for answer in answers:
    work_file.write(str(answer)+'\n')
work_file.close()
