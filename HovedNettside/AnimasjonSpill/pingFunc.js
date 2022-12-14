
// Funksjonen spill() gjører selve spillet,
// og gjenta i det uendelige
function spill() {
    // Tømmer alt innhold på canvaas-element
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Flytter og tegner opp de to spillerne
    spiller1.flytt();
    spiller1.tegn();
    spiller2.flytt();
    spiller2.tegn();

    // Flytter og tegner opp ballen
    ball.flytt(spiller1, spiller2);
    ball.tegn();

    // Gjentar funksjonen spill()
    requestAnimationFrame(spill);


}



// Når en knapp holdes nede,
// registreres den som true i arrayen taster,
// tilsvarende slettes den (settes til false)
// Når den ikke holdes nede
function knappnedopp(e) {
    if (e.type === "keydown") {
        taster[e.keyCode] = true;
    } else if (e.type === "keyup") {
        delete taster[e.keyCode];
    }
}


// Lager en klasse for spillerne
class Spiller {
    constructor(x, y, bredde, hoyde, fart, opptast, nedtast, farge) {
        // Spillerens egenskaper
        this.x = x;
        this.y = y;
        this.bredde = bredde;
        this.hoyde = hoyde;
        this.fart = fart;
        this.opptast = opptast;
        this.nedtast = nedtast;
        this.farge = farge;
    }

    // Metoden tegn() tegner opp spilleren
    tegn() {
        ctx.fillStyle = this.farge;
        ctx.fillRect(this.x, this.y, this.bredde, this.hoyde);
    }

    // Metoden flytt() flytter spilleren
    flytt() {
        this.y += this.fart;

        if (taster[this.opptast] && this.y >= 1) { // Justert
            this.y -= 5;
            this.fart = -10;
            console.log("Koordinat: " + this.y)
        } else if (taster[this.nedtast] && this.y <= 448) { // Justert
            this.y += 5;
            this.fart = 10;
            console.log("Koordinat: " + this.y)
        } else {
            this.fart = 0;
        }
    }
}
// Lager de to spillerne
// var spiller1 = new Spiller(50, 300, 20, 100, 0, 87, 83, "white"); // Justert
// var spiller2 = new Spiller(530, 300, 20, 100, 0, 38, 40, "white"); // Justert



// Lager en klasse for ballen
class Ball {
    
    constructor(x, y, radius, xFart, yFart, farge) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.xFart = xFart;
        this.yFart = yFart;
        this.farge = farge;
    }

    // Metoden tegn() tegner ballen
    tegn() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 2 * Math.PI, false);
        ctx.fillStyle = this.farge;
        ctx.fill();
    }

    flytt(sp1, sp2) {
        this.x += this.xFart;
        this.y += this.yFart;
        
        var topp = this.y - 10;
        var bunn = this.y + 10;
        var venstre = this.x - 10;
        var hoyre = this.x + 10;

        // Treffer topp- eller bunnvegg
        if (topp < 0 || bunn > canvas.height) {
            this.yFart =  -this.yFart;
            // console.log("Top, Bunn: Truffet!")
        }
        // Treffer spiller 1
        if (venstre < sp1.x + sp1.bredde && topp < sp1.y + sp1.hoyde && bunn > sp1.y) {
            this.xFart = -this.xFart;
            audioHit.play();
            // console.log("Spiller 1: Truffet!")

            // Hvis sp1 ikke står still
            if(sp1.fart !== 0) {
                this.yFart = sp1.fart;
                // console.log("Spiller 1 står still")
            }
        }

        // Treffer spiller 2
        if (hoyre > sp2.x && topp < sp2.y + sp2.hoyde && bunn > sp2.y) {
            this.xFart = -this.xFart;
            audioHit.play();
            // console.log("Spiller 2: Truffet!")

            // Hvis sp2 ikke står stille
            if (sp2.fart !== 0) {
                this.yFart = sp2.fart;
                // console.log("Spiller 2 står still")
            }
        }
         // Forlater "banen" (Justert)
        if(this.x < 1) {
            this.x = 700;
            this.y = 350;
            sp1Poeng += 1;
            spiller2Poeng.innerHTML = "Spiller 2: " + sp1Poeng;
            console.log("Spiller 2: " + sp1Poeng);
            audio.play();
        } else if (this.x > canvas.width - 10) {
            this.x = 100;
            this.y = 350;
            sp2Poeng += 1;
            spiller1Poeng.innerHTML = "Spiller 1: " + sp2Poeng;
            console.log("Spiller 1: " + sp2Poeng);
            audio.play();
        }

        if (sp1Poeng === mål) {
            spiller2Poeng.innerHTML = "Vinner!";
            spiller1Poeng.innerHTML = "Taper!";
            spill = false;
        } else if (sp2Poeng === mål) {
            spiller1Poeng.innerHTML = "Vinner!";
            spiller2Poeng.innerHTML = "Taper!";
            spill = false;
        }
    }
}



// Setter i gang funksjonen spill() første gang
requestAnimationFrame(spill);

// Henter canvas-element
var canvas = document.querySelector("#mittCanvas");
var ctx = canvas.getContext("2d");

var audio = new Audio("point.mp3");
var audioHit = new Audio("POP.mp3")

var spaceAdd = document.getElementById("space_between");
spaceAdd.innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";


// Lager en tom array som skal holde på tastene som trykkes ned
var taster = [];

// Lytter etter keydown- og keyup-hendelser
window.addEventListener("keydown", knappnedopp);
window.addEventListener("keyup", knappnedopp);

// Lager ballen
var ball = new Ball(40, 350, 10, 10, 10, "white");

// Lager de to spillerne
var spiller1 = new Spiller(0, 300, 10, 50, 0, 87, 83, "white"); // Justert
var spiller2 = new Spiller(790, 300, 10, 50, 0, 38, 40, "white"); // Justert

var spiller1Poeng = document.getElementById("sp1Poeng");
var spiller2Poeng = document.getElementById("sp2Poeng");

spiller1Poeng.innerHTML = "Spiller 1: 0";
spiller2Poeng.innerHTML = "Spiller 2: 0";

var sp1Poeng = 0;
var sp2Poeng = 0;
var mål = 20;
