var flower;

function setup() {
    createCanvas(400, 400);
    flower = {
    	col : color(220, 220, 220),
    	name : "sunflower"
    }
}

function draw() {
    background(0);
    fill(flower.col);
    text(flower.name, 5, 5);
    

}