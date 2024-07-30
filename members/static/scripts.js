document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready!');

    var loginButton = document.getElementById('loginButton');
    loginButton.addEventListener('click', function() {
        window.location.href = 'login';
    });

    var signupButton = document.getElementById('signupButton');
    signupButton.addEventListener('click', function() {
        window.location.href = 'signup';
    });
});``