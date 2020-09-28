def count_recursive(number):


    if number == 0 :
        return
    
    print(number)

    count_recursive(number - 1)

count_recursive(20)