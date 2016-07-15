var postcss = require('gulp-postcss'),
    gulp = require('gulp'),
    autoprefixer = require('autoprefixer'),
    sass = require('gulp-sass'),
    rename = require("gulp-rename"),
    cssnano = require('cssnano');

gulp.task('sass', function () {
    return gulp.src('sass/main.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./css'));
});

gulp.task('css', function () {
    var processors = [
        autoprefixer({browsers: ['> 1%', 'last 2 version', 'IE 11']}),
        cssnano()
    ];
    return gulp.src('css/main.css')
        .pipe(postcss(processors))
        .pipe(rename("main.min.css"))
        .pipe(gulp.dest('./css'));
});

gulp.task('sass:watch', function () {
    gulp.watch('./sass/**/*.sass', ['sass'])
});