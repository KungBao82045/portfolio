// VARIABEL. Tenk som en pakke som inneholder verdi

var variable = 0 // Ikke anbefalt å bruke var. Brukes til gammelt browser


// Bruk let hvis du tror verdien kan endres
let variable1 = true // Kan reassigne, men kan ikke redeclare
// Kan reassigne. 
variable1 = "True" 
// Kan ikke redeclare: SyntaxError: Identifier 'variable1' has already been declared
// let variable1 = "False"



// Bruk const hvis du tror verdien kan IKKE endres
const variable2 = "Hello, World!" // Kan ikke reassigne og redeclare.
// Kan ikke reassigne:
// variable2 = "Hi?"

// Kan ikke redeclare
// const variable2 = "OK PEOPLE!"


// Skriv ut inneholdet fra konsollen. Finner i inspiser nettside.
console.log(variable, variable1, variable2) // 0 true "Hello, World!"








// DATATYPER
console.log(typeof(true)) // Boolean
console.log(typeof(12))   // Number
console.log(typeof("Hi, there!")) // String







// IF-SETNINGER

// ===     Sammenligner mellom to verdier
// ==      Konverterer verdier før sammenligner
// >=      Bedre enn eller like
// >       Betyr bedre enn
// <       Betyr mindre enn

if(10 === 20) { // False
    console.log("Yes")
} else {
    console.log("False")
}

if("12" == 12) { // "12" ble konvertert til integer og deretter, 12 === 12 returnerer True
    console.log("Yup!") // Returnerer True.
} else if("Hi" == 2) { // Kan ikke konvertere
    console.log("YESSSSU")
} else {
    console.log("NONONO")
}






// FUNKSJON - definer navn på funksjon "myfunc()" og inni paranteser, inneholder det parameter. 
// Funksjon kan gjøre koden din kortere. 

function myfunc(par1, par2) { 
    return par1 + par2
}

console.log(myfunc(230, 249)) // Skriv ut inneholdet i funksjon
console.log("The Answer:", myfunc(50, 50) + 200) // Returner 300


function myfunc1(par1, par2) {
    console.log(par1 + par2)
}

myfunc1(30,30) // Skriv ut 60


const func22 = myfunc1(56, 56)
console.log("Answer1:", func22)         // Undefined: bruker ikke return
console.log("Answer2:", myfunc1(50,50)) // Undefined: bruker ikke return




// ARRAYS
// Arrays. Kan ha flere verdier i en variabel
const arreys = ["Chicken", "Apple", "Orange", "Green", "Terrorist"]
console.log(arreys)
console.log(arreys[1]) // Hent spesifikk verdi. Starter fra 0. Skriv ut "Apple"

arreys.push("Lol") // Adder ny verdi slutten av array
arreys.pop() // Fjern verdi slutten av array
arreys.sort() // Sorter verdier. Starter fra A-Z eller starte fra minst tall til høyest tall
console.log(arreys.includes("Green")) // Returnert true

console.log(arreys)




// LOOP - Kjører koden om og om igjen. Kan gjøre koden kortere og organisert

for (let i = 0; i <= 10; i++) { // Itererer fra 0 til 10
    console.log(i)
}

const for_of_test = "World"
for(let index of for_of_test) { // Itererer hvert bokstaver
    console.log(index)
}

const for_of_test_array = ["Chicken", "Salsa", "In", "McDonald"]
for(let index1 of for_of_test_array) { // Itererer hvert ord
    console.log(index1)
}