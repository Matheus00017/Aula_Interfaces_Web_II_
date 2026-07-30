function converter(tipo) {
    const temperatura = Number(document.getElementById("temperatura").value);

    let resultado;

    if (tipo === "paraFahrenheit") {
        resultado = temperatura * 9 / 5 + 32;
        document.getElementById("resultado").innerText = "resultado: " + resultado.toFixed(1) + " °F ";

    } else if (tipo === "paraCelsius") {
        resultado = (temperatura - 32) * 5 / 9;
        document.getElementById("resultado").innerText = "resultado: " + resultado.toFixed(1) + " °c ";
    }
}