const messages = [
    "¡Hola, bienvenidos!",   
    "Hello, welcome!",       
    "Bonjour, bienvenue!",   
    "Hallo, willkommen!",    
    "Ciao, benvenuti!",      
    "Ola, bem-vindos!"       
];

let currentMessageIndex = 0;
let currentCharacterIndex = 0;
let typingSpeed = 100;

function typeMessage() {
    const message = messages[currentMessageIndex];
    const currentCharacter = message.slice(0, currentCharacterIndex + 1);

    document.getElementById("welcome-message").textContent = currentCharacter;

    if (currentCharacterIndex < message.length - 1) {
        currentCharacterIndex++;
        setTimeout(typeMessage, typingSpeed);
    } else {
        setTimeout(function() {
            currentMessageIndex = (currentMessageIndex + 1) % messages.length;
            currentCharacterIndex = 0;
            typeMessage();
        }, 1500);
    }
}

window.onload = function() {
    typeMessage();
};

window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
