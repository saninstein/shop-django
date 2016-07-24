/**
 * Created by шаша on 24.07.2016.
 */
$(document).ready(function () {
    $('#first-item').keyup(function(){
        if($(this).val().length >= 2){
            var value = $(this).val();
            var search_str = '/adminpanel/ajax_adm_search/' + value;
            $('#ci1').load(search_str, function(){
                $(this).show();
                $('#first-item').focusout(function(){
                    $('#ci1').hide(function(){
                        $(this).html("");
                    });
                });
            });
        } else{
           $('#ci1').hide(function(){
               $(this).html("");
           });
        }
        return false;
    });
    $('#second-item').keyup(function(){
        if($(this).val().length >= 2){
            var value = $(this).val();
            var search_str = '/adminpanel/ajax_adm_search/' + value;
            $('#ci2').load(search_str, function(){
                $(this).show();
                $('#second-item').focusout(function(){
                    $('#ci2').hide(function(){
                        $(this).html("");
                    });
                });
            });
        } else{
           $('#ci2').hide(function(){
               $(this).html("");
           });
        }
        return false;
    });
});
