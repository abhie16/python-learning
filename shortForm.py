
def initials(phrase):
    words = phrase.upper().split(" ")
    result = ""
    for word in words:
        result += word[0]
    return result


print(initials('local area network'))
print(initials('Universal serial bus'))
print(initials('Operating system'))
