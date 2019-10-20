from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# Q:"we could do these two on one line, how?"
# A: in_file = open(from_file, 'r') ???? 
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# New command, to me. exists() returns true/false is a file exists or not
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

