const closeChatButton = document.querySelector('.chat-close-icon');
const chatContainer = document.querySelector('.chat-container');
const botContainer = document.querySelector('.bot-container');
const botPopup = document.querySelector('.bot-popup');



function centrarPopup() {
    //Se obtiene los valores del tamano del contenedor padre y el contenedor hijo
    let botContainerWidth = botContainer.offsetWidth;
    let botContainerHeight = botContainer.offsetHeight;
    let popupWidth = botPopup.offsetWidth;
    let popupHeight = botPopup.offsetHeight;

    //Calcula la posicion y la centra
    let leftPosition = (botContainerWidth - popupWidth) / 2;
    let topPosition = (botContainerHeight - popupHeight) / 2;

    //Aplica el valor obtenido al HTML
    botPopup.style.position = "absolute;"
    botPopup.style.left = leftPosition + "px";
    botPopup.style.top = topPosition + "px";
}

var gifs = ["../static/img/default.gif", "../static/img/sleepstart.gif", "../static/img/sleeploop.gif"];
var currentGif = 1;
var gifIndex = 0
let intervalID = setInterval(changeGif, 6000);


function changeGif() {
    var botBackground = document.querySelector('.bot-background');
    if (currentGif === 1) {
        clearInterval(intervalID); // detener el intervalo actual
        botBackground.style.backgroundImage = "url('" + gifs[gifIndex] + "')";
        gifIndex++;
        currentGif = 2;
        intervalID = setInterval(changeGif, 10000); // primero ejecuta [0] default.gif luego lo aumenta iniciar un nuevo intervalo con un tiempo de 10 segundos
    } else if (currentGif === 2) {
        clearInterval(intervalID);
        botBackground.style.backgroundImage = "url('" + gifs[gifIndex] + "')";
        gifIndex++
        currentGif = 3;
        intervalID = setInterval(changeGif, 2000); // ejecuta [1] sleepstart luego lo aumenta iniciar un nuevo intervalo con un tiempo de 2 segundos
    } else if (currentGif === 3) {
        botBackground.style.backgroundImage = "url('" + gifs[gifIndex] + "')"
        currentGif = 4;
    } else if (currentGif === 4) {
        // ejecuta [2] sleeploop y queda ahi el sleeploop se quedará en loop infinito
    }
}
//cuando carga la pagina y cuando cambia de tamano llama a la funcion para centrar siempre al robot 
window.addEventListener("load", centrarPopup);
window.addEventListener("resize", centrarPopup);


//Funciones para abrir y cerrar el chat
botContainer.addEventListener('click', openChat);

function openChat() {
    botContainer.setAttribute('id', 'inactive');
    chatContainer.removeAttribute('id', 'inactive')
}

closeChatButton.addEventListener('click', closeChat);

function closeChat() {
    chatContainer.setAttribute('id', 'inactive');
    botContainer.removeAttribute('id', 'inactive');
}

$(function() {
    $('form').on('submit', function(event) {
      event.preventDefault();
      var formData = $(this).serialize();
      $.ajax({
        type: 'POST',
        url: '',
        data: formData,
        success: function(response) {
          $('#chat-area').append('<div class="message"><span class="user-input">' + response.input_usuario + '</span><span class="bot-response">' + response.resultado + '</span></div>');
          $('input[name="input_usuario"]').val('');
        }
      });
    });
  });
