#'r' --- read / прочитать из файла
my_file = open("input.txt", mode = 'r')
text = my_file.read()
print(text)
my_file.close()





#'w' --- write / перезаписать
new_file = open("new_dir/new_input.txt", "w")
message = "Something!"
new_file.write(message)
new_file.close() 


#'a' --- дописать в конец
bp_file = open("input.txt", mode = "a")
new_message = "\nHey I'm here!"
bp_file.write(new_message)
bp_file.close()

print(1,2,3,4,5,5,67, sep="###", end = '\n')
print(12312893)