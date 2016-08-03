function loadTests() {
    alert("akjbfknsnf");
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/v1.0/tests";
    xhr.open('GET', url, true);
    
    xhr.send();
    alert("Hello");
    xhr.onload = function() {
        if (xhr.status === 200 && xhr.readyState === 4) {

            print("ok")
        } else {
            alert( 'Ошибка: ' + (this.status ? this.statusText : 'запрос не удался') );
        }
    }
}