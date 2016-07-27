var gulp = require('gulp'),
	sass = require('gulp-sass'),
	cssnano = require('gulp-cssnano'),
	autoprefixer = require('autoprefixer'),
	postcss = require('gulp-postcss'),
	rename = require('gulp-rename')

gulp.task('css', function() {
	var processors = [
		autoprefixer({browsers: ['last 15 versions', '> 1%', 'ie 8', 'ie 7']}),
	];

	return gulp.src('static/sass/**/*.sass')
		.pipe(sass())		
		.pipe(postcss(processors))
		.pipe(gulp.dest('static/css'));
});

gulp.task('min', ['css'], function() {
	return gulp.src('static/css/main.css')
	.pipe(cssnano())
	.pipe(rename({suffix: '.min'}))
	.pipe(gulp.dest('static/css'))
})

gulp.task('watch', ['min'], function() {
	gulp.watch('static/sass/**/*.sass', ['css', 'min']);
});