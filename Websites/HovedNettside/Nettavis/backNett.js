
// Dette er når du trykker på en av artikklene, kommer det opp øverst på nettsiden.
const menuList = document.getElementsByClassName("section");
const sections = document.getElementsByTagName("article"); 
[...menuList].forEach(menuItem => {
    menuItem.addEventListener("click", (e) => {
        let target = menuItem.dataset.target;
        [...sections].forEach(section => {
            section.classList.add("hide");
        });
        document.getElementById(target).classList.remove("hide");
    });
});