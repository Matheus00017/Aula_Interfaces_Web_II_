<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data e Hora Atual</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Data e Hora Atual</h1>
        <p><?php date_default_timezone_set('America/Sao_Paulo');
        echo date("d/m/y H:i:s") ?></p>
    </div>
</body>
</html>