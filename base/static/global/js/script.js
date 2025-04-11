let likes = 0;
let dislikes = 0;

document.addEventListener("DOMContentLoaded", function () {
    const likeBtn = document.getElementById("likeBtn");
    const dislikeBtn = document.getElementById("dislikeBtn");
    const likeCount = document.getElementById("likeCount");
    const dislikeCount = document.getElementById("dislikeCount");
    const comentarioInput = document.getElementById("comentarioInput");
    const listaComentarios = document.getElementById("listaComentarios");

    if (likeBtn && dislikeBtn && likeCount && dislikeCount) {
        likeBtn.addEventListener("click", function () {
            likes++;
            likeCount.innerText = likes;
        });

        dislikeBtn.addEventListener("click", function () {
            dislikes++;
            dislikeCount.innerText = dislikes;
        });
    }

    window.adicionarComentario = function () {
        if (!comentarioInput || comentarioInput.value.trim() === "") return;

        const novoComentario = document.createElement("li");
        novoComentario.classList.add("comment");
        novoComentario.textContent = comentarioInput.value;
        listaComentarios.appendChild(novoComentario);

        comentarioInput.value = "";
    }

    window.toggleMenu = function () {
        const menu = document.getElementById("sideMenu");
        if (menu) {
            menu.classList.toggle("open");
        }
    }
});
window.toggleMenu() {
    var sideMenu = document.getElementById("sideMenu");
    var currentPosition = sideMenu.style.right;
    if (currentPosition === "0px") {
        sideMenu.style.right = "-250px"; // Esconde o menu
    } else {
        sideMenu.style.right = "0"; // Mostra o menu
    }
}
async function converter() {
    const valor = document.getElementById("valor").value;
    const moeda = document.getElementById("moeda").value;
    const resultado = document.getElementById("resultado");

    if (valor === "" || valor <= 0) {
        resultado.innerHTML = "Por favor, insira um valor válido!";
        return;
    }

    try {
        // Buscar as cotações em tempo real
        const resposta = await fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin,ripple&vs_currencies=brl");
        const cotacoes = await resposta.json();

        // Obter o valor correto da moeda escolhida
        let valorConvertido;
        if (moeda === "btc") {
            valorConvertido = valor / cotacoes.bitcoin.brl;
            resultado.innerHTML = `💰 ${valor} BRL = ${valorConvertido.toFixed(6)} BTC`;
        } else if (moeda === "eth") {
            valorConvertido = valor / cotacoes.ethereum.brl;
            resultado.innerHTML = `💰 ${valor} BRL = ${valorConvertido.toFixed(6)} ETH`;
        } else if (moeda === "ltc") {
            valorConvertido = valor / cotacoes.litecoin.brl;
            resultado.innerHTML = `💰 ${valor} BRL = ${valorConvertido.toFixed(6)} LTC`;
        } else if (moeda === "xrp") {
            valorConvertido = valor / cotacoes.ripple.brl;
            resultado.innerHTML = `💰 ${valor} BRL = ${valorConvertido.toFixed(6)} XRP`;
        }

    } catch (error) {
        resultado.innerHTML = "Erro ao obter cotações. Tente novamente mais tarde.";
    }
}
document.getElementById('formCadastro').addEventListener('submit', function (e) {
    e.preventDefault(); // Impede o envio para outra página

    const termos = document.getElementById('termos');

    if (termos.checked) {
        document.getElementById('formCadastro').style.display = 'none'; // Esconde o formulário
        document.getElementById('mensagem').style.display = 'block'; // Exibe a mensagem
    } else {
        alert('Você precisa aceitar os termos e condições!');
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById("aceito-termos");
    const botao = document.getElementById("botao-continuar");

    checkbox.addEventListener("change", function () {
        if (checkbox.checked) {
            botao.classList.add("enabled");
            botao.disabled = false;
        } else {
            botao.classList.remove("enabled");
            botao.disabled = true;
        }
    });

    botao.addEventListener("click", function () {
        if (checkbox.checked) {
            window.location.href = "{% url 'home' %}"; // Redireciona para a página inicial ou outra desejada
        }
    });
});