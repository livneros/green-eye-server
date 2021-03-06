const SERVER_PATH = document.URL;
const INVALID_INPUT_MSG = "Please type a valid number, between 1 to 15."
const WAITING_MSG = "<br>Please wait while ae are processing your request...</br>"
const MIN_N_CLUSTERS = 1;
const MAX_N_CLUSTERS = 15;
function valid_n_clusters(n_clusters){
    if (isNaN(n_clusters) || parseInt(n_clusters) < MIN_N_CLUSTERS || parseInt(n_clusters) > MAX_N_CLUSTERS){
        alert(INVALID_INPUT_MSG);
        return false;
    }
    return true;
}

function loadImages() {
    loadNewResults();
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', SERVER_PATH , true)
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var n_clusters = document.getElementById('clusters_input').value;
    if(!valid_n_clusters(n_clusters)){return;}
    xhttp.send(JSON.stringify({n_clusters: n_clusters}));
    xhttp.onload = function()
        {
            if (this.status === 200){
                document.getElementById("loader").style.visibility = 'hidden';
                document.getElementById("images").innerHTML = this.responseText;
            }
        }
}
function loadNewResults(){
    document.getElementById('loader').style.visibility = 'visible';
    document.getElementById("images").innerHTML = '';
}
function clearText(id){
    document.getElementById(id).value = "";
}
