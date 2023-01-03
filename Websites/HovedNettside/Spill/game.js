
/*
Du har 100 helse. Hvis helsen din er under 0, taper du. 
Hvis du har 1000kr til flybilett, vinner du.
Velg en av ran type for å stjele penger.
*/
var startSpillet = true;

var helseHP = document.getElementById("helse");
var bankPenger = document.getElementById("bank");
var win_win = document.getElementById("vinner");
var resultE = document.getElementById("E_resultat");
var resultT = document.getElementById("T_resultat");

var HP = 100
var Bank = 0


helseHP.innerText = "Helse: " + HP;
bankPenger.innerText = "Bank: " + Bank + "kr";



function ranFunction() {
    if(startSpillet) {
        var quotes = Math.floor(Math.random() * 2);
        var random = Math.floor(Math.random() * 10);
        var risiko = Math.floor(Math.random() * 10);
        random === 0 ? random += 1 : console.log("Not 0");
        console.log(risiko)
    
        if(risiko < 8) {
            Bank += random;
            bankPenger.innerText = "Bank: " + Bank + "kr";
            var missionCompleted = ["Du datt ned en person og stikker av med ", "Du har truet en person om å gi deg penger og stikker av med "];
            resultE.innerText = missionCompleted[quotes] + random + "kr";
        } 
        
        else { /* Hvis risiko er ikke bedre enn 8. Feil */ 
            HP -= random;
            helseHP.innerText = "Helse: " + HP 
            var missionFailed = ["Personen vet boxing. Slo deg på hodet og stikker av for sikkerhet skyld", "Personen sparka deg og løpte fra deg."];
            resultE.innerText = missionFailed[quotes];
            if (HP < 0) {
                helseHP.innerText = "Du døde. Game Over!";
                startSpillet = false;
            }
        }
    }    
}

function butikkFunction() {
    if(startSpillet) {
        var quotes = Math.floor(Math.random() * 2);
        var random = Math.floor(Math.random() * 100);
        var risiko = Math.floor(Math.random() * 10);
        random === 0 ? random += 1 : console.log("Big not 0");

        if(risiko < 8) {
            Bank += random;
            bankPenger.innerText = "Bank: " + Bank + "kr";
            var hardCOmpleted = ["Du rante en dagligvarebutikk og stikker av med ", "Du rante en kiosk og stikker av med "]
            resultT.innerText = hardCOmpleted[quotes] + random + "kr";
        }
        else {
            HP -= random;
            helseHP.innerText = "Helse: " + HP;
            var HardFailed = ["Folk rundt deg prøver å sammarbeide og taklet deg ned. politiet kommer og arresterer deg. Game Over!", "Du ble slått ned med balltre. Politi kommer og arresterer deg. Game Over!"]
            resultT.innerText = HardFailed[quotes];
            startSpillet = false
        }
    }
}


function heal() {
    if(startSpillet) {
        if(Bank > 74) {
            Bank -= 75;
            HP += 25
            bankPenger.innerText = "Bank: " + Bank + "kr";
            helseHP.innerText = "Helse: " + HP 
        }
    }
}


function win() {
    if(startSpillet) {
        if(Bank > 999) {
            Bank -= 500
            win_win.innerText = "Du rømte fra Norge! Gratulerer!";
            startSpillet = false;
        }
    }
}