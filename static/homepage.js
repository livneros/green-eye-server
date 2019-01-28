const SERVER_PATH = 'http://35.204.32.41:8080';

function validate_n_clusters(n_clusters){
    if (isNaN(n_clusters) || parseInt(n_clusters) < 1 || parseInt(n_clusters) > 15){
        alert("Please type a valid number.");
        return false;
    }
    return true;
}

function loadImages() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', SERVER_PATH , true)
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var n_clusters = document.getElementById('clusters_input').value;
    if(!validate_n_clusters(n_clusters)){return;}
    xhttp.send(JSON.stringify({n_clusters: n_clusters}));
    xhttp.onload = function()
        {
            if (this.status === 200){
                document.getElementById("images").innerHTML = this.responseText;
            }
        }
//    xhttp.send();
}

function clearText(id){
    document.getElementById(id).value = "";
}
