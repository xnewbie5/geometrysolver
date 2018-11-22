from sympy.geometry import*
from problem1 import*
from problem2 import*
from problem3 import*

def main():
    #begin program1
    p1 = problem1()
    p2 = problem2()
    p3 = problem3()
    #p1.get_value("v1")
    #p1.get_all()
    #boot up a problem
    while p1.print_menu():
        #input("Enter anything to continue to the menu. ")
        pass
    while p2.print_menu():
        #input("Enter anything to continue to the menu. ")
        pass
    while p3.print_menu():
        #input("Enter anything to continue to the menu. ")
        pass


    print("Exiting program...")

if __name__ == "__main__":
    main()