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
