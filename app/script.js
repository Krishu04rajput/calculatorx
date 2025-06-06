// Handles input on number and operator button press
function press(val) {
  const display = document.getElementById("display");

  // If display is "Error", reset it
  if (display.value === "Error") {
    display.value = "";
  }

  // Handle ± toggle
  if (val === "+/-") {
    if (display.value) {
      if (display.value.startsWith("-")) {
        display.value = display.value.slice(1);
      } else {
        display.value = "-" + display.value;
      }
    }
    return;
  }

  // Handle %
  if (val === "%") {
    if (display.value) {
      display.value = String(parseFloat(display.value) / 100);
    }
    return;
  }

  // Append value to display
  display.value += val;
}

// Clears the display
function clearDisplay() {
  document.getElementById("display").value = "";
}

// Evaluates the expression
function calculate() {
  const display = document.getElementById("display");

  try {
    const result = eval(display.value);
    display.value = Number.isFinite(result) ? result : "Error";
  } catch (err) {
    display.value = "Error";
  }
}
