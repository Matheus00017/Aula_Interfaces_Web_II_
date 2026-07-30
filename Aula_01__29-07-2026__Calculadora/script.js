function calcular(operador) {
    const numero1 = Number(document.getElementById("numero1").value);
    const numero2 = Number(document.getElementById("numero2").value);

    let Resultado;

    if (operador === "+") {
        Resultado = numero1 + numero2;
    }else if (operador === "-") {
        Resultado = numero1 - numero2
    }else if (operador === "*") {
        Resultado = numero1 * numero2
    }else if (operador === "/") {
        if (numero2 === 0){
            document.getElementById("resultado").innerHTML = "Erro: divisão por zero!";
            return;
        }
        Resultado = numero1 / numero2;
    }

    document.getElementById("Resultado").innerText = "Resultado " + Resultado;
}
