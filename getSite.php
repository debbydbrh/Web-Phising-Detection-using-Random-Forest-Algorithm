<?php
$URL = "Welcome";
header("Access-Control-Allow-Origin: *");
$URL = $_POST['url'];

$html = file_get_contents($URL);

$bytes = file_put_contents('file.txt', $html);

$website = exec('/ProgramData/Anaconda3/python test.py '.$URL.' 2>$1 ');


echo $website;
?>