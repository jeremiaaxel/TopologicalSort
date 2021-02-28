from os.path import join
import os

def remove_excess_whitespace(word):
    i = 0
    while word[i] == " ":
        i += 1
    j = len(word)-1
    while word[j] == " ":
        j -= 1

    return word[i:j+1]
    

def file_to_list_of_courses(filename, test_dir=None) -> list:
    '''
    Takes test directory path (test_dir) and name of the file (filename)
    Return a list of strings.

    if test_dir is not declared, automatically switch to current directory
    '''
    try:
        if (test_dir is None):
            test_dir = os.getcwd()

        f = open(join(test_dir, filename), 'r')
        lines = f.read().splitlines()
        f.close()
        print("File read success")

        list_of_soals = []
        for line in lines:
            if (line != ""):
                line = line.replace(".", "").split(",")
                for i in range(len(line)):
                    line[i] = remove_excess_whitespace(line[i])

                list_of_soals.append(line)

        return list_of_soals

    except FileNotFoundError:
        print("File not found")
        exit(1)

    except TypeError:
        print("Input error")
        exit(1)

def romanizer(number):
    arabian_to_roman_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        ( 100, 'C'), ( 90, 'XC'), ( 50, 'L'), ( 40, 'XL'),
        (  10, 'X'), (  9, 'IX'), (  5, 'V'), (  4, 'IV'),
        (   1, 'I')]

    num = number
    result = ''
    i = 0
    while num > 0:
        while arabian_to_roman_dict[i][0] > num: 
            i += 1
        result += arabian_to_roman_dict[i][1]
        num -= arabian_to_roman_dict[i][0]
        
    return result