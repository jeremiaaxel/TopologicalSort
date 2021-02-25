# File : main.py
# program untuk melakukan topological sort

from pathlib import Path
from os.path import join

from myLib.DAGraph import DAGraph
from myLib.ListOfCourses import ListOfCourses
from myLib.FileParser import FileParser

debug = True
test_file = "test1.txt"

### MAIN ####
test_dir = join(Path(__file__).resolve().parent.parent, "test")

if (debug == True):
    filename = test_file
else:
    print("File input otomatis dipindah ke folder test.")
    filename = input("Insert file name : ")

course_list = FileParser.file_to_list_of_courses(filename, test_dir)
# print(course_list)

list_of_courses = []
for course in course_list:
    p = DAGraph(course[0], course[1:])
    list_of_courses.append(p)

del course_list

print("Initial list of courses")
for course in list_of_courses:
    print(course, end=".\n")

list_of_courses_plan = []
loop = 0
while len(list_of_courses) > 0:
    targets = ListOfCourses()
    for course in list_of_courses:
        if len(course.getPreq()) == 0:
            targets.add(course.getMain())

            # print("\nCurrently looking for: " + course.getMain())
            
            list_of_courses.remove(course)


    if (len(targets) > 0):
        list_of_courses_plan.append(targets)

        # print("list_of_course_taken : ")
        # print(list_of_courses_plan)

        for target in targets.getCourses():
            for course in list_of_courses:

                # print(course.getMain() + " has prequisite : ", end="")
                # print(course.getPreq())

                if (course.getPreq().has(target)):
                    course.remove_this_from_preq(target)
    else:
        print("No course with zero or taken prequisite found")
        break

print()
for i in range(len(list_of_courses_plan)):
    print("Semester {num} : {courses}.".format(num=i+1, courses=list_of_courses_plan[i]))