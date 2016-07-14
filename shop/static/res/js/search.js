/**
 * Created by Alex on 14.07.2016.
 */

$(document).ready(function(){
    $("#search").keyup(function(){
        var value = $(this).val();
            if(value.length >= 3){
                alert(value);
            }

    });
});


