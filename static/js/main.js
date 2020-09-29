function toggleForm() {
    id = event.toElement.id
    if(id == 'button1'){
        document.getElementById('button1').style.display = "none";
        document.getElementById('form').style.display = "block"
    }
    if(id == 'button2'){
        document.getElementById('form').style.display = "none";
        document.getElementById('button1').style.display = "block";
    }
    
}