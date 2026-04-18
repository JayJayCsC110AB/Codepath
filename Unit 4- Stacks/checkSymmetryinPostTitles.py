def is_symmetrical_title(title):
    no_spaces = "".join(title.split()).lower()
    i = 0
    j = len(no_spaces)-1

    while i < j:
        if no_spaces[i] == no_spaces[j]:
            i += 1
            j -= 1
        elif no_spaces[i] != no_spaces[j]:
            return False
    return True

print(is_symmetrical_title("a Santa at NASA"))
print(is_symmetrical_title("Social Media"))
print(is_symmetrical_title("Race Car"))