document.addEventListener("DOMContentLoaded", function (){
    const container = document.getElementById("produtosContainer");
    const campoBusca = document.getElementById("campoBusca");
    
    function renderizarProdutos(filtro) {
        container.innerHTML = "";

        const filtrados = produtos.filter(produto =>
            produto.nome.toLowerCase().includes(filtro.toLowerCase())
        );

        filtrados.forEach(produto => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
             <img src="${produto.imagem}" alt="Imagem do produto">
             <div class="info">
                <h2>${produto.nome}</h2>
                <p><strong>${produto.preco}</strong></p>
             </div>
            `;

            container.appendChild(card);
        });
    }

    campoBusca.addEventListener("input", () => {
        renderizarProdutos(campoBusca.value);
    });

    renderizarProdutos("");
});