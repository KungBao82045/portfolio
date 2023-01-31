/*
Spillets regler:

Elevene skal utforme ett spill for to spillere som dreier seg om å kaste en terning og samle inn poeng. 
Spillet har 2 spillere, som spiller i runder. I hver runde ruller en spiller terningen så mange ganger han vil. 
Hvert resultat blir lagt til hans poeng for hver runde. 
Hvis spilleren ruller en 1, blir all hans runde poengsum tapt. 
Etter det er det neste spillers tur. 
Spilleren kan velge å holde sin poengsum, noe som betyr at hans runde poengsum blir lagt til hans totale poengsum. 
Etter det er det neste spillers tur. 
Den første spilleren som når 100 poeng (eller valgfri maxsum) på spillerens totale poengsum vinner spillet.
*/

var poengsum, rundePoeng, aktivSpiller, spill, maxPoeng, rotation;
startSpill()

// var terning = Math.floor(Math.random() * 6 ) + 1;


 
// Når jeg trykker på "Kast terning"
document.querySelector(".btn-kast").addEventListener("click", function(){
    if (spill) {
        // 1. Tilfeldig nummer (Kast terning)
        var terning = Math.floor(Math.random() * 6) + 1;

        // 2. Vis resultatet
        document.querySelector(".terning").style.display = "block";
        document.querySelector(".terning").src = "img/terning-" + terning + ".png";
        // 3. Oppdater rundePoeng bare hvis kastet terning er mellom 2 og 6.
        if (terning !== 1) {
            // Legg til poeng
            rundePoeng += terning;
            // Oppdater poenget til nettsidet
            document.querySelector("#sum-" + aktivSpiller).textContent = rundePoeng;
        } else {
            // Neste spiller
            nesteSpiller();
        }
    }

    // var terning = Math.floor(Math.random() * 6 ) + 1;
    // Gjør at hvis terning er "6", finner koden filen: terning-6.png
    // Hvis terning er "10", finner koden IKKE filen: terning-10.png. Kan kræsje ut error. (Vi skal ikke ha mer enn 6 terning).
    // document.querySelector(".terning").src = "img/terning-" + terning + ".png";

    // if(terning !== 1) {
    //     rundePoeng += terning;
    //     document.querySelector("#sum-" + aktivSpiller).textContent = rundePoeng;
    // } else {
    //     nesteSpiller()
    //     // Nullstill sum poeng
    //     // document.getElementById("sum-0").textContent = "0";
    //     // rundePoeng = 0;
    //     // // Fjerner "aktiv" fra klassen på linje 15
    //     // document.querySelector(".spiller-0-panel").classList.remove("aktiv");
    //     // document.querySelector(".spiller-1-panel").classList.add("aktiv");
    // }
});

// Når jeg trykker på "Hold"
document.querySelector(".btn-hold").addEventListener("click", function() {
    // Uten if spill, spillet fortsetter etter en spiller har vunnet.
    if (spill) {
        // Legg til poengsum fra rundepoeng
        poengsum[aktivSpiller] += rundePoeng;
        // Oppdater poengsum
        document.getElementById("poeng-" + aktivSpiller).textContent = poengsum[aktivSpiller];
    
        // hvis spiller 1 vant, bytt spiller 1 til "Chicken Dinner" og spiller 2 til "Taper"
        if(poengsum[0] >= maxPoeng) {
            document.querySelector("#navn-0").textContent = "Chicken Dinner! 😎";
            document.querySelector("#navn-1").textContent = "Taper 😭";
    
            // Grønn tekst fra vinner og fjern fots fra aktiv
            document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.add("vinner");
            document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.remove("aktiv");
    
            // Adder taper (rød tekst, bakgrunn mørk, poeng farge hvit) 
            document.querySelector(".spiller-1-panel").classList.add("taper");
           // document.querySelector(".spiller-1-panel").classList.remove("aktiv");
            spill = false;
        // Hvis spiller 2 vant, bytt spiller 2 navn til "Chicken Dinner" og spiller 2 til "Taper"
        } else if (poengsum[1] >= maxPoeng) {
            document.querySelector("#navn-1").textContent = "Chicken Dinner! 😎";
            document.querySelector("#navn-0").textContent = "Taper 😭";
    
            // Grønn tekst fra vinner og fjern fots fra aktiv
            document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.add("vinner");
            document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.remove("aktiv");
    
            // Adder taper (rød tekst, bakgrunn mørk, poeng farge hvit) 
            document.querySelector(".spiller-0-panel").classList.add("taper");
            //document.querySelector(".spiller-0-panel").classList.remove("aktiv");
            spill = false;
        // Bytt spiller hvis ingen av de spillere har mer enn "maxPoeng"
        } else {
            nesteSpiller()
        }
    }

        // if(poengsum[aktivSpiller] >= maxPoeng) { // Hvis spiller fikk "maxPoeng"
        //     document.querySelector("#navn-" + aktivSpiller).textContent = "Chicken Dinner!";
        //     document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.add("vinner");
        //     document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.remove("aktiv");
        //     spill = false;
        //     // Test
        //     console.log("poengsum: " + poengsum + "\n" + "rundePoeng: " + rundePoeng + "\n" + "aktivSpiller: " + aktivSpiller + "\n" + "spill: " + spill + "\n" + "maxPoeng: " + maxPoeng)
        // } else {
        //     nesteSpiller();
        // }

    
    
});


