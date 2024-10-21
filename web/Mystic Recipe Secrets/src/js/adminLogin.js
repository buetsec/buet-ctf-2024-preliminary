const usernameField = document.getElementById("user");
const passwordField = document.getElementById("pass");

document.addEventListener('keyup', (event) => {
    if (event.key === "Enter") {
        processLogin();
    }
});

function processLogin() {
    const enteredUsername = usernameField.value;

    if (enteredUsername !== "admin") {
        notifyUser("Access Denied: Admins only!");
        return;
    }

    const enteredPassword = passwordField.value;
    const transformedPassword = encodePassword(enteredPassword);

    storeCookie("hiddenRecipe", transformedPassword, 365);

    redirectToEditor();
}

function notifyUser(message) {
    alert(message);
}

function redirectToEditor() {
    window.location.href = "adminEditor.html";
}

function storeCookie(cookieName, cookieValue, expiryDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expiryDays * 24 * 60 * 60 * 1000));
    const expiry = "expires=" + date.toUTCString();
    document.cookie = `${cookieName}=${cookieValue};${expiry};path=/`;
}

function retrieveCookie(cookieName) {
    const namePattern = `${cookieName}=`;
    const allCookies = decodeURIComponent(document.cookie).split(';');

    for (let i = 0; i < allCookies.length; i++) {
        let cookie = allCookies[i].trim();
        if (cookie.startsWith(namePattern)) {
            return cookie.substring(namePattern.length);
        }
    }
    return "";
}

function encodePassword(passwordInput) {
    return Array.from(passwordInput)
        .map(char => char.charCodeAt(0) + "b")
        .join("");
}