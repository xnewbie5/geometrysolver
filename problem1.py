from sympy.geometry import*
import math

class problem1:
    def __init__(self):
        self.List = dict() #list of known variables
        self.i1 = None
        self.i2 = None
        self.c1 = None
        self.c2 = None
        self.List =	{
            "v1": None,
            "v2": None,
            "v3": None,
            "a1": None,
            "a2": None,
            "a3": None,
            "e1": None,
            "e2": None,
            "e3": None,
            "radius": None,
            "center": None                
        }

    def get_all(self):
        print (self.List)
        return self.List

    def get_value(self, name):
        if name in self.List:
            print (self.List.get(name))
            return self.List.get(name)

    #ASSUME THE CENTER OF CIRCLE IS A VERTEX
    def set_vertex(self, name, x, y):
        if (name == "v1" or name == "v2" or name == "v3" or name == "center"):
            if name in self.List: #checks if the String name is in the list
                self.List[name] = Point(x,y)
    
    def set_value(self, name, value):
        if (name != "v1" and name != "v2" and name != "v3" and name != "center"):
            if name in self.List:
                if (name == "a1" or name == "a2" or name == "a3"):
                    self.List[name] = math.radians(value)
                else:
                    self.List[name] = value

    def create_triangle(self):
        #check if we can create a triangle (3 vertices only)
        return


    #attempt to solve triangle
    def solve_Triangle(self):
        #put in a bunch of if cases
        tempV1 = self.List["v1"]
        tempV2 = self.List["v2"]
        tempV3 = self.List["v3"] 

        return True #return True if no more things to solve

    #attempt to solve circle
    def solve_Circle(self):
        if((self.List["radius"] != None) and (self.List["center"] != None)):
            tempCircle = Circle(self.List["center"], self.List["radius"])
            print("TempCircle Created")
        #does it intersect a line segment twice?
        if():
            pass
        return True



        