from sys import argv #argv is argument variable

script, first, second, third = argv

print(">>>> argv=", repr(argv)) # debug line?

print("This script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

