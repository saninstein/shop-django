$(document).ready(function(){
   $('#buy-btn').click(function(){
       var count = Math.abs($('#buy-count').val())
       if(!count){
           count = 1;
       }
       var basket_price = parseFloat($.cookie('basket-price'));
       if(basket_price){
            basket_price += count * parseFloat($('#buy-btn').data('price'));
            $.cookie('basket-price', basket_price,{
                expire: 30,
                path: '/',
            });
       } else{
            $.cookie('basket-price', count * parseFloat($('#buy-btn').data('price')),{
                expire: 30,
                path: '/',
            });
       }
       $(document).trigger('cookieUpdate');


       $.post(
           '/ajax_addbasket/',
           {
               item: $('#buy').data('item'),
               count: count
           }
       );
   });
});
