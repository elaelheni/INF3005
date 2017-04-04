// Copyright 2017 Jacques Berger
//
function onPaysChange() {
    var champProvince = document.getElementById("champ-province");

    var pays = document.getElementById("champ-pays").value;
    if (pays === "") {
        champProvince.value = "";
        champProvince.disabled = true;
    } else {
        champProvince.disabled = false;

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    champProvince.innerHTML = xhr.responseText;
                    champProvince.value = "";
                } else {
                    console.log('Erreur avec le serveur');
                }
            }
        };

        xhr.open("GET", "/provinces/"+pays, true);
        xhr.send();
    }
    var champVille = document.getElementById("champ-ville");
    champVille.value = "";
    champVille.disabled = true;
}

// Lancée lorsque la province change. Met la liste des villes à jour.
function onProvinceChange() {
    var champVille = document.getElementById("champ-ville");

    var province = document.getElementById("champ-province").value;
    if (province === "") {
        champVille.value = "";
        champVille.disabled = true;
    } else {
        champVille.disabled = false;

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    champVille.innerHTML = xhr.responseText;
                    champVille.value = "";
                } else {
                    console.log('Erreur avec le serveur');
                }
            }
        };

        xhr.open("GET", "/villes/"+province, true);
        xhr.send();
    }
}

function sendPays() {
    var pays = document.getElementById("nouveau_pays").value;
    if (pays !== "") {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 201) {
                    alert('Pays ajouté à la liste');
                } else {
                    console.log('Erreur avec le serveur');
                }
            }
        };

        xhr.open("POST", "/api/pays/", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify({nom:pays}));
    }
}