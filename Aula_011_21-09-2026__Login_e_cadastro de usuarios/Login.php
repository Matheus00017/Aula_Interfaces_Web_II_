<?php
$login = $_POST['login'];
$entrar = $_POST['entrar'];
$senha = md5($_POST['senha']);
$connect = mysqli_connect("localhost", "root", "", "login");
//$db = mysql_select_db('nome_do_banco_de_dados);
if(isset($entrar)) {
    $verificar = mysqli_query($connect, "select * from usuarios where 
    login = '$login' and senha = '$senha'") or die ("erro ao selecionar");
    
    if(mysqli_num_rows($verificar)<=0){
        echo"<script language='javascript' type='text/javascript'>
            alert('Login e/ou senha incorreto!');
            window.location.href='login.html';</script>";
        die();

    }else{
        setcookie("login", $login);
        header("location:http://google.com");
    }
}
?>