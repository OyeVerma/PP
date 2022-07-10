$(document).ready(function(){
    $('.input').on('change', function(){
        let value = $(this).val();
        if (value.length) {
            $(this).addClass('input-active');
            $(this).parent().children('label').addClass('label-active');
        } else {
            $(this).removeClass('input-active');
            $(this).parent().children('label').removeClass('label-active');
    
        })
})