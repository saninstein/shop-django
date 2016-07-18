/**
 * Created by шаша on 18.07.2016.
 */
$(document).ready(function(){
    if($.cookie('liked') == null){
        alert("as");
        $('.fa-heart').css("color", "#FFE566");
    }
});