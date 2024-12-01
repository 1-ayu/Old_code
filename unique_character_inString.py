def unique_char(character):
    char=set()
    for a in character:
        if a in char:
            return False
        else:
            char.add(a)
    return True

print(unique_char("bgisbg"))
print(unique_char("AyushKaran"))