function sendArticle() {
    var titreid = document.getElementById("titreidf").value;
    var identifiantid = document.getElementById("identifiantidf").value;
    var auteurid = document.getElementById("auteuridf").value;
    var dateid = document.getElementById("date_publicationidf").value;
    var paragrapheid = document.getElementById("paragrapheidf").value;
    if (titreid !== "" && identifiantid !== "" && auteurid !== ""  && dateid !== ""  && paragrapheid !== "" ) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 201 || xhr.status === 200) {
                } else {
                    console.log('Erreur avec le serveur');
                }
            }
        };

        xhr.open("POST", "/api/articles/", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify({titre:titreid, identifiant:identifiantid, auteur:auteurid, date:dateid, paragraphe:paragrapheid}));
    }
}

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
    $('#titreidf').keyup(function() {
        var identReplaceSpace = $(this).val();
        var identReplaceIllegalCar = identReplaceSpace.replace(/ /g, "-");
        var result = identReplaceIllegalCar.replace(/[^\w\s_-]/gi, "");
        var resultLower = result.toLowerCase();
        $("#identifiantidf").val(resultLower);
    });
}

function onTitreChange() {
    var identifiant = document.getElementById("identifiantidf").value;
    var nouveauIdentifiant = document.getElementById("identifiantidf");

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
