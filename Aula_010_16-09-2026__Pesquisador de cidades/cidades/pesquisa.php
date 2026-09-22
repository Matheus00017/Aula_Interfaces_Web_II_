<?php
include ("conn.php");

$estado = $_POST["estado"];
$cidade = $_POST["cidade"];

$sql = "select c.nome as cidade, e.nome as estado 
        from cidade c, estado e 
        where c.codigo_estado = e.codigo_estado
        and e.nome like '%$estado%'
        and c.nome like '%$cidade%'";

$resultado = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Resultado da pesquisa</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="caixa">
    <h2>Resultado da pesquisa</h2>
    <a href="index.html">Nova pesquisa</a>
    </div>

    <table>
        <tr>
            <th>Cidade</th>
            <th>Estado</th>
        </tr>

        <?php
        if($resultado ->num_rows > 0){
            while ($row = $resultado->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row["cidade"] . "</td>";
                echo "<td>" . $row["estado"] . "</td>";
                echo "</tr>";
            } 
        } else {
            echo "<tr><td colspan='2'>Nenhum Resultado encontado</td></tr>";
        }
        ?>
    </table>
</body>
</html>