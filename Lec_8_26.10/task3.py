def add_and_pow(n):
    return n + n ** 3 + n ** 5

answers = []

with open('numbers.txt', 'r') as work_file:
    print(dir(work_file))
    for num in work_file:
        num = num.rstrip()
        nums = num.split()
        s = float(num[0]) + float(nums[1])
    
        answer = add_and_pow(s)
        answers.append(answer)
        print(answers)






