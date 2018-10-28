from sympy.geometry import*

def main():
    print("hello world")
    x = input("Enter x coord: ")
    y = 50
    r = 100

    c1 = Circle(Point(x,y), r)
    print("radius is ", c1.radius)
    print("Area is ",float (c1.area))

if __name__ == "__main__":
    main()