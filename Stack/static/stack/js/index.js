$(document).ready(function(){

    $('.input').on('change', function(){
        let value = $(this).val();
        if (value.length) {
            $(this).addClass('input-active');
            $(this).parent().children('label').addClass('label-active');
        } else {
            $(this).removeClass('input-active');
            $(this).parent().children('label').removeClass('label-active');
        }})

        let newformcheckbox = $('#stackEventNewInput')
        let newform = $('.stackEventNewForm')
        
        newform.hide()
        newformcheckbox.on('change', function(){
            if (newformcheckbox.checked) {
                newform.show()
            } else {
                newform.hide()
            }
        })
        
        $('.stackEventEdit').hide()
        $('.stackEventText').click(function(){
            $(this).parent().children('.stackEventEdit').toggle()
        })
        
        $('#stackEventFormBtn').click(function(){
            $('#id_text').text('')
        })
        
        $('.stackBody').on('DOMTreeModified', function(){
            console.log('changed')
            $('.stackEventEdit').hide()
        })

        Mousetrap.bind('=', function(){
            console.log('clicked')
            $('#stack-create-anchor').click()
        });
    })

// Stack-Detail