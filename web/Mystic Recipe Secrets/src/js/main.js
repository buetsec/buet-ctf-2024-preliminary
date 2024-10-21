const ham = document.getElementById('ham');
const menu = document.getElementById('flyout');
const links = Array.from(document.getElementsByClassName("sideLink"));
console.log(links)
let menuOpen = false;

//animated sidebar
ham.addEventListener('click', () => {
    menu.style.animation = "none";
    setTimeout(() => {
        menu.style.animation = !menuOpen ?
            "sidebar 300ms ease-out" :
            "sidebar 300ms ease-out reverse";
        menu.style.animationFillMode = !menuOpen ?
            "forwards" :
            "both"
        menuOpen = !menuOpen;
    }, 0);
});