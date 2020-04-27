var username = document.getElementById("username");
var password = document.getElementById("password");

function usernameFocus() {
    username.value = "";
}

function passwordFocus() {
    password.value = "";
}

function usernameBlur(){
    if (username.value == ""){
        username.value = "username";
    }
}

function passwordBlur(){
    if (password.value == ""){
        password.value = "password";
    }
}
