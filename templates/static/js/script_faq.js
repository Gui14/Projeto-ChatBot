$(function(){
    $(".botao").hover(
        function(){
            //Ao posicionar o cursor sobre a div
            $(this).css('background', 'rgb(187, 184, 184)');
           
        },
        function(){
            //Ao remover o cursor da div
            $(this).css('background', 'rgba(233, 224, 252)');
        }
    );
});


document.getElementById("botoes-acao").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "block";
});

document.getElementById("closePopup").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "none";
});

// Selecione todos os botões e respostas
const botoes = document.querySelectorAll('.botao');
const respostas = document.querySelectorAll('.resposta');

// Adicione um evento de clique a cada botão
botoes.forEach((botao, index) => {
    botao.addEventListener('click', () => {
        // Verifique se a resposta está visível
        const respostaVisivel = respostas[index].style.maxHeight !== '0px';

        // Oculte todas as respostas
        respostas.forEach((resposta) => {
            resposta.style.maxHeight = '0';
        });

        // Se a resposta estiver visível, oculte-a
        if (respostaVisivel) {
            respostas[index].style.maxHeight = '0';
        } else {
            // Se a resposta estiver oculta, mostre-a
            respostas[index].style.maxHeight = respostas[index].scrollHeight + 'px';
        }
    });
});
