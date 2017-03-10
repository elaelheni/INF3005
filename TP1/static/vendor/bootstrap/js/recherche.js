

function test() {
    var len = $('.requi :input,textarea').filter(function() {
        return !$(this).val();
    }).length;
    $('#modifButton').prop('disabled', !!len);
}

function recherche() {
    $('#recherButton').attr('disabled',true);
    $('#rechercheid').keyup(function(){
        if($(this).val().length !=0)
            $('#recherButton').attr('disabled', false);
        else
            $('#recherButton').attr('disabled',true);
    })
}

$(document).ready(function(){
    $('.dd input,textarea').keyup(test);
    recherche();
});
