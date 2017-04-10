
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

function identifiantReplaceSpace() {
    $('#titreid').keyup(function() {
        var identReplaceSpace = $(this).val();
        var result = identReplaceSpace.replace(/ /g, "_");
        var resultLower = result.toLowerCase();
        $("#identifiantid").val(resultLower);
    });
}

function onTitreChange() {
    var identifiant = document.getElementById("identifiantid").value;
    var nouveauIdentifiant = document.getElementById("identifiantid");

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                nouveauIdentifiant.value = xhr.responseText;
            } else {
                console.log('Erreur avec le serveur');
            }
        }
    };

    xhr.open("GET", "/ident/"+identifiant, true);
    xhr.send();
}

$(document).ready(function(){
    identifiantReplaceSpace();
    modifadmin();
    recherche();
});
