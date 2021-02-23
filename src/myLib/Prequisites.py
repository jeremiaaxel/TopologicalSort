class Prequisites:
    def __init__(self, preq="None") -> None:
        if (preq is None):
            preq = []
        elif (type(preq) != "list"):
            preq = list(preq)
        self.__preq = preq

    def __repr__(self):
        name = ""
        for i in range(len(self.__preq)):
            name += self.__preq[i]
            if (i != len(self.__preq)-1):
                name += ", "
        
        return name
    
    def __str__(self) -> str:
        name = ""
        for i in range(len(self.__preq)):
            name += self.__preq[i]
            if (i != len(self.__preq)-1):
                name += ", "
        
        return name

    def __len__(self) -> int:
        return len(self.__preq)

    def getPreq(self):
        return self.__preq

    def setPreq(self, newPreq):
        if (type(newPreq) != "list"):
            newPreq = list(newPreq)

        self.__preq = newPreq
    
    def add(self, add_preq) -> None:
        self.__preq.extend(add_preq)

    def remove(self, removed_preq) -> None:
        self.__preq.remove(removed_preq)

    def has(self, search) -> bool:
        return search in self.__preq