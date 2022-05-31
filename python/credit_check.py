from functools import reduce

def credit_check(str):
    #pass
    #syntax reverse sting [::-1]
    reversed_num = str[::-1]
    #use map to turn list of string into list of ints
    #map(convert to int, pass it list) it iterates through
    #map is an object so needs to be converted to other type like list
    int_list = list(map(int,(list(reversed_num))))

    list_combo_every_other = []
    #iterate over list
    #basic syntax is is enumerate(sequence, start=0)
    #enumerate returns enumerate object, lets me get index, once in a loop/iteration
    for number, i in enumerate(int_list):
        if i % 2 == 0:
            list_combo_every_other.append(number)
        else: 
            list_combo_every_other.append(number)
        

    # list_every_other = []
    # list_numbers = []
    # for j in reversed_num:
    #     list_numbers.append(int(j))
    # #syntax used to increment use slice [1::2]
    # for i in list_numbers[1::2]:
    #     #every other conver number by 2
    #     list_every_other.append(i*2)
    #     list_numbers.remove(i)

    # for j in reversed_num:
    #     list_numbers.append(int(j))

    print(int_list)
    print(list_combo_every_other)

    #return list_every_other
    # print(list_numbers)
    # print(list_every_other)

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

print(credit_check("5541808923795240"))