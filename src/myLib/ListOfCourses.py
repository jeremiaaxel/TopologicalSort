class ListOfCourses:
    def __init__(self, list_of_course=None) -> None:
        if (list_of_course is None):
            list_of_course = []
        elif (type(list_of_course) != "list"):
            list_of_course = list(list_of_course)
        self.__list_of_course = list_of_course

    def __repr__(self):
        name = ""
        for i in range(len(self.__list_of_course)):
            name += self.__list_of_course[i]
            if (i != len(self.__list_of_course)-1):
                name += ", "
        
        return name
    
    def __str__(self) -> str:
        name = ""
        for i in range(len(self.__list_of_course)):
            name += self.__list_of_course[i]
            if (i != len(self.__list_of_course)-1):
                name += ", "
        
        return name

    def __len__(self) -> int:
        return len(self.__list_of_course)

    def getCourses(self):
        return self.__list_of_course

    def setCourses(self, newCourses):
        if (type(newCourses) != "list"):
            newCourses = list(newCourses)

        self.__list_of_course = newCourses
    
    def add(self, add_course) -> None:
        self.__list_of_course.append(add_course)

    def remove(self, removed_course) -> None:
        self.__list_of_course.remove(removed_course)

    def has(self, search) -> bool:
        return search in self.__list_of_course