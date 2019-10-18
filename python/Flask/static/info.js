spanTemp = document.getElementById('tempDiv');
spanHum = document.getElementById('humDiv');
spanLux = document.getElementById('luxDiv');

function setColors(){
    validateHum();
    validateLux();
    validateTemp();
}

function validateHum() {
    var humVal = document.getElementById('lastHum').innerHTML;
    if (humVal < 40) {
        spanHum.style.color = "red";
    } else if (40 <= humVal && humVal <  45) {
        spanHum.style.color = "orange";
    } else if (45 <= humVal && humVal <  55) {
        spanHum.style.color = "green";
    } else if (55 <= humVal && humVal <  60) {
        spanHum.style.color = "orange";
    } else if (humVal >=60){
        spanHum.style.color = "red";
    }
}

function validateTemp() {
    var tempVal = document.getElementById('lastTemp').innerHTML;
    if (tempVal <11) {
        spanTemp.style.color = "red"
    } else if (11 <= tempVal && tempVal< 16) {
        spanTemp.style.color = "orange"
    } else if (16 <= tempVal && tempVal< 20) {
        spanTemp.style.color = "green"
    } else if (20 <= tempVal && tempVal< 25) {
        spanTemp.style.color = "orange"
    } else if(tempVal >= 25){
        spanTemp.style.color = "red"
    }
}

function validateLux() {
    var luxVal = document.getElementById('lastLux').innerHTML;
    if (luxVal <5) {
        spanLux.style.color = "green"
    } else if (5 <= luxVal && luxVal< 10) {
        spanLux.style.color = "orange"
    } else if (luxVal >= 10){
        spanLux.style.color = "red"
    }
}

setColors();

