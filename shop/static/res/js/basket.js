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
        var basket = JSON.parse($.cookie('basket-price'));
        var newprice = 0;
        for(var i in basket.item){
            newprice += basket.price[i] * basket.count[i];
        }
        if(newprice){
            $('#basket-empty').hide();
            $('#basket-full').show();
            newprice = String(newprice) + ' грн.';
            $('#basket a u').html(newprice);
            $('#basket a').css({'visibility': 'visible'});
        } else {
            $('#basket-full').hide();
            $('#basket-empty').show();
            newprice = String(newprice) + ' грн.';
            $('#basket a').css({'visibility': 'hidden'});
        }

    }
});