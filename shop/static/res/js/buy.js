$(document).ready(function(){
   $('#buy-btn').click(function(){
       var basket_price = parseFloat($.cookie('basket-price'));
       if(basket_price){
            basket_price += parseFloat($('#buy-btn').data('price'));
            $.cookie('basket-price', basket_price);
       } else{
            $.cookie('basket-price', parseFloat($('#buy-btn').data('price')));
       }
       $(document).trigger('cookieUpdate');

       $.post(
           '/ajax_addbasket/',
           {
               item: $('#buy').data('item')
           }
       );
   });
});
