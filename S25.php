<?php
$file=$_POST['file'];
$c=$_POST['b'];
switch($c)

    {

	case 1 :
                        $t=filetype($file);
		      echo "type of file is :$t";
                         break;	

	case 2:

		$a=fileatime($file);
		echo "last accessed time of file  is :$a<br>";
		echo "Last access time".date("F d Y H:i:s.",fileatime($file));
		break;
	case 3:

		$size=filesize($file);
		echo "the size of file is:$size";
			break;
	case 4:

                       if(unlink($file))
                      echo "file is deletd";		
                      else
                      echo "file not deleted";
        

      default:"invalid choice";

}

?>	