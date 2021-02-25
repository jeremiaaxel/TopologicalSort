# File : main.py
# program untuk melakukan topological sort

import sys

from pathlib import Path
from os.path import join

from myLib import FileParser
from myLib.DAGraph import DAGraph

def get_courses_str(list_of_courses):
    if (len(list_of_courses) > 0):
        result = list_of_courses[0]
        for i in range(1, len(list_of_courses)):
            result += ", " + list_of_courses[i]
        return result
    return 

def print_hasil(list_of_courses_plan):
    roman_num = [FileParser.romanizer(i+1) for i in range(len(list_of_courses_plan))]
    max = 0
    for rom in roman_num:
        if (len(rom) > max):
            max = len(rom)
    
    print("\nResult:")
    for i in range(len(list_of_courses_plan)):
        buffer = max-len(roman_num[i])
        print("Semester {num} ".format(num=roman_num[i]) + " "*buffer + ": {courses}.".format(courses=get_courses_str(list_of_courses_plan[i])))


### MAIN ####
test_dir = join(Path(__file__).resolve().parent.parent, "test")

# input filename
if (len(sys.argv) > 1):
    filename = sys.argv[1]
    print("Test case file : " + filename)
else:
    print("File input otomatis dipindah ke folder test.")
    filename = input("Insert file name : ")

# open file and create list of (list of strings)
course_list = FileParser.file_to_list_of_courses(filename, test_dir)

# convert list of strings to Graph
# first string in the list of strings becomes the course, the rest become the prequisites.
list_of_courses = []
for course in course_list:
    list_of_courses.append(DAGraph(course[0], course[1:]))

del course_list

# show the graph
print("Initial list of courses")
for course in list_of_courses:
    print(course, end=".\n")

# start topological sorting
list_of_courses_plan = []

# loop selama list of courses masih ada isinya
while len(list_of_courses) > 0:
    targets = []

    # mencari course-course dengan nol prequisite
    for course in list_of_courses:
        if len(course.getPreq()) == 0:
            # memasukan semua course yang preqnya nol ke dalam list
            targets.append(course.getMain())

    # jika terdapat course dengan nol prequisite
    if (len(targets) > 0):
        # memasukan semua courses tersebut ke dalam list hasil
        list_of_courses_plan.append(targets)

        # menghapus courses dengan nol prequisite dari prequisite courses lainnya
        for current_target in targets:
            for course in list_of_courses:
                if (course.getPreq().has(current_target)):
                    course.remove_this_from_preq(current_target)

            # menghapus course dengan nol prequisite dari list of courses utama
            for course in list_of_courses:
                if course.getMain() == current_target:
                    list_of_courses.remove(course)

    # jika tidak terdapat course dengan nol prequisite berarti graf tidak asiklik
    # dan program tidak dapat dilanjutkan            
    else:
        print("No course with zero or taken prequisite found")
        print("Last course searched : {}".format(list_of_courses_plan[-1][-1]))
        exit(1)

# menampilkan hasil
print_hasil(list_of_courses_plan)