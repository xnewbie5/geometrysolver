from sympy.geometry import*
from sympy.core.sympify import sympify
import math

class problem1:
    def __init__(self):
        self.List = dict() #list of known variables
        self.i1 = None #hidden from the user
        self.i2 = None
        self.c1 = None
        self.c2 = None
        # self.a1_rads = None
        # self.a2_rads = None
        # self.a3_rads = None

        self.circleCircumference = None
        self.circleArea = None
        self.triangleArea = None
        self.circleAreaInTriangle = None
        self.circleAreaOutsideTriangle = None

        self.trianglePerimeter = None
        self.triangleAreaPartial = None

        self.List =	{
            "v1": None,
            "v2": None,
            "v3": None,
            "a1": None, #remember, do math in radians
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

    def print_menu(self):
        #print out the list in the dictionary and prompt for editing
        j = 1
        for i in self.List:
            if(isinstance(self.List[i], Point2D)):
                print(j,i,"=", self.List[i].evalf())
                j+=1
            else:
                print(j,i,"=",self.List[i])
                j+=1
        print(j,"Submit")
        j+=1
        print(j, "Print additional variables")
        j+=1
        print(j, "Set an Example")
        j+=1
        print(j, "Clear (run this atleast once before each solve)")
        j+=1
        print(j,"Quit")
        uInput = input("Select an option or choose a value to edit: ")
        #Keep main menu loop going by returning True
        if(self.perform_Operation(uInput)==True):
            return True
        else:
            return False

    def testFloat(self, x):
        try:
            return float(eval(x))
        except ValueError:
            print("Not a float", x)
            return False
        except SyntaxError:
            print("Not a float", x)
            return False
        except NameError:
            print("Not a float", x)
            return False

    def perform_Operation(self, operation):
        if operation.lower() in {"1","v1"}:
            uInput = input("Input value for VERTEX v1 X: ")
            f_uInput = self.testFloat(uInput)
            uInput2 = input("Input value for VERTEX v1 Y: ")
            f2_uInput = self.testFloat(uInput2)
            if(type(f_uInput)==float and type(f2_uInput)==float):
                self.set_vertex("v1", sympify(uInput, rational=True), sympify(uInput2, rational=True))
                #print("Successfully edited v1")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"2","v2"}:
            uInput = input("Input value for VERTEX v2 X: ")
            f_uInput = self.testFloat(uInput)
            uInput2 = input("Input value for VERTEX v2 Y: ")
            f2_uInput = self.testFloat(uInput2)
            if(type(f_uInput)==float and type(f2_uInput)==float):
                self.set_vertex("v2", sympify(uInput, rational=True), sympify(uInput2, rational=True))
                print("Successfully edited v2")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"3","v3"}:
            uInput = input("Input value for VERTEX v3 X: ")
            f_uInput = self.testFloat(uInput)
            uInput2 = input("Input value for VERTEX v3 Y: ")
            f2_uInput = self.testFloat(uInput2)
            if(type(f_uInput)==float and type(f2_uInput)==float):
                self.set_vertex("v3", sympify(uInput, rational=True), sympify(uInput2, rational=True))
                print("Successfully edited v3")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"4","a1"}:
            uInput = input("Input value (angle in degrees) for a1: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("a1", sympify(uInput, rational=True))
                print("Successfully edited a1")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"5","a2"}:
            uInput = input("Input value (angle in degrees) for a2: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("a2", sympify(uInput, rational=True))
                print("Successfully edited a2")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"6","a3"}:
            uInput = input("Input value (angle in degrees) for a3: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("a3", sympify(uInput, rational=True))
                print("Successfully edited a3")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"7","e1"}:
            uInput = input("Input value (edge length) for e1: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("e1", sympify(uInput, rational=True))
                print("Successfully edited e1")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"8","e2"}:
            uInput = input("Input value (edge length) for e2: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("e2", sympify(uInput, rational=True))
                print("Successfully edited e2")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"9","e3"}:
            uInput = input("Input value (edge length) for e3: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("e3", sympify(uInput, rational=True))
                print("Successfully edited e3")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"10","radius"}:
            uInput = input("Input value for radius: ")
            f_uInput = self.testFloat(uInput)
            if(type(f_uInput)==float):
                self.set_value("radius", sympify(uInput, rational=True))
                print("Successfully edited radius")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"11","center"}:
            uInput = input("Input value for CENTER of CIRCLE X: ")
            f_uInput = self.testFloat(uInput)
            uInput2 = input("Input value for CENTER of CIRCLE Y: ")
            f2_uInput = self.testFloat(uInput2)
            if(type(f_uInput)==float and type(f2_uInput)==float):
                self.set_vertex("center", sympify(uInput, rational=True), sympify(uInput2, rational=True))
                print("Successfully edited CENTER of CIRCLE")
            else:
                print("Invalid type entered")
        elif operation.lower() in {"12", "submit"}:
            self.solve_looping()
        elif operation.lower() in {"13"}:
            self.print_extra_variables()
        elif operation.lower() in {"14"}:
            self.set_Example()
        elif operation.lower() in {"15", "clear"}:
            self.clear()
        elif operation.lower() in ("16", "quit", "q"):
            return False
        return True #leave switch case

    def get_value(self, name):
        if name in self.List:
            print (self.List.get(name)) #difference b/w direct access and get() is the default value if not found. Default is None
            return self.List.get(name)

    def set_Example(self):
        for x in self.List:
            self.List[x] = None
        self.List["v1"] = Point(1.8,2.4)
        self.List["v2"] = Point(0,0)
        self.List["v3"] = Point(5,0)
        self.set_vertex("center", 4 ,1.2)
        self.List["radius"] = 0.6

    def clear(self):
        for x in self.List:
            self.List[x] = None
        self.i1 = None #hidden from the user
        self.i2 = None
        self.c1 = None
        self.c2 = None
        self.a1_rads = None
        self.a2_rads = None
        self.a3_rads = None

        self.circleCircumference = None
        self.circleArea = None
        self.triangleArea = None
        self.circleAreaInTriangle = None
        self.circleAreaOutsideTriangle = None
        self.triangleAreaPartial = None

    def print_extra_variables(self):
        if(isinstance(self.i1,Point2D)):
            print("i1: ", self.i1.evalf())
        else:
            print("i1: ", None)
        if(isinstance(self.i2,Point2D)):
            print("i2: ", self.i2.evalf())
        else:
            print("i2: ", None)
        print("c1: ", self.c1)
        print("c2: ", self.c2)
        if(self.trianglePerimeter != None):
            print("Triangle Perimeter: ", round(self.trianglePerimeter,2))
        else:
            print("Triangle Perimeter: ", None)
        if(self.triangleArea != None):
            print("Triangle Area: ", round(self.triangleArea,2))
        else:
            print("Triangle Area: ", None)
        if(self.circleCircumference != None):
            print("Circle Circumference: ", round(self.circleCircumference,2))
        else:
            print("Circle Circumference: ", None)
        if(self.circleArea != None):
            print("Circle Area: ", round(self.circleArea,2))
        else:
            print("Circle Area: ", None)
        if(self.triangleAreaPartial != None):
            print("Triangle Area (minus circle): ", round(self.triangleAreaPartial,2))
        else:
            print("Triangle Area (minus circle): ", None)
        if(self.circleAreaInTriangle != None):
            print("Circle Area in Triangle: ", round(self.circleAreaInTriangle,2))
        else:
            print("Circle Area in Triangle: ", None)
        if(self.circleAreaOutsideTriangle != None):
            print("Circle Area outside Triangle: ", round(self.circleAreaOutsideTriangle,2))
        else:
            print("Circle Area outside Triangle: ", None)
        #input("Enter anything to continue...")

    #for use with the website.
    def print_extra_variables_website(self):
        if(isinstance(self.i1,Point2D)):
            print("<br>i1: ", self.i1.evalf())
        else:
            print("<br>i1: ", None)
        if(isinstance(self.i2,Point2D)):
            print("<br>i2: ", self.i2.evalf())
        else:
            print("<br>i2: ", None)
        print("<br>c1: ", self.c1)
        print("<br>c2: ", self.c2)
        if(self.trianglePerimeter != None):
            print("<br>Triangle Perimeter: ", round(self.trianglePerimeter,2))
        else:
            print("<br>Triangle Perimeter: ", None)
        if(self.triangleArea != None):
            print("<br>Triangle Area: ", round(self.triangleArea,2))
        else:
            print("<br>Triangle Area: ", None)
        if(self.circleCircumference != None):
            print("<br>Circle Circumference: ", round(self.circleCircumference,2))
        else:
            print("<br>Circle Circumference: ", None)
        if(self.circleArea != None):
            print("<br>Circle Area: ", round(self.circleArea,2))
        else:
            print("<br>Circle Area: ", None)
        if(self.triangleAreaPartial != None):
            print("<br>Triangle Area (minus circle): ", round(self.triangleAreaPartial,2))
        else:
            print("<br>Triangle Area (minus circle): ", None)
        if(self.circleAreaInTriangle != None):
            print("<br>Circle Area in Triangle: ", round(self.circleAreaInTriangle,2))
        else:
            print("<br>Circle Area in Triangle: ", None)
        if(self.circleAreaOutsideTriangle != None):
            print("<br>Circle Area outside Triangle: ", round(self.circleAreaOutsideTriangle,2))
        else:
            print("<br>Circle Area outside Triangle: ", None)

    #ASSUME THE CENTER OF CIRCLE IS A VERTEX
    def set_vertex(self, name, x, y):
        if (name == "v1" or name == "v2" or name == "v3" or name == "center"):
            if name in self.List: #checks if the String name is in the list
               # self.List[name] = Point(x,y, evaluate=False) #keep the user input before evaluation
               self.List[name] = Point(x,y)
    
    def set_value(self, name, value):
        if (name != "v1" and name != "v2" and name != "v3" and name != "center"):
            if name in self.List:
                if (name == "a1"):
                    #self.a1_rads = math.radians(value)
                    self.List[name] = value
                elif (name == "a2"):
                    #self.a2_rads = math.radians(value)
                    self.List[name] = value
                elif (name == "a3"):
                    #self.a3_rads = math.radians(value)
                    self.List[name] = value
                else:
                    self.List[name] = value

    def create_triangle(self):
        #check if we can create a triangle (3 vertices only)
        return

    def solve_looping(self):
    #begin solve looping, solve returns false if there are no more things left to solve
    #so only break out if result and result2 return true.
    #everytime something is solved once, false statement is returned.
        counter = 0
        while True:
            result = self.solve_Triangle()
            result2 = self.solve_Circle()
            if(result and result2):
                #input("Done! No more things to solve. Enter anything to continue... ")
                break
            else:
                counter+=1
                if(counter==30):
                    print("Unsolvable. Try again?")
                    #input("Unsolvable. Enter anything to continue... ")
                    break
        self.solve_extra_variables()

    #Use this function after everything for the user-side has been set.
    def solve_extra_variables(self):
        if(self.List["radius"]!= None):
            self.circleCircumference = self.List["radius"] * 2 * math.pi
            self.circleArea = math.pi*self.List["radius"]*self.List["radius"]

        #If the list is complete...else RETURN 
        for x in self.List:
            if(self.List[x]== None):
                return

        #solve all variables
        #triangle area
        tTri = Triangle(self.List["v1"], self.List["v2"], self.List["v3"])
        self.triangleArea = tTri.area
        #triangle perimeter
        self.trianglePerimeter = tTri.perimeter

        #arclengths as well as the circle area in triangle
        if(self.i1 != None and self.i2 != None):
            smallTri = Triangle(self.i1, self.i2, self.List["center"])
            #smallTri must NOT be a segment (aka center is collinear with i1 and i2.)
            if(not isinstance(smallTri, Segment2D) and isinstance(smallTri, Triangle)):
                ray1 = Ray(self.List["center"],self.i1)
                ray2 = Ray(self.List["center"],self.i2)
                #returns the nonreflex angle (smaller) in radians
                self.c2 = self.toDegrees(ray1.angle_between(ray2))
                self.c1 = 360-self.c2
                #swap them if the circle is inside. Use the rays to help.
                if(tTri.encloses_point(self.List["center"])):
                    temp = self.c2
                    self.c2 = self.c1
                    self.c1 = temp 
                self.circleAreaInTriangle = float((self.c2 /360)*float(self.circleArea)) - float(smallTri.area)
            #smallTri is collinear with i1 and i2...
            else:
                self.circleAreaInTriangle = self.circleArea/2
                self.c1 = 180
                self.c2 = 180
                
        #Circle area outside triangle
        if(self.circleAreaInTriangle != None and self.circleArea != None):
            self.circleAreaOutsideTriangle = self.circleArea - self.circleAreaInTriangle

        #triangle area minus the inside circle area
        if(self.circleAreaInTriangle != None and self.triangleArea != None):
            self.triangleAreaPartial = self.triangleArea - self.circleAreaInTriangle

    #attempt to solve triangle. Return True if no more things to solve.
    def solve_Triangle(self):
        #put in a bunch of if cases using temporary variables
        tV1 = self.List["v1"]
        tV2 = self.List["v2"]
        tV3 = self.List["v3"]
        tA1 = self.List["a1"]
        tA2 = self.List["a2"]
        tA3 = self.List["a3"]
        tE1 = self.List["e1"]
        tE2 = self.List["e2"]
        tE3 = self.List["e3"]
        tI1 = self.i1
        tI2 = self.i2
        tC1 = self.c1
        tC2 = self.c2
        #check for current errors
        #check if the angles add up
        #https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        #handles an arbitrarily number of arguments to be passed to the constructor.
        try:
            if(tA1 != None and tA2 != None and tA3 != None):
                tSum = tA1+tA2+tA3
                if(tSum != 180):
                    raise ArithmeticError("Warning: Triangle MIGHT NOT add up to 180 degrees.") 
        except ArithmeticError as err:
            print(err.args)
            return True

        #Using my geometry knowledge.. Solve for all unknowns!
        #https://math.stackexchange.com/questions/187107/calculate-coordinates-of-3rd-point-vertex-of-a-scalene-triangle-if-angles-and
        #for vertices
        if(tV1 == None):
            #calculate based on other two vertices
            if (isinstance(tV2, Point2D) and isinstance(tV3,Point2D) and
                tE3 != None and tE2 != None and tE1 != None):
                #print("attempting to calculate based on other 2 vertices")
                #intersecting circles method. We just need tE2 and tE3 as the radius of the circle
                c1 = Circle(tV2, tE3)
                c2 = Circle(tV3, tE2)
                iList = c1.intersection(c2)
                tV1 = iList[1]
                self.List["v1"] = tV1
                return False
            #calculate based on 1 vertex (the other must be missing)
            elif (isinstance(tV2, Point2D) and not (isinstance(tV3,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV2.x - listVertices[0].x 
                offsetY = tV2.y - listVertices[0].y 
                tV1 = listVertices[2].translate(offsetX,offsetY)
                tV3 = listVertices[1].translate(offsetX,offsetY)
                self.List["v1"] = tV1
                self.List["v3"] = tV3
                return False
            elif (isinstance(tV3, Point2D) and not (isinstance(tV2,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV3.x - listVertices[1].x 
                offsetY = tV3.y - listVertices[1].y 
                tV1 = listVertices[2].translate(offsetX,offsetY)
                tV2 = listVertices[0].translate(offsetX,offsetY)
                self.List["v1"] = tV1
                self.List["v2"] = tV2
                return False
                
        if(tV2 == None):
            if (isinstance(tV1, Point2D) and isinstance(tV3,Point2D) and
                tE3 != None and tE2 != None and tE1 != None):
                #print("attempting to calculate based on other 2 vertices")
                c1 = Circle(tV1, tE3)
                c2 = Circle(tV3, tE1)
                iList = c1.intersection(c2)
                tV2 = iList[0]
                self.List["v2"] = tV2
                return False
            #calculate based on 1 vertex (the other must be missing)
            elif (isinstance(tV1, Point2D) and not (isinstance(tV3,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV1.x - listVertices[2].x 
                offsetY = tV1.y - listVertices[2].y 
                tV2 = listVertices[0].translate(offsetX,offsetY)
                tV3 = listVertices[1].translate(offsetX,offsetY)
                self.List["v2"] = tV2
                self.List["v3"] = tV3
                return False
            elif (isinstance(tV3, Point2D) and not (isinstance(tV1,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV3.x - listVertices[1].x 
                offsetY = tV3.y - listVertices[1].y 
                tV2 = listVertices[0].translate(offsetX,offsetY)
                tV1 = listVertices[1].translate(offsetX,offsetY)
                self.List["v1"] = tV1
                self.List["v2"] = tV2
                return False

        if(tV3 == None):
            if (isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and
                tE3 != None and tE2 != None and tE1 != None):
                #print("attempting to calculate based on other 2 vertices")
                c1 = Circle(tV1, tE2)
                c2 = Circle(tV2, tE1)
                iList = c1.intersection(c2)
                tV3 = iList[1]
                self.List["v3"] = tV3
                return False
            #calculate based on 1 vertex (the other must be missing)
            elif (isinstance(tV1, Point2D) and not (isinstance(tV2,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV1.x - listVertices[2].x 
                offsetY = tV1.y - listVertices[2].y 
                tV2 = listVertices[0].translate(offsetX,offsetY)
                tV3 = listVertices[1].translate(offsetX,offsetY)
                self.List["v2"] = tV2
                self.List["v3"] = tV3
                return False
            elif (isinstance(tV2, Point2D) and not (isinstance(tV1,Point2D)) and
                tE3 != None and tE2 != None and tE1 != None):
                tTri = Triangle(sss=(tE1,tE2,tE3))
                listVertices = tTri.vertices
                offsetX = tV2.x - listVertices[0].x 
                offsetY = tV2.y - listVertices[0].y 
                tV3 = listVertices[1].translate(offsetX,offsetY)
                tV1 = listVertices[2].translate(offsetX,offsetY)
                self.List["v3"] = tV3
                self.List["v1"] = tV1
                return False

        if(tA1 == None):
            if( tA2 != None and tA3 != None):
                #use the other two angles, requires a2, a3
                tA1 = 180-tA2-tA3
                self.List["a1"] = tA1
                return False
            elif(tE3 != None and tA2 != None and tE1 != None):
                #sas triangle using e3, a2, e1.
                tTri = Triangle(sas=(tE3,tA2,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE2 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a3"] = round(tA3,2)
                self.List["e2"] = round(tE2,2)
                return False
            elif(tE2 != None and tA3 != None and tE1 != None):
                #sas triangle using e2, a3, e1.
                tTri = Triangle(sas=(tE2,tA3,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE3 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["e3"] = round(tE3,2)
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False

        if(tA2 == None):
            if( tA1 != None and tA3 != None):
                #use the other two angles, requires a1, a3
                tA2 = 180-tA1-tA3
                self.List["a2"] = tA2
                return False
            elif(tE3 != None and tA1 != None and tE2 != None):
                #sas triangle using e3, a1, e2.
                tTri = Triangle(sas=(tE3,tA1,tE2))
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                return False
            elif(tE2 != None and tA3 != None and tE1 != None):
                #sas triangle using e2, a3, e1.
                tTri = Triangle(sas=(tE2,tA3,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE3 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["e3"] = round(tE3,2)
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False
        if(tA3 == None):
            if( tA1 != None and tA2 != None):
                #use the other two angles, requires a1, a2
                tA3 = 180-tA1-tA2
                self.List["a3"] = tA3
                return False
            elif(tE3 != None and tA1 != None and tE2 != None):
                #sas triangle using e3, a1, e2.
                tTri = Triangle(sas=(tE3,tA1,tE2))
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                return False
            elif(tE3 != None and tA2 != None and tE1 != None):
                #sas triangle using e3, a2, e1.
                tTri = Triangle(sas=(tE3,tA2,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE2 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a3"] = round(tA3,2)
                self.List["e2"] = round(tE2,2)
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False
        if(tE1 == None):
            #asa triangle a2, e3, a1
            if(tA2 != None and tE3 != None and tA1 != None):
                tTri = Triangle(asa=(tA2,tE3,tA1))
                tE2 = self.toFloat(tTri.sides[1].length)
                tE1 = self.toFloat(tTri.sides[2].length)
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e2"] = round(tE2,2)
                self.List["e1"] = round(tE1,2)
                self.List["a3"] = round(tA3,2)
                return False
            #asa triangle a1, e2, a3
            if(tA1 != None and tE2 != None and tA3 != None):
                tTri = Triangle(asa=(tA1,tE2,tA3))
                tE3 = self.toFloat(tTri.sides[2].length)
                tE1 = self.toFloat(tTri.sides[1].length)
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e3"] = round(tE3,2)
                self.List["e1"] = round(tE1,2)
                self.List["a2"] = round(tA2,2)
                return False
            #sas triangle e3, a1, e2
            if(tE3 != None and tA1 != None and tE2 != None):
                tTri = Triangle(sas=(tE3,tA1,tE2))
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                return False
            #vertices v2 and v3 are established
            if(isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                tE1 = self.toFloat(tV2.distance(tV3))
                self.List["e1"] = round(tE1,2)
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False

        if(tE2 == None):
            #sas triangle e3, a2, e1
            if(tE3 != None and tA2 != None and tE1 != None):
                #sas triangle using e3, a2, e1.
                tTri = Triangle(sas=(tE3,tA2,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE2 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a3"] = round(tA3,2)
                self.List["e2"] = round(tE2,2)
                return False
            #asa triangle a2, e1, a3
            elif(tA2 != None and tE1 != None and tA3 != None):
                tTri = Triangle(asa=(tA2,tE1,tA3))
                tE2 = self.toFloat(tTri.sides[1].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                self.List["a1"] = round(tA1,2)
                return False
            #asa triangle a2, e3, a1
            elif(tA2 != None and tE3 != None and tA1 != None):
                tTri = Triangle(asa=(tA2,tE3,tA1))
                tE2 = self.toFloat(tTri.sides[1].length)
                tE1 = self.toFloat(tTri.sides[2].length)
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e2"] = round(tE2,2)
                self.List["e1"] = round(tE1,2)
                self.List["a3"] = round(tA3,2)
                return False
            #vertices v1 and v3 are established
            if(isinstance(tV1,Point2D) and isinstance(tV3,Point2D)):
                tE2 = self.toFloat(tV1.distance(tV3))
                self.List["e2"] = round(tE2,2)
                print("Edge")
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False
        if(tE3 == None):
            #asa triangle a1, e2, a3
            if(tA1 != None and tE2 != None and tA3 != None):
                tTri = Triangle(asa=(tA1,tE2,tA3))
                tE3 = self.toFloat(tTri.sides[2].length)
                tE1 = self.toFloat(tTri.sides[1].length)
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e3"] = round(tE3,2)
                self.List["e1"] = round(tE1,2)
                self.List["a2"] = round(tA2,2)
                return False
            #asa triangle a2, e1, a3
            elif(tA2 != None and tE1 != None and tA3 != None):
                tTri = Triangle(asa=(tA2,tE1,tA3))
                tE2 = self.toFloat(tTri.sides[1].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                self.List["a1"] = round(tA1,2)
                return False
            #sas triangle e2, a3, e1
            elif(tE2 != None and tA3 != None and tE1 != None):
                #sas triangle using e2, a3, e1.
                tTri = Triangle(sas=(tE2,tA3,tE1))
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE3 = self.toFloat(tTri.sides[1].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["e3"] = round(tE3,2)
                return False
            #Vertices v1, v2 are established
            if(isinstance(tV1,Point2D) and isinstance(tV2,Point2D)):
                tE3 = self.toFloat(tV1.distance(tV2))
                self.List["e3"] = round(tE3,2)
                return False
            elif(isinstance(tV1, Point2D) and isinstance(tV2,Point2D) and isinstance(tV3,Point2D)):
                #all three vertices are established.
                tTri = Triangle(tV1,tV2,tV3)
                tA1 = self.toDegrees(tTri.angles[tTri.vertices[0]])
                tA2 = self.toDegrees(tTri.angles[tTri.vertices[2]])
                tA3 = self.toDegrees(tTri.angles[tTri.vertices[1]])
                tE1 = self.toFloat(tTri.sides[1].length)
                tE2 = self.toFloat(tTri.sides[0].length)
                tE3 = self.toFloat(tTri.sides[2].length)
                self.List["a1"] = round(tA1,2)
                self.List["a2"] = round(tA2,2)
                self.List["a3"] = round(tA3,2)
                self.List["e1"] = round(tE1,2)
                self.List["e2"] = round(tE2,2)
                self.List["e3"] = round(tE3,2)
                return False
        #if no vertices are specified. Set V2 as an anchor (0,0)
        if(not isinstance(tV1, Point2D) and not isinstance(tV2,Point2D) and not isinstance(tV3,Point2D)):
            self.List["v2"] = Point(0,0)
            #print("No vertex detected. Anchoring v2 at (0,0)...")
            return False

        return True #return True if no more things to solve

    #attempt to solve circle. Make sure the triangle exists first.
    def solve_Circle(self):
        if(self.List["v1"]==None or self.List["v2"]==None or self.List["v3"]==None):
            #print("hi (vertices are not set)")
            return
        #print("hi2 (vertices are set) ")
        tCenter = self.List["center"]
        tRadius = self.List["radius"]
        #user enters both center and a radius
        if((tRadius != None) and (isinstance(tCenter, Point2D))):
            tCircle = Circle(tCenter, tRadius)
            #print("TempCircle Created")
            #good circle, keep
            if(self.checkCircle(tCircle)):
                pass
            #bad circle. Have the user re-enter everything
            else:
                tCenter = None
                tRadius = None
                self.List["center"] = tCenter
                self.List["radius"] = tRadius
                print("Bad Circle. Try another circle? (Or try entering just radius)...")
                return True
        #User enters a radius but not center. Solve for center. It tries once to find center.
        elif((self.List["radius"] != None) and (not isinstance(tCenter, Point2D))):
            #defaulted to the right of e2
            #print("Setting position for circle...")
            tV1 = self.List["v1"]
            tV3 = self.List["v3"]
            tSegment2 = Segment(tV1,tV3)
            tMidpoint = tSegment2.midpoint
            shift = self.List["radius"]/3.0
            tRadius2 = self.List["radius"]
            tCenter2 = tMidpoint.translate(shift)
            rxCenter2 = round(tCenter2.x, 2)
            ryCenter2 = round(tCenter2.y, 2)
            tCenter2 = Point(rxCenter2,ryCenter2)
            self.set_vertex("center", rxCenter2, ryCenter2)
            tCircle2 = Circle(tCenter2, tRadius2)
            #print("CHECKING TEMP CIRCLE CREATED WITH JUST RADIUS", tCircle2)
            if(self.checkCircle(tCircle2)==False):
                print("Can not find a suitable center for the circle.")
                self.List["center"] = None
                return True
            
        #User enters a center, but not radius. Solve for radius WILL NOT IMPLEMENT
        return True

    #passes True if its a good circle that intersects a side twice. False if it's not. 
    #c is circle object
    def checkCircle(self, c):
        #print("Checking created circle...")
        tCenter = c.center
        tRadius = c.radius
        tV1 = self.List["v1"]
        tV2 = self.List["v2"]
        tV3 = self.List["v3"]
        tSegment = None
        tSegment2 = None
        tSegment3 = None
        if (isinstance(tV1, Point2D) and isinstance(tV2, Point2D) and isinstance(tV3, Point2D)):
            tSegment = Segment(tV1, tV3)
            tSegment2 = Segment(tV1, tV2)
            tSegment3 = Segment(tV2, tV3)
        else: 
            return False
        #print("Segments created. ", tSegment, "\n", tSegment2, "\n", tSegment3)
        #user enters both center and a radius
        if((tRadius != None) and (isinstance(tCenter, Point2D))):
            tCircle = Circle(tCenter, tRadius)
            #tList = tCircle.intersection(tSegment)
            tList = intersection(tSegment, tCircle)
            tList1 = intersection(tSegment2, tCircle)
            tList2 = intersection(tSegment3, tCircle)
            #print("Actually checking circle", tCircle, tSegment, tSegment2, tSegment3)
            #good circle, keep
            if((len(tList)==2 and len(tList1)==0 and len(tList2)==0 ) or 
                (len(tList)==0 and len(tList1)==2 and len(tList2)==0 ) or
                (len(tList)==0 and len(tList1)==0 and len(tList2)==2 )):
                if(len(tList)==2):
                    #print(tList)
                    #print(tList[0].evalf(), tList[1].evalf())
                    #print("good circle! Intersects side e2...")
                    self.i1 = tList[0]
                    self.i2 = tList[1]
                    #print(self.i1.evalf(), self.i2.evalf())
                elif(len(tList1)==2):
                    self.i1 = tList1[0]
                    self.i2 = tList1[1]
                    #print(self.i1.evalf(), self.i2.evalf())
                    #print("good circle! Intersects side e3...")
                elif(len(tList2)==2):
                    self.i1 = tList2[0]
                    self.i2 = tList2[1]
                    #print(self.i1.evalf(), self.i2.evalf())
                    #print("good circle! Intersects side e1...")
                return True
            else:
                print("Error. Not enough or too many intersection points.")
                return False
        print("Fatal Error: Center and radius not entered")
        return False

    def toDegrees(self, x):
        return float(x*180/math.pi)

    def toFloat(self, x):
        x= x/float(1.0)
        return float(x)


        