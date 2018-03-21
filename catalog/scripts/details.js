$(function(context) {
    return function () {
        $(".thumbnails").mouseenter(function(){
            console.log("I love to buy intruments");
            $("#mainImage").attr("src",this.src);
        });
    }
}(DMP_CONTEXT.get()))
