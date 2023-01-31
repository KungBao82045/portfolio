//function myFunction() {
//    var x = document.getElementById("topnav");
//    if (x.className === "Meny") {
//      x.className += " responsive";
//      console.log("Clicked on the meny icon")
//    } else {
//      x.className = "Meny";
//    }
//  }

const toggleButton = document.getElementsByClassName("button")[0]
const navbarLinks = document.getElementsByClassName("Meny")[0]

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle("active")
  

})


// Portfolio

// const acc = document.getElementsByClassName("SchoolProject2021_2022");   // Lage variablel og info inni variabel
// var i;                                                                // Lage variabel uten value

// for (i = 0; i < acc.length; i++) {   
//     /* Toggle between adding and removing the "active" class,
//     to highlight the button that controls the panel */                      
//     acc[i].addEventListener("click", function() {
//         this.classList.toggle("active");
//         var panel = this.nextElementSibling;
//         /* Toggle between hiding and showing the active panel */
//         if (panel.style.display === "block") {
//         panel.style.display = "none";
//         } else {
//         panel.style.display = "block";
//         }
//     });
// }

// lag variabel
const buttons = document.getElementsByClassName("SchoolProject2021_2022");
// Creates a new array with the 
// result of calling a function for each array element
[...buttons].map(button => {
    button.addEventListener("click", (e) => {
        let currentButton = e.target;
        let currentAccordionItem = currentButton.nextElementSibling;

        // Lukk alle først
        let items = document.getElementsByClassName("TrykkePåBoks active");
        [...items].map(item => {
            item.classList.remove("active");
        })

        // Next step, åpne den som ble trykket på
        currentAccordionItem.classList.add("active");
    });
});



// Programmering


let tidboks = document.getElementById("time");

tidboks.innerHTML = Date();
tidboks.style.backgroundColor = "Red";


let box = document.getElementById("box");

box.style.width = "200px";
box.style.height = "200px";
box.style.backgroundColor = "black";

box.addEventListener("click", () => {


    if(box.style.backgroundColor == "black") {
        box.style.backgroundColor = "red";
    }
    else {
        box.style.backgroundColor = "black";
    }
})



function myfunc2() {
    var element = document.body
    element.classList.toggle("dark_moded")
}
// Variables defined with const cannot be Redeclared.

// Variables defined with const cannot be Reassigned.

// Variables defined with const have Block Scope.


// The addEventListener() method attaches an event...
// handler to the specified element.