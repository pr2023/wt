<?php
if(file_exists("stud.dat"))
{
  $fp1=fopen("stud.dat","r"); 
  $buf1=fread($fp1,filesize("stud.dat"));
  $temprecs=explode("\n",$buf1);
  $i=0;
   foreach($temprecs as $t)
      if(strlen($t)>0)
          $records[$i++]=explode(" ",$t);
          echo"<p>********Student Detalis******</p>";
          echo "<table border=2>";
          echo"<tr><th>rollno</th><th>Name</th><th>OS</th><th>WT</th><th>DS</th><th>Python</th><th>Java</th><th>CN</th><th>ptage</th></tr>";
      foreach($records as $rec)
       {
           echo "<tr>";
           $k=1;
           $tot=0;
            foreach($rec as $f)
              {
                printf("<td>%s</td>",$f);
                $k++; 
                 if($k>3)
                $tot=$tot+$f;
             }
            $ptage=$tot/6.0;
            printf("<th>%.2f</th><br>",$ptage);
      }
     echo"</table>";
     fclose($fp1);
}//if
else
echo "  file not exists";
?>

