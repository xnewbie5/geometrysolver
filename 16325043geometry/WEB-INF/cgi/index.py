# WEBSITE FOR GEOMETRY SOLVER
# Gerry Su #16325043
# November 29, 2018
# EECS 118
import cgi, cgitb
from problem1 import*
from problem2 import*
from problem3 import*
from sympy.geometry import*
from sympy.core.sympify import sympify
import math

print("<!DOCTYPE html>")
print("Content-Type: text/html")
print()

#set table styles
print("""
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
""")
print("<html>")
#title
print("<title>Geometry Solver 16325043</title>")
#meta
print("""
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
""")
#Page Header
print("""
<h2><center> Geometry Solver</center></h2>
<h3><center> Term Project by Gerry Su #16325043</center></h3>
""")
#reload page button
print("""
<center>
<input type="button" value="Main Menu" onClick="window.location.href=window.location.href">
</center>
""")
#Problem selection form. Show only if the selection hasn't been pressed.
#create instance of FieldStorage
form = cgi.FieldStorage()
#print(form, "<br>")
if(form.getvalue("submitButton") == None):
    print("""
    <form NAME=problemselect method=POST> 

    <Table>
        <tr>
            <th>Problem 1</th>
            <th>Problem 2</th>
            <th>Problem 3</th>
        </tr>
        <tr>
            <td><img src="../problem1.png" alt="Problem 1" width="500"></td>
            <td><img src="../problem2.png" alt="Problem 2" width="500"></td>
            <td><img src="../problem3.png" alt="Problem 3" width="500"></td>
        </tr>
        <tr>
            <td align="center"><input type=radio name=selection value="1"></td>
            <td align="center"><input type=radio name=selection value="2"></td>
            <td align="center"><input type=radio name=selection value="3"></td>
        </tr>
        <tr>
            <td></td>
            <td align="center"><input type="submit" name=submitButton value="Select"> </td>
            <td></td>
        </tr>
    </Table>

    </form>
    """)
#INPUT PROCESSING
#select button is pressed
if(form.getvalue("submitButton")!= None):
    #check which problem selected and create appropriate forms.
    check =  form.getvalue("selection")
    if(check == "1"):
        print("You selected Problem 1 <br>")
        print("""
        <img src="../problem1.png" alt="Problem 1" width="500">
        <form NAME=Problem1Form method=POST>
        v1 X: <input type ="text" name="v1X" value="" size="3"> 
        v1 Y: <input type ="text" name="v1Y" value="" size="3"> <br>
        v2 X: <input type ="text" name="v2X" value="" size="3">
        v2 Y: <input type ="text" name="v2Y" value="" size="3"> <br>
        v3 X: <input type ="text" name="v3X" value="" size="3">
        v3 Y: <input type ="text" name="v3Y" value = "" size="3"> <br>
        a1 (degrees): <input type ="text" name="a1" value = ""> <br>
        a2 (degrees): <input type ="text" name="a2" value = ""> <br>
        a3 (degrees): <input type ="text" name="a3" value = ""> <br>
        e1: <input type ="text" name="e1" value = "5"> <br>
        e2: <input type ="text" name="e2" value = "4"> <br>
        e3: <input type ="text" name="e3" value = "3"> <br>
        Circle Center X: <input type ="text" name="cX" value = "4"> <br>
        Circle Center Y: <input type ="text" name="cY" value = "1.2"> <br>
        Circle Radius: <input type ="text" name="radius" value = "0.6"> <br>
        <input type="hidden" name=submitButton value="Select"> 
        <input type="submit" name=SubmitProblem1 value="Solve">
         """)
    elif(check == "2"):
        print("You selected Problem 2 <br>")
        print("""
        <img src="../problem2.png" alt="Problem 2" width="500">
        <form NAME=Problem2Form method=POST>
        v1 X: <input type ="text" name="v1X" value="1.8" size="3"> 
        v1 Y: <input type ="text" name="v1Y" value="2.4" size="3"> <br>
        v2 X: <input type ="text" name="v2X" value="0" size="3">
        v2 Y: <input type ="text" name="v2Y" value="0" size="3"> <br>
        v3 X: <input type ="text" name="v3X" value="5" size="3">
        v3 Y: <input type ="text" name="v3Y" value = "0" size="3"> <br>
        a1 (degrees): <input type ="text" name="a1" value = ""> <br>
        a2 (degrees): <input type ="text" name="a2" value = ""> <br>
        a3 (degrees): <input type ="text" name="a3" value = ""> <br>
        e1: <input type ="text" name="e1" value = ""> <br>
        e2: <input type ="text" name="e2" value = ""> <br>
        e3: <input type ="text" name="e3" value = ""> <br>
        Circle Center X: <input type ="text" name="cX" value = "4"> <br>
        Circle Center Y: <input type ="text" name="cY" value = "0.6"> <br>
        Circle Radius: <input type ="text" name="radius" value = "0.6"> <br>
        <input type="hidden" name=submitButton value="Select"> 
        <input type="submit" name=SubmitProblem2 value="Solve">
         """)
    elif(check == "3"):
        print("You selected Problem 3 <br>")
        print("""
        <img src="../problem3.png" alt="Problem 3" width="500">
        <form NAME=Problem2Form method=POST>
        v1 X: <input type ="text" name="v1X" value="1.8" size="3"> 
        v1 Y: <input type ="text" name="v1Y" value="2.4" size="3"> <br>
        v2 X: <input type ="text" name="v2X" value="0" size="3">
        v2 Y: <input type ="text" name="v2Y" value="0" size="3"> <br>
        v3 X: <input type ="text" name="v3X" value="5" size="3">
        v3 Y: <input type ="text" name="v3Y" value = "0" size="3"> <br>
        v4 X: <input type ="text" name="v4X" value="" size="3">
        v4 Y: <input type ="text" name="v4Y" value = "" size="3"> <br>
        a1 (degrees): <input type ="text" name="a1" value = ""> <br>
        a2 (degrees): <input type ="text" name="a2" value = ""> <br>
        a3 (degrees): <input type ="text" name="a3" value = ""> <br>
        a4 (degrees): <input type ="text" name="a4" value = ""> <br>
        a5 (degrees): <input type ="text" name="a5" value = ""> <br>
        a6 (degrees): <input type ="text" name="a6" value = ""> <br>
        e1: <input type ="text" name="e1" value = ""> <br>
        e2: <input type ="text" name="e2" value = ""> <br>
        e3: <input type ="text" name="e3" value = ""> <br>
        e4: <input type ="text" name="e4" value = "3"> <br>
        e5: <input type ="text" name="e5" value = "4"> <br>
        <input type="hidden" name=submitButton value="Select"> 
        <input type="submit" name=SubmitProblem3 value="Solve">
         """)
