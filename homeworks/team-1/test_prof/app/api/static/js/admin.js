function addAnswer() {
	$(".answers").append("<p><input type='text' placeholder='Відповідь' class='input-answer'></p>");
}

function addQuestion() {
	$("#questions").append("<div id='question'><div id='answers' telnum='' class='answers'><p><input type='text' placeholder='Назва запитання'></p><p><input type='text' placeholder='Відповідь' class='input-answer'></p><p><input type='text' placeholder='Відповідь' class='input-answer'></p></div><button class='button' onclick='addAnswer()'>Додати відповідь</button></div>");
}