$(function(){
    $(".botao").hover(
        function(){
            //Ao posicionar o cursor sobre a div
            $(this).css('background', 'rgba(233, 224, 252)');
           
        },
        function(){
            //Ao remover o cursor da div
            $(this).css('background', 'white');
        }
    );
});


document.getElementById("botoes-acao").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "block";
});

document.getElementById("closePopup").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "none";
});

document.getElementById("botoes-acao2").addEventListener("click", function() {
    document.getElementById("popupContainer2").style.display = "block";
});

document.getElementById("closePopup2").addEventListener("click", function() {
    document.getElementById("popupContainer2").style.display = "none";
});

document.getElementById('botao_confirmar').addEventListener('click', function() {
    document.getElementById('formulario-guardiao').submit();
});

document.getElementById('botao_confirmar2').addEventListener('click', function() {
    document.getElementById('formulario-patrulha').submit();
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
            resposta.style.border = "0px solid rgba(149, 2, 152)";
        });

        // Se a resposta estiver visível, oculte-a
        if (respostaVisivel) {
            respostas[index].style.maxHeight = '0';
            respostas[index].style.border = "0px solid rgba(149, 2, 152)";
        } else {
            // Se a resposta estiver oculta, mostre-a
            respostas[index].style.maxHeight = respostas[index].scrollHeight + 'px';
            respostas[index].style.border = "2px solid rgba(149, 2, 152)";
        }
    });
});
