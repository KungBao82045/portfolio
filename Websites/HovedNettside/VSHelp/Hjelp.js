

//left racket position and height
let racketPos1 = 250;
let racketHeight = 100;
let racketpos1 = 50;


// right racket position and height
let racketPos2 = 250;
let racketHeight2 = 100;
let racketpos2 = 730;

// PingPong Ball
let xPos = 200;
let yPos = Math.floor(Math.random() * 300) + 50;
let diameter = 25;
let xSpeed = (2, 7);
let ySpeed = (-7,-2);

//Score
let score = 0;
    
function setup() {
createCanvas(800, 650);
}


function draw() {
background(0);

// line
  fill (random(255) , random(255), random (255));
  rect (400, 620, 10, 25);
  rect (400, 570, 10, 25);
  rect (400, 520, 10, 25);
  rect (400, 470, 10, 25);
  rect (400, 420, 10, 25);
  rect (400, 370, 10, 25);
  rect (400, 320, 10, 25);
  rect (400, 270, 10, 25);
  rect (400, 220, 10, 25);
  rect (400, 170, 10, 25);
  rect (400, 120, 10, 25);
  rect (400, 70, 10, 25);
  rect (400, 20, 10, 25);
  rect (0, 0, 800, 10);
  rect (0, 640, 800, 10);
  rect (0, 0, 10, 650);
  rect (790, 0, 10, 650);
  circle (405, 310, 100);

// racket on the left side
noStroke();
fill(random(255), 0, 0);
rect(racketpos1, racketPos1, 10, racketHeight);

if (keyIsDown(87)){
racketPos1 -= 5;
}
else if (keyIsDown(83)){
racketPos1 += 5;
} 

// racket on the right side
fill (0, 0, random(255));
rect (racketpos2, racketPos2, 10, racketHeight2);  

if (keyIsDown(UP_ARROW)){
racketPos2 -= 5;
}
else if (keyIsDown(DOWN_ARROW)){
racketPos2 += 5;
} 
  
// ball
fill (random(255), 0, random(255));
circle (xPos, yPos, diameter);

// functions
  resetBall();
  move();
  bounce();
  paddle();
  
// BallSpeed
function move(){
yPos += ySpeed;
xPos += xSpeed;
}
  
// Bounce on wallsw
function bounce (){
if (yPos < 10 || yPos > 640) {
      ySpeed *= -1;
    }
if (xPos < 10 || xPos > 785) {
      xSpeed *= -1;
    }
  } 

function paddle (){
if ((yPos > racketPos1 && yPos < racketPos1) && (xPos + 10 >= racketpos1));
else if ((yPos > racketPos2 && yPos < racketPos2) && (xPos + 10 <= racketpos2));
}

 // Reset Ball
  function resetBall() {
    if (xPos >= 785) {
      score(0);
      text("Score: Winner!" + score, 600, 50);
    }
    if (xPos <= 15) {
      score(0);
      text("Score: Winner!" + score, 100, 50);
    }
  }
}