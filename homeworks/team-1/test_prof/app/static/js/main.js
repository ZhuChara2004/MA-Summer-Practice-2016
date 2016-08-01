function loadTests() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    
    xhr.send();

    xhr.onload = function() {
        if (xhr.status === 200 && xhr.readyState === 4) {
            alert("OK");
            
        } else {
            alert( 'Ошибка: ' + (this.status ? this.statusText : 'запрос не удался') );
        }
    }
}