def Sum_of_two_strings(x,y):
    list=set()
    for letter in x:
        if(y.find(letter)>=0):
            list.add(letter)
        else:
            pass
    print(len(list))
Sum_of_two_strings('bee','peer')