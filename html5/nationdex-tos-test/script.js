let button = document.querySelector("#button");
let isBroken = false;
let clickCounter = 0;

button.style.background = "blue";

button.addEventListener("mouseover", e => {
    if (isBroken === false) {
        button.style.background = "green";
        button.style.color = "white";
    }
});

button.addEventListener("mouseout", e => {
    if (isBroken === false) {
        button.style.background = "blue";
    }
});

button.addEventListener("click", e => {
    clickCounter++;

    if (clickCounter >= 10) {
        button.style.background = "red";
        button.innerHTML = "Au";
        isBroken = true;
    }
});

const campus1 = document.querySelector('#textcampus1');
const campus2 = document.querySelector('#textcampus2');
const operation = document.querySelector('#operation');
let answer = document.querySelector('#answer');

operation.addEventListener("change", calculate);
campus1.addEventListener("keyup", calculate);
campus2.addEventListener("keyup", calculate);

function calculate() {
    if (campus1.value != "" && campus2.value != "") {
        const num1 = parseInt(campus1.value);
        const num2 = parseInt(campus2.value);
        const op = operation.value;

        if (op === "suma") {
            answer.innerHTML = num1 + num2;
        } else if (op === "resta") {
            answer.innerHTML = num1 - num2;
        } else if (op === "multiplicacion") {
            answer.innerHTML = num1 * num2;
        } else if (op === "division") {
            answer.innerHTML = num1 / num2;
        }
    }
};
