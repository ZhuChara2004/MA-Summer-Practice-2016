function loadTest() {
    $.getJSON("http://127.0.0.1:5000/api/v1.0/tests", function (data) {
        out = "";
        for (i = 0; i < data.length; i++) {
            out += "<p><label><a href='/'><input type='submit' name='answer' value=''>" + data[i].test + "</a></label></p>";
        }
        document.getElementById("listTests").innerHTML = out;
        document.getElementById("name").innerHTML = "Як Вам найкраще сприймати інформацію?";
    })
}