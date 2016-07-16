/**
 * Created by Alex on 16.07.2016.
 */

var arr = [];
var price = [];
var i = 0;
var filt = function(){
    if($(':checkbox').checked){
        arr[i] = $(':checkbox').prop("name");
        i++;
    }else{
        var val = $(':checkbox').prop("name");
        var index = arr.indexOf(val);
        arr.splice(index, 1);
        i--;
    }
    $(".wrp").empty();
    $("#loading-img").show();

    var filter_str = "/ajax_phone_filter/";
    if(arr.length){
        arr.forEach(function(item, i, arr){
            filter_str += item;
            if(i != arr.length - 1){
                filter_str += "-";
            }
        });
        filter_str += 'p' + price[0] + '+' + price[1];
        filter_str += '/';
    } else{
        var filter_str = "/ajax_phone_filter/";
        filter_str += 'p' + price[0] + '+' + price[1];
        filter_str += '/';
    }


    setTimeout(function () {
        $(".wrp").load(filter_str, function(){
            $("#loading-img").hide();
        });
    }, 500);

};

$(":checkbox").change(filt());




$("#price_slider").ionRangeSlider({
    onFinish: function(data){
        price[0] = data['from'];
        price[1] = data['to'];
        filt();
    },
    onStart: function(data){
        price[0] = data['from'];
        price[1] = data['to'];
    },
    onChange: function(data){
        price[0] = data['from'];
        price[1] = data['to'];
    }

});