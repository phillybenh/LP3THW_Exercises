from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
# print(txt) >>> "<_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='UTF-8'>"
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close
txt_again.close
