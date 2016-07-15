var FontFaceObserver = require('fontfaceobserver');

var font = new FontFaceObserver('My Family', {
  weight: 400
});

font.load().then(function () {
  console.log('Font is available');
}, function () {
  console.log('Font is not available');
});