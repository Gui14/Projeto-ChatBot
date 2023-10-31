document.addEventListener("keypress", function(e) {
    if(e.key === 'Enter') {
    
        var btn = document.querySelector("#enviar");
      
      btn.click();
    
    }
  });

  
  // Define um cookie de sessão para rastrear o status de login
  document.cookie = "user_logged_in=true; path=/";

  // Adiciona um manipulador de eventos para o evento "beforeunload"
  window.addEventListener('beforeunload', function (e) {
      if (document.cookie.indexOf('user_logged_in=true') !== -1) {
          // O usuário está logado, então faz o logout
          $.post('/logout/', function () {
              // Redireciona o usuário para a página de logout ou outra página de sua escolha
              window.location.href = '/logout/success/';
          });
      }
  });
