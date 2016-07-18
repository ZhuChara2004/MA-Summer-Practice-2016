var postcss = require('gulp-postcss'),
    gulp = require('gulp'),
    autoprefixer = require('autoprefixer'),
    sass = require('gulp-sass'),
    rename = require("gulp-rename"),
    cssnano = require('cssnano');

gulp.task('sass', function () {
    return gulp.src('./flask_blog/sass/main.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./flask_blog/static'));
});

gulp.task('css', function () {
    var processors = [
        autoprefixer({browsers: ['> 1%', 'last 2 version', 'IE 11']}),
        cssnano()
    ];
    return gulp.src('./flask_blog/static/main.css')
        .pipe(postcss(processors))
        .pipe(rename("main.min.css"))
        .pipe(gulp.dest('./flask_blog/static'));
});

gulp.task('sass:watch', function () {
    gulp.watch('./sass/**/*.sass', ['sass'])
});