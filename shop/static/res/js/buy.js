$(document).ready(function(){
   $('#buy-btn').click(function(){
       var count = Math.abs($('#buy-count').val())
       if(!count){
           count = 1;
       }
       var price;
       if(count > 1){
           if($('#buy-btn').data('price_opt')){
               price = parseFloat($('#buy-btn').data('price_opt'));
           } else{
               price = parseFloat($('#buy-btn').data('price'));
           }
       } else{
           price = parseFloat($('#buy-btn').data('price'));
       }

       var basket_price = $.cookie('basket-price');
       if(basket_price){
            basket_price += count * parseFloat($('#buy-btn').data('price'));
            $.cookie('basket-price', basket_price,{
                expire: 30,
                path: '/',
            });
       } else{
           var basket = {

           };
           $.cookie('basket-price', "",{
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
