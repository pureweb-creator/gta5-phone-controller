var gulp = require('gulp')
var bs = require("browser-sync").create()

gulp.task('serve', function(){
    bs.init({
        server: {
            baseDir: "./templates"
        },
        port: 3000,
        open: "external"
    })

    gulp.watch("./templates/index.html").on('change', bs.reload);

})

gulp.task('default', gulp.series('serve'))