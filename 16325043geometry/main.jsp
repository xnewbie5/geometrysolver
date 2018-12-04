<!-- WEBSITE FOR GEOMETRY SOLVER -->
<!-- Gerry Su #16325043 -->
<!-- November 22, 2018 -->
<!-- EECS 118 -->
<%@ page import="java.util.*"%>
<%@ page import="java.io.*" %>
<!DOCTYPE html>

<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>


<html>
<head>
<title>Geometry Solver 16325043</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<h2><center> Geometry Solver</center></h2>
<h3><center> Term Project by Gerry Su #16325043</center></h3>

 <!-- Reload Page button -->
<center>
<input type="button" value="Refresh Page" onClick="window.location.href=window.location.href">
</center>


<form NAME=problemselect method=POST> 

<Table>
    <tr>
        <th>Problem 1</th>
        <th>Problem 2</th>
        <th>Problem 3</th>
    </tr>
    <tr>
        <td><img src="problem1.png" alt="Problem 1" width="500"></td>
        <td><img src="problem2.png" alt="Problem 2" width="500"></td>
        <td><img src="problem3.png" alt="Problem 3" width="500"></td>
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


</html>
