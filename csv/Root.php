<?php
header('Content-type: application/json');

 $newArray = array("http://train.byethost7.com/api/CalendarTren.php",
                "http://train.byethost7.com/api/ElementTrasa.php",
                "http://train.byethost7.com/api/Modificari.php",
                "http://train.byethost7.com/api/ModificariInParcurs.php",
                "http://train.byethost7.com/api/RestrictiiTren.php",
                "http://train.byethost7.com/api/Trasa.php",
                "http://train.byethost7.com/api/Trase.php",
                "http://train.byethost7.com/api/Tren.php",
           );
echo json_encode($newArray);

?>