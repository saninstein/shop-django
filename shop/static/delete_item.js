/**
 * Created by шаша on 22.07.2016.
 */
$(document).ready(function(){
    $('.fa-times').click(function(){
        alert($(this).data('item'));
        alert($('input[name=csrfmiddlewaretoke]').val());
    });
});