#Solve problem 1 and output everything.
if(form.getvalue("SubmitProblem1")!= None):
    print("""
    <img src="../problem1.png" alt="Problem 1" width="500"> <br>
    """)
    p1 = problem1()
    #print(form.keys(), "<br>")
    for key in form.keys():
        if key == "v1X":
            p1.set_vertex("v1", sympify(form.getvalue("v1X"), rational=True), sympify(form.getvalue("v1Y"), rational=True))
        if key == "v2X":
            p1.set_vertex("v2", sympify(form.getvalue("v2X"), rational=True), sympify(form.getvalue("v2Y"), rational=True))
        if key == "v3X":
            p1.set_vertex("v3", sympify(form.getvalue("v3X"), rational=True), sympify(form.getvalue("v3Y"), rational=True))
        if key == "a1":
            p1.set_value("a1", sympify(form.getvalue("a1"), rational=True))
        if key == "a2":
            p1.set_value("a2", sympify(form.getvalue("a2"), rational=True))
        if key == "a3":
            p1.set_value("a3", sympify(form.getvalue("a3"), rational=True))
        if key == "e1":
            p1.set_value("e1", sympify(form.getvalue("e1"), rational=True))
        if key == "e2":
            p1.set_value("e2", sympify(form.getvalue("e2"), rational=True))
        if key == "e3":
            p1.set_value("e3", sympify(form.getvalue("e3"), rational=True))
        if key == "radius":
            p1.set_value("radius", sympify(form.getvalue("radius"), rational=True))
        if key == "cX":
            p1.set_vertex("center", sympify(form.getvalue("cX"), rational=True), sympify(form.getvalue("cY"), rational=True))
    print("<br>Values before: <br>")
    for i in p1.List:
        if(isinstance(p1.List[i], Point2D)):
            print(i,"=", p1.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p1.List[i])
            print("<br>")
    #print(p1.get_all(), "<br>")
    p1.solve_looping()
    print("<br><b>Values after: <br>")
    #print(p1.get_all(), "<br>")
    for i in p1.List:
        if(isinstance(p1.List[i], Point2D)):
            print(i,"=", p1.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p1.List[i])
            print("<br>")
    print("<br>Extra Variables:")
    p1.print_extra_variables_website()
    print("</b>")
