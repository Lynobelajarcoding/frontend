<?php 
$judul = $_POST['title'];
$isi =  $_POST['content'];

$json = ['judul'=>$judul, 'isi'=>$isi];
echo  json_encode($json);
?>