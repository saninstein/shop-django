/**
 * Created by шаша on 22.07.2016.
 */
$(document).ready(function(){
    $('.fa-times').click(function(){
        var item = alert($(this).data('item'));
        var csrf = alert($(this).data('csrf'));

        
        $.post(
            "/adminpanel/delete/",
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