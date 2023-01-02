<html lang="en" dir="ltr">
 <head>
 <meta charset="utf-8">
 <title></title>
 </head>
 <body>
 <fieldset>
 <legend><h3>Enter Item Details :</h3></legend>
 <form class="" action="" method="post">
 
 <center>
 <h3>Student Roll No : <input type="text" name="sno" value=""></h3>
 <h3>Student Name : <input type="text" name="sname" value=""></h3>
 <h3>Marsk[ 5 Subject] : <input type="text" name="marks" value="" 
placeholder=" eg. 80,50,70,87,60"></h3>
 <input type="submit" name="submit" value="Submit">
 </center>
 
 </form>
 </fieldset>
 </body>
</html>
<?php
 if(isset($_POST['submit'])){
 $sno = $_POST['sno'];
 $sname = $_POST['sname'];
 $marks = explode(",",$_POST['marks']);
 $total=0;
 $cnt = count($marks);
 for($i=0; $i<$cnt; $i++)
 {
 $total = $total + $marks[$i];
 }
 $per = $total/$cnt;
 if($per>=80){
 $grade='A';
 }
 else if($per>=60){
 $grade = 'B';
 }
 else if($per>=40){
 $grade = "C";
 }
 else {
 $grade = "Fail";
 }
 echo "<table align=center border=1 width='100%'>";
 echo "<tr>
 <th> Roll No </th>
 <th> Name </th>
 <th> Sub1 </th>
 <th> Sub2 </th>
 <th> Sub3 </th>
 <th> Sub4 </th>
 <th> Sub5 </th>
 <th> Total </th>
 <th> Percentage </th>
 <th> Grade </th>
 </tr>";
 echo "<tr>
 <td> $sno </td>
 <td> $sname </td>
 <td> $marks[0] </td>
 <td> $marks[1] </td>
 <td> $marks[2] </td>
 <td> $marks[3] </td>
 <td> $marks[4] </td>
 <td> $total </td>
 <td> $per </td>
 <td> $grade </td>
 </tr>";
 echo "</table>";
 }
?>