elif(form.getvalue("SubmitProblem2")!=None):
    print("""
    <img src="../problem2.png" alt="Problem 2" width="500"> <br>
    """)
    p2 = problem2()
    #print(form.keys(), "<br>")
    for key in form.keys():
        if key == "v1X":
            p2.set_vertex("v1", sympify(form.getvalue("v1X"), rational=True), sympify(form.getvalue("v1Y"), rational=True))
        if key == "v2X":
            p2.set_vertex("v2", sympify(form.getvalue("v2X"), rational=True), sympify(form.getvalue("v2Y"), rational=True))
        if key == "v3X":
            p2.set_vertex("v3", sympify(form.getvalue("v3X"), rational=True), sympify(form.getvalue("v3Y"), rational=True))
        if key == "a1":
            p2.set_value("a1", sympify(form.getvalue("a1"), rational=True))
        if key == "a2":
            p2.set_value("a2", sympify(form.getvalue("a2"), rational=True))
        if key == "a3":
            p2.set_value("a3", sympify(form.getvalue("a3"), rational=True))
        if key == "e1":
            p2.set_value("e1", sympify(form.getvalue("e1"), rational=True))
        if key == "e2":
            p2.set_value("e2", sympify(form.getvalue("e2"), rational=True))
        if key == "e3":
            p2.set_value("e3", sympify(form.getvalue("e3"), rational=True))
        if key == "radius":
            p2.set_value("radius", sympify(form.getvalue("radius"), rational=True))
        if key == "cX":
            p2.set_vertex("center", sympify(form.getvalue("cX"), rational=True), sympify(form.getvalue("cY"), rational=True))
    print("<br>Values before: <br>")
    for i in p2.List:
        if(isinstance(p2.List[i], Point2D)):
            print(i,"=", p2.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p2.List[i])
            print("<br>")
    #print(p1.get_all(), "<br>")
    p2.solve_looping()
    print("<br><b>Values after: <br>")
    #print(p1.get_all(), "<br>")
    for i in p2.List:
        if(isinstance(p2.List[i], Point2D)):
            print(i,"=", p2.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p2.List[i])
            print("<br>")
    print("<br>Extra Variables:")
    p2.print_extra_variables_website()
    print("</b>")
elif(form.getvalue("SubmitProblem3")!=None):
    print("""
    <img src="../problem3.png" alt="Problem 3" width="500"> <br>
    """)
    p3 = problem3()
    #print(form.keys(), "<br>")
    for key in form.keys():
        if key == "v1X":
            p3.set_vertex("v1", sympify(form.getvalue("v1X"), rational=True), sympify(form.getvalue("v1Y"), rational=True))
        if key == "v2X":
            p3.set_vertex("v2", sympify(form.getvalue("v2X"), rational=True), sympify(form.getvalue("v2Y"), rational=True))
        if key == "v3X":
            p3.set_vertex("v3", sympify(form.getvalue("v3X"), rational=True), sympify(form.getvalue("v3Y"), rational=True))
        if key == "v3X":
            p3.set_vertex("v4", sympify(form.getvalue("v4X"), rational=True), sympify(form.getvalue("v4Y"), rational=True))
        if key == "a1":
            p3.set_value("a1", sympify(form.getvalue("a1"), rational=True))
        if key == "a2":
            p3.set_value("a2", sympify(form.getvalue("a2"), rational=True))
        if key == "a3":
            p3.set_value("a3", sympify(form.getvalue("a3"), rational=True))
        if key == "a4":
            p3.set_value("a4", sympify(form.getvalue("a4"), rational=True))
        if key == "a5":
            p3.set_value("a5", sympify(form.getvalue("a5"), rational=True))
        if key == "a6":
            p3.set_value("a6", sympify(form.getvalue("a6"), rational=True))
        if key == "e1":
            p3.set_value("e1", sympify(form.getvalue("e1"), rational=True))
        if key == "e2":
            p3.set_value("e2", sympify(form.getvalue("e2"), rational=True))
        if key == "e3":
            p3.set_value("e3", sympify(form.getvalue("e3"), rational=True))
        if key == "e4":
            p3.set_value("e4", sympify(form.getvalue("e4"), rational=True))
        if key == "e5":
            p3.set_value("e5", sympify(form.getvalue("e5"), rational=True))
    print("<br>Values before: <br>")
    for i in p3.List:
        if(isinstance(p3.List[i], Point2D)):
            print(i,"=", p3.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p3.List[i])
            print("<br>")
    #print(p1.get_all(), "<br>")
    p3.solve_looping()
    print("<br><b>Values after: <br>")
    #print(p1.get_all(), "<br>")
    for i in p3.List:
        if(isinstance(p3.List[i], Point2D)):
            print(i,"=", p3.List[i].evalf())
            print("<br>")
        else:
            print(i,"=",p3.List[i])
            print("<br>")
    print("<br>Extra Variables:")
    p3.print_extra_variables_website()
    print("</b>")
             
    
    

print("</html>")