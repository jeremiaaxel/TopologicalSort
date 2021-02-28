from myLib.ListOfCourses_13519188 import ListOfCourses

class DAGraph :
    ### Construct, Representation, and Destruct ###
    def __init__(self, main, preq=None) -> None:
        self.__main = main
        self.__preq = ListOfCourses(preq)
    
    def __repr__(self):
        name = self.__main
        if (len(self.__preq.getCourses()) > 0):
            name += ", " + str(self.__preq)
        
        return name
    
    def __str__(self) -> str:
        name = self.__main
        if (len(self.__preq) > 0):
            name += ", " + str(self.__preq)
        
        return name

    def destruct(self) -> None:
        del self

    ### Printing ###
    def print(self) -> None:
        name = self.__main
        if (len(self.__preq) > 0):
            name += ", " + str(self.__preq)
        
        print("{name}.".format(name=name), end="\n")

    ### Getter and Setter ###
    def getMain(self):
        return self.__main

    def setMain(self, newMain):
        self.__main = newMain
    
    def getPreq(self):
        return self.__preq

    def setPreq(self, newPreq):
        self.__preq.setCourses(newPreq)
    
    def add_this_to_preq(self, add_preq) -> None:
        self.__preq.addCourse(add_preq)

    def remove_this_from_preq(self, removed_preq) -> None:
        self.__preq.removeCourse(removed_preq)
