class Calculus:
    def __init__(self,function):
        self.function = function
    def differentiate(self):
        pass
    def integrate(self):
        pass
    def find(self,str,char):
        yield [c for c, value in enumerate(str) if value == char]
    def __add__(self, other):
        self.selfaddLIST = list(self.find(self.function[1],"^"))[0]
        self.selfdegrees = list(int(self.function[1][i+1]) for i in self.selfaddLIST)
        self.coeff = list(map(lambda x: int(self.function[1][x-2]),self.selfaddLIST))

        self.otheraddLIST = list(other.find(other.function[1],"^"))[0]
        self.otherdegrees = list(int(other.function[1][i+1]) for i in self.otheraddLIST)
        self.othercoeff = list(map(lambda x: int(other.function[1][x - 2]), self.otheraddLIST))

        self.commoncoeff = []
        self.commoncoeff.extend(self.coeff)

        self.degrees = []
        self.degrees.extend(self.selfdegrees)

        print(self.commoncoeff)
        for i in self.selfdegrees:
            if i in self.otherdegrees:
                self.commoncoeff[self.selfdegrees.index(i)] = self.coeff[self.selfdegrees.index(i)]+self.othercoeff[self.otherdegrees.index(i)]
                self.othercoeff.pop(self.otherdegrees.index(i))
                self.otherdegrees.pop(self.otherdegrees.index(i))
        self.commoncoeff.extend(self.othercoeff)
        self.degrees.extend(self.otherdegrees)

        return "FuncAdded = " + " + ".join(list(map(lambda x: str(x)+'x^'+str(self.degrees[self.commoncoeff.index(x)]),self.commoncoeff))) + " + C"
    def __sub__(self, other):
        self.selfaddLIST = list(self.find(self.function[1], "^"))[0]
        self.selfdegrees = list(int(self.function[1][i + 1]) for i in self.selfaddLIST)
        self.coeff = list(map(lambda x: int(self.function[1][x - 2]), self.selfaddLIST))

        self.otheraddLIST = list(other.find(other.function[1], "^"))[0]
        self.otherdegrees = list(int(other.function[1][i + 1]) for i in self.otheraddLIST)
        self.othercoeff = list(map(lambda x: int(other.function[1][x - 2]), self.otheraddLIST))

        self.commoncoeff = []
        self.commoncoeff.extend(self.coeff)

        self.degrees = []
        self.degrees.extend(self.selfdegrees)

        print(self.commoncoeff)
        for i in self.selfdegrees:
            if i in self.otherdegrees:
                self.commoncoeff[self.selfdegrees.index(i)] = self.coeff[self.selfdegrees.index(i)] - self.othercoeff[
                    self.otherdegrees.index(i)]
                self.othercoeff.pop(self.otherdegrees.index(i))
                self.otherdegrees.pop(self.otherdegrees.index(i))
        self.commoncoeff.extend(self.othercoeff)
        self.degrees.extend(self.otherdegrees)

        return "FuncAdded = " + " + ".join(list(
            map(lambda x: str(x) + 'x^' + str(self.degrees[self.commoncoeff.index(x)]), self.commoncoeff))) + " + C"
    def __mul__(self, other):
        self.find(self.function[1], "^")
        pass
    def __truediv__(self, other):
        pass
    def __str__(self):
        return self.function[0] + " = " + self.function[1]
def isit_invalidFunction(function):
    variable_count = 0
    ValidVAR =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in ValidVAR:
        if letter in function:
            variable_count += 1
    if variable_count == 1:
        FunctionORNOT = True
    else:
        FunctionORNOT = False
    for i in function:
        if i in ['@','#','$','%','&',':','"',"'",'<','>','?','*','=','\\','/']:
            FunctionORNOT = False
    return FunctionORNOT

def main():
    print("""Please enter a valid function with their degrees, for example: 
        4x^2 + 7x^1 + 8 -> Yes :)
        8x^2 + 3x + 3 -> no
        positive coefficients only
    """)
    functionStorage = []
    exitCommands = ['exit','break','quit']
    userInput = input("Enter a function: ").replace(" ", "")
    Counter = 0
    while userInput.lower() not in exitCommands:
        if isit_invalidFunction(userInput):
            FunctionOF = input("Enter a variable to represent function: ")
            if FunctionOF in userInput:
                print("please enter a valid variable")
                FunctionOF = input("Enter a variable to represent function: ")
            if Counter >= 1:
                for i in functionStorage:
                    if FunctionOF != i[0]:
                        isValidVAR = True
                    else:
                        isValidVAR = False
                if isValidVAR:
                    aOBJ = Calculus([FunctionOF, userInput])
                    functionStorage.append([FunctionOF, userInput])
                    print(functionStorage)
                    previousOBJ = Calculus(functionStorage[Counter-1])
                    print(aOBJ - previousOBJ)
                else:
                    print("it's not valid")
            else:
                aOBJ = Calculus([FunctionOF,userInput])
                functionStorage.append([FunctionOF, userInput])
                print(functionStorage)
        else:
            print("invalid function")
        userInput = input("Enter a function: ").replace(" ", "")
        Counter += 1

if __name__ == '__main__':
    main()

