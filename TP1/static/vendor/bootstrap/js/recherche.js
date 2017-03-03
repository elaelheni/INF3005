$(document).ready(function(){
    $('#recherButton').attr('disabled',true);
    $('#rechercheid').keyup(function(){
        if($(this).val().length !=0)
            $('#recherButton').attr('disabled', false);
        else
            $('#recherButton').attr('disabled',true);
    })
});
