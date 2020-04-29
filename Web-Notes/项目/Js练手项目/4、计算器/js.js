/* limpa o display */
document.getElementById("clear").addEventListener("click", function () {
    document.getElementById("display").value = "";
});
/* recebe os valores */
function get(value) {
    document.getElementById("display").value += value;
}

/* calcula */
function calculates() {
    var result = 0;
    result = document.getElementById("display").value;
    document.getElementById("display").value = "";
    document.getElementById("display").value = eval(result);
};