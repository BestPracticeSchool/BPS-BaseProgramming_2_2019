try:
    value = int(input())
    answer = 10 / value
except ValueError as v_err :
    print("Invalid type of value!")
except ZeroDivisionError as z_err:
    print("Lol. U can'tmake zero division!")
else:
    print("Exception not found!")
    print("Else block working!")
    print(answer)
finally:
    print("HAHAHAHAH FINALLY!!")