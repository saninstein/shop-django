/**
 * Created by шаша on 19.07.2016.
 */
$(document).ready(function(){
    if($.cookie('basket-price')){
        updateBasketPrice();
    }

    $(document).on('cookieUpdate', function(){
        updateBasketPrice();
    });

    function updateBasketPrice(){
        $('#basket-empty').hide();
        $('#basket-full').show();
        var newprice = $.cookie('basket-price');
        newprice += ' грн.';
        $('#basket a u').html(newprice);
        $('#basket a').css({'visibility': 'visible'});
    }
});