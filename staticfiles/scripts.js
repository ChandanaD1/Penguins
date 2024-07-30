document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready!');

    var loginButton = document.getElementById('loginButton');
    loginButton.addEventListener('click', function() {
        redirect('login.html')
    });

    var signupButton = document.getElementById('signupButton');
    signupButton.addEventListener('click', function() {
        redirect('signup.html')
    });
});