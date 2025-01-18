document.getElementById("submit-btn").addEventListener("click", async () => {
    const inputBox = document.getElementById("input-box").innerText;
    const outputBox = document.getElementById("output-box");

    const response = await fetch("/correct", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input_text: inputBox })
    });

    if (response.ok) {
        const data = await response.json();
        outputBox.innerText = data.corrected_text;
    } else {
        outputBox.innerText = "Error occurred while processing.";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const inputBox = document.getElementById("input-box");
    const maxLenBox = document.getElementById("current-len");
    const MAX_LENGTH = 512;

    inputBox.addEventListener("input", function () {
        const currentLength = inputBox.textContent.length;
        maxLenBox.textContent = currentLength;

        if (currentLength > MAX_LENGTH) {
            inputBox.textContent = inputBox.textContent.substring(0, MAX_LENGTH);
            maxLenBox.textContent = MAX_LENGTH;
        }
    });
});