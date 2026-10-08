<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de produtos</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Lista de produtos</h1>
        <table>
            <tr>
                <th>Nome</th>
                <th>Preço</th>
                <th>Estoque</th>
            </tr>

            <?php
                $produtos = [
                    ["nome" => "Produto A", "preco" => 50.00, "estoque" => 10],
                    ["nome" => "Produto B", "preco" => 30.00, "estoque" => 5],
                    ["nome" => "Produto C", "preco" => 75.00, "estoque" => 20],
                    
                ];

                foreach ($produtos as $produto) {
                    echo "<tr>";
                    echo "<td>" . $produto["nome"] . "</td>";
                    echo "<td>R$ ". number_format($produto["preco"], 2, ',', '.' ) . "</td>";
                    echo "<td>" . $produto["estoque"] . "</td>";
                    echo "</tr>";




                }
            ?>
        </table>
    </div>
</body>
</html>