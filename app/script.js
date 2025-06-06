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
}function press(val) {
  const display = document.getElementById("display");
  if (val === '+/-') {
    display.value = -1 * parseFloat(display.value || "0");
  } else if (val === '%') {
    display.value = parseFloat(display.value || "0") / 100;
  } else {
    display.value += val;
  }
}

function clearDisplay() {
  document.getElementById("display").value = "";
}

function calculate() {
  try {
    const result = eval(document.getElementById("display").value);
    document.getElementById("display").value = result;
  } catch {
    document.getElementById("display").value = "Error";
  }
}


function calculate() {
    try {
        let result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
    } catch {
        document.getElementById('display').value = 'Error';
    }
}
