# from doctest import testmod


def urlify(url):
    """
    >>> urlify("Mr John Smith     ")
    "Mr%20John%20Smith"
    """
    for i in reversed(range(len(url))):
        print(url[i])


print(urlify("Mr John Smith     "))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
#     verbose = True