formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your", 
    "Own text here", # lolz, no
    "Maybe a poem", # still nope
    "Or a song about fear" # why so afraid?
    ))

#what's this do? .... not much since it's jsut a string
print(formatter.format(1, 2, 3, 4) + formatter.format(3, 5, 6, 7))