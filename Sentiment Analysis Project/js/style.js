const txt = document.querySelector('#myTextarea');
function setNewSize() {
   this.style.height = "1px";
   this.style.height = this.scrollHeight + "px";
}
txt.addEventListener('keyup', setNewSize);