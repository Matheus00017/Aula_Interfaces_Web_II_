<?php
$conn = new mysqli("localhost", "root", "", "cidades_brasil");

if($conn -> connect_error) {
    die("Erro na conexão");
}
?>