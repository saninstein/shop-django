/**
 * Created by Alex on 16.07.2016.
 */

var arr = [];
var i = 0;
$(":checkbox").change(function(){
    if(this.checked){
        arr[i] = $(this).prop("name");
        i++;
    }else{
        var val = $(this).prop("name");
        var index = arr.indexOf(val);
        arr.splice(index, 1);
        i--;
    }
    $(".wrp").empty();
    $("#loading-img").show();
    var filter_str = "/ajax_phone_filter/";
    for(var i = 0; i < arr.length; i++){
        filter_str += arr[i] + "-";
    }
    alert(filter_str);

    $(".wrp").load(filter_str, function(){
        $("#loading-img").hide();
    });
});