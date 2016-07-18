/**
 * Created by шаша on 18.07.2016.
 */
var key = 'new';
$(document).ready(function(){
    $('.btn-new').click(function(){
    key = 'new';
    switcher();
});

$('.btn-popular').click(function(){
    key = 'pop';
    switcher();
});
});

function switcher(){
    alert(key)
  if(key == 'new'){
      $('#pop').hide();
      $('.btn-popular').addClass('notselected-btn');
      $('#news').show();
      $('.btn-new').removeClass('notselected-btn');
  } else if(key == 'pop'){
      $('#news').hide();
      $('.btn-new').addClass('notselected-btn');
      $('#pop').show();
      $('.btn-popular').removeClass('notselected-btn');
  }
};