// 获取模型
var modal = document.getElementById('id01');

// 鼠标点击模型外区域关闭登录框
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}