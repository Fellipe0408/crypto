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

window.toggleMenu() {
    var sideMenu = document.getElementById("sideMenu");
    var currentPosition = sideMenu.style.right;
    if (currentPosition === "0px") {
        sideMenu.style.right = "-250px"; // Esconde o menu
    } else {
        sideMenu.style.right = "0"; // Mostra o menu
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
fetch("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=percent_change_24h_desc&per_page=3&page=1")
  .then(response => response.json())
  .then(data => {
    const lista = document.getElementById("criptoEmAlta");
    lista.innerHTML = ""; // limpa antes de adicionar
    data.forEach(coin => {
      const li = document.createElement("li");
      li.textContent = `${coin.name} ${coin.price_change_percentage_24h.toFixed(2)}%`;
      lista.appendChild(li);
    });
  });