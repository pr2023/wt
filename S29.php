 <?php
$conn=pg_connect("host=localhost port=5433  dbname=ty22 user=postgres password=123456");
if(!$conn)
{

echo("An error.....in connection");
}
else
{
echo("connection succesfull");
echo "<br>";
	  
$ename1=$_POST['txt1'];
$s1="update event,committee,ec set status='working' 
                                    where event.eno=ec.fk_eno and
                                    committee.cno=ec.fk_cno  and etitle='$ename1'";

   $result = pg_query($conn,$s1);
		if (!$result)
		{
			echo"ERROR.....";
			
		}
		else
		{
			  echo "record updated";
		
		}
	   
 	
 }
?>
