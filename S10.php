<?php

function mod($x,$y)
{
   $z=$x%$y;
echo "mod value of $x & $y is $z<br>";
  }
function power($x, $y) 
{
  $f= 1;
  $n1 = $y;
  while($n1 > 0)
{
    $f= $f * $x;
    $n1--;
  }
  echo "$x raised to the power $y = $f <br>";
}
function sum($x)
{
   $sum=0;
   $i=1;
  while($i<=$x)
   {
    $sum=$sum+$i;
    $i++;
    }
  echo "sumof first $x number is $sum<br>"; 
}
function fact($y)
  {
    $i=1;$f=1;
  while($i<=$y)
    {
    
      $f=$f*$i;
   $i++;
   }
echo "factorial of $y is $f";
  
 }

$x=$_POST['t1'];
$y=$_POST['t2'];
mod($x,$y);
 power($x,$y);
sum($x);
fact($y);
?> 