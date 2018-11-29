import cgi
from sympy.geometry import*
from sympy.core.sympify import sympify
import math

steveniscool = Triangle(sss=(3,4,5))
someint = 5

print("Content-Type: text/html")
print()
print("<html>")

#header
print("""
<title>CGI script output</title>
<h1>This is my first CGI script</h1>
 """)
#reload page button
print("""
<center>
<input type="button" value="Refresh Page" onClick="window.location.href=window.location.href">
</center>
""")
#some line of text
print("Hello, worldsa!")
print("Triangle is", steveniscool, sep='')
print("god dam it")

#example forms
print("""<br>
<form method ="post">
    first name: <input type ="text" name="firstname">
    <br>
    last name: <input type ="text" name="lastname">
    <br>
    <input type ="submit" value ="Submit" name="SubmitButton1">
    </form> """)
print("<br>")
print("<br>")
form = cgi.FieldStorage()
print(form)
print("<br>")
print("<br>")
check =  form.getlist("SubmitButton1")
print(check)
print("<br>")
print("<br>")
#check if submit button was pressed
if(len(check) == 1):
    print("u clicked submit")
    print("<br>")
    if((len(form.getlist("firstname")) == 1) and 
        (len(form.getlist("lastname")) == 1)):
        print("First name: ", form.getlist("firstname")[0])
        print("<br>")
        print("Last name: ", form.getlist("lastname")[0])
    else:
        print("please fill in a first and last name")



#end of file
print("</html>")