function nesteSpiller() {
    // Neste spiller
    aktivSpiller === 0 ? aktivSpiller = 1 : aktivSpiller = 0;
    rundePoeng = 0;
    // Oppdater GUI
    document.getElementById("sum-0").textContent = "0";
    document.getElementById("sum-1").textContent = "0";
    // Endre på aktiv spiller i CSS (dot)
    document.querySelector(".spiller-0-panel").classList.toggle("aktiv");
    document.querySelector(".spiller-1-panel").classList.toggle("aktiv");
}

// Når "Nytt spill" ble trykket, kjører funksjonen startSpill()
document.querySelector(".btn-ny").addEventListener("click", startSpill);


// Start spill eller nullstille
function startSpill() {
    poengsum = [0, 0];
    aktivSpiller = 0;
    rundePoeng = 0;
    spill = true;
    maxPoeng = 100;

    // Alle spiller fjerne vinner (grønn tekst, osv), aktiv (dots)
    document.querySelector(".spiller-0-panel").classList.remove('aktiv');
    document.querySelector(".spiller-1-panel").classList.remove('aktiv');
    document.querySelector(".spiller-0-panel").classList.remove('vinner');
    document.querySelector(".spiller-1-panel").classList.remove('vinner');

    document.querySelector(".spiller-0-panel").classList.remove('taper');
    document.querySelector(".spiller-1-panel").classList.remove('taper');

    document.querySelector(".spiller-0-panel").classList.add('aktiv');

    document.querySelector('.terning').style.display = 'none';


    // document.querySelector(".spiller-" + aktivSpiller + "-panel").classList.remove("vinner");

    // Bytt navnet til spiller 1 og spiller 2
    document.getElementById("navn-0").textContent = "Spiller 1";
    document.getElementById("navn-1").textContent = "Spiller 2";
    console.log("Første man til " + maxPoeng + " vinner!")
    // document.querySelector("#sum-" + aktivSpiller).textContent = terning;
    document.querySelector("#sum-" + aktivSpiller).textContent = terning;

    document.querySelector("#sum-" + aktivSpiller).innerHTML = "<em>" + terning + "</em>";


    // Spiller 1 poeng nullstill
    document.getElementById("poeng-0").textContent = "0";
    document.getElementById("sum-0").textContent = "0";
    // Spiller 2 poeng nullstill
    document.getElementById("poeng-1").textContent = "0";
    document.getElementById("sum-1").textContent = "0";


    document.getElementById("mål").innerHTML = "Første man til " + maxPoeng + " vinner!";

    // Test
    console.log("poengsum: " + poengsum + "\n" + "rundePoeng: " + rundePoeng + "\n" + "aktivSpiller: " + aktivSpiller + "\n" + "spill: " + spill + "\n" + "maxPoeng: " + maxPoeng)
    
}

