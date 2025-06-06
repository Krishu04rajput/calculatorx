function press(val) {
    let display = document.getElementById('display');
    if (val === '+/-') {
        display.value = eval(display.value) * -1;
    } else if (val === '%') {
        display.value = eval(display.value) / 100;
    } else {
        display.value += val;
    }
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    try {
        let result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
    } catch {
        document.getElementById('display').value = 'Error';
    }
}
