import random

def i_tried():
    food = ""

    for i in range(10):
        temp = str(random.randint(0,4))
        food += temp

    return food

njajal = i_tried()
print("Im trying \n \n"+ njajal)