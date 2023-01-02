
<?php

  include("seta2_2.php");
$x=$_POST['txt1'];
$y=$_POST['op'];

if($y=="five")
{
      echo implode(' ', array_slice(explode(' ', $x), 0, 5));
   
}

else
 if($y=="convert")
  {
 
    
	echo "lowercase of string".strtolower($x)."<br>";
               echo "upper case of string is".strtoupper($x)."<br>";

  }
else
 if($y=="pad")
  {
 
   $p=str_pad($x,15,"*",STR_PAD_BOTH);
        echo "padded string is".$p."<br>";

  }
else
 if($y=="sp")
  {
 
   echo "after removing white spaces from begining".ltrim($x);

  }
else
 if($y=="rev")
  {
 
  echo "after reverse the string".strrev($x);
  }

  
else
   echo"invalid choice";
?>
