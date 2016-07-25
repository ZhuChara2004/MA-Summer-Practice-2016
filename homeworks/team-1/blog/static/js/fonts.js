var FontFaceObserver = require('fontfaceobserver');

var roboto = new FontFaceObserver('Roboto', {
        weight: 400
    })

roboto.check().then(function () {
    document.documentElement.classList.add('roboto');
}, function () {
	console.info('Web font could not be loaded in time. Falling back to system fonts.');
});