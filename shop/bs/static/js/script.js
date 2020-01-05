var navMain = document.querySelector('.main-nav');
var navToggle = document.querySelector('.main-nav__toggle');
var link = document.querySelector('.main-nav__user-login');
var popup = document.querySelector(".modal-login");
var close = popup.querySelector(".modal-login__close");
var form = popup.querySelector("form");
var login = popup.querySelector("[name=login]");
var password = popup.querySelector("[name=password]");
var storage = localStorage.getItem("login");

var application = document.querySelector('.form__apply');
var modalSuccess = document.querySelector('.modal-success');
var modalFailure = document.querySelector('.modal-failure');
var modalLoginClose = document.querySelector('.modal-login__close');
var modalSuccessClose = document.querySelector('.modal-success__close');
var modalFailureClose = document.querySelector('.modal-failure__close');

navMain.classList.remove('main-nav--nojs');

navToggle.addEventListener('click', function() {
    if (navMain.classList.contains('main-nav--closed')) {
        navMain.classList.remove('main-nav--closed');
        navMain.classList.add('main-nav--opened');
    } else {
        navMain.classList.add('main-nav--closed');
        navMain.classList.remove('main-nav--opened');
    }
});

link.addEventListener("click", function(event) {
    event.preventDefault();
    popup.classList.add("modal-login--show");
});

close.addEventListener("click", function(event) {
    event.preventDefault();
    popup.classList.remove("modal-login--show");
});

application.addEventListener('click', function (event) {
    event.preventDefault();
    modalSuccess.classList.add('modal-success--show');
});

modalSuccessClose.addEventListener('click', function (event) {
    event.preventDefault();
    modalSuccess.classList.remove('modal-success--show');
});