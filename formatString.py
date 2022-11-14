def formats(name, grade):
    return "{} had recieved {}% grade".format(name, grade)


def lucknumber(name):
    return "{name} , your lucky no is {number}".format(name=name, number=len(name)*3)


print(formats('Abhishek', 80))
print(formats('vivek', 60))
print(formats('nitin', 60))
print(lucknumber("abhishek"))
