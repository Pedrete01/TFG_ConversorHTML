// ----------- NavBar ------------

const navMenu = document.querySelector("#navMenu");
const ulMenu = document.querySelector("#ulMenu");

navMenu.addEventListener("click", () => {
    navMenu.classList.toggle("activeNav");
    if (navMenu.classList.contains("activeNav")) {
        ulMenu.style.left = "0";
    } else {
        ulMenu.style.left = "-400px";
    }

});