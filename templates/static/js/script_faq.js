$(function(){
    $(".botao").hover(
        function(){
            //Ao posicionar o cursor sobre a div
            $(this).css('background', 'rgb(187, 184, 184)');
           
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