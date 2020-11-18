from doctest import testmod
def count_recursive(number):


    if number == 0 :
        return
    
    print(number)

    count_recursive(number - 1)

count_recursive(20)

if __name__ == '__main__': 
    testmod(verbose = True) 