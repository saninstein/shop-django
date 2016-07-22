/**
 * Created by шаша on 22.07.2016.
 */
$(document).ready(function(){
    $('.fa-times').click(function(){
        var item = $(this).data('item');
        var csrf = $('input[name=csrfmiddlewaretoken]').val()


        $.post(
            "/adminpanel/ajax_delete/",
            {
                item: item,
                csrfmiddlewaretoken: csrf
            },
            function(data){
                location.reload(true);
            }

        );
    });
});