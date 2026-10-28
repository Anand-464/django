document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("thankButton");
    if (button) {
        button.addEventListener("click", function () {
            alert("Thank you for visiting my website!");
        });
    }
});