var acc = document.querySelectorAll('.notice-title');
acc.forEach(ele => {
    ele.addEventListener("click", () => {
        ele.classList.toggle('active');
        var panel = ele.nextElementSibling;
        console.log(panel);
        if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
});


function removeActiveClass() {
    acc.forEach(ele=>{
        ele.classList.remove('active');
        var panel = ele.nextElementSibling;
        panel.style.maxHeight = null;
    });
}