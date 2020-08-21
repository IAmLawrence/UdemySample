import os

# print(os.getcwd())
hold_path = os.path.abspath('OS_MODULE_SAMPLE\\INSIDE_OS_MODULE_SAMPLE')
print("hold_path >", hold_path)
os.chdir(hold_path)
print("Current WD >", os.getcwd())

read_file = open('file_to_read.txt', 'r')
# file_name.write(" Lawrence") if you  uncomment this it will gives you an error because
# the file_to_read.txt is readable only
print("Read File >", read_file.read())
read_file.close()

write_file = open('file_to_write.txt', 'wt')
# print("Read File >", read_file.read()) if you  uncomment this it will gives you an error because
# the file_to_write.txt is not readable
# write will overwrite anything inside your file_to_write.txt and change whatever you put inside the parenthesis
write_file.write("Hello World") # Hello World original content is Hello There
write_file.close()

append_file = open('file_to_append.txt', 'a')
append_file.write(" Lawrence") # it will give you Hello There Lawrence
append_file.close()

loop_file = open('file_to_loop.txt', 'r')
for lines in loop_file.readlines():
    lines = lines.strip('\n')
    print("lines >", lines)
    if lines == 'lawrence':
        print("Found you!")
loop_file.close()

