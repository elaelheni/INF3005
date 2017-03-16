
function modifadmin() {
$('.requi input,textarea').keyup(function(){
  var lengthT = $('input[name=titre]').val().length;
  var lengthP = $('textarea[name=paragraphe]').val().length;

  $('#modifButton').prop('disabled', lengthT < 1 || lengthP < 1 || lengthT > 100 || lengthP > 500);
});
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
    modifadmin();
    recherche();
});
