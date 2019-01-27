const SERVER_PATH = 'http://35.204.32.41:8080';

function loadImages() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', SERVER_PATH , true)
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var n_clusters = document.getElementById('clusters_input').value;
    console.log("n_clusters = ", n_clusters)
    validate_n_clusters(n_clusters);
    xhttp.send(JSON.stringify({n_clusters: n_clusters}));
    xhttp.onload = function()
        {
            if (this.status === 200){
                document.getElementById("images").innerHTML = this.responseText;
            }
        }
    xhttp.send();
}

export function validate_n_clusters(n_clusters){
    if (isNan(n_clusters) || parseInt(n_clusters) < 1 || parseInt(n_clusters > 20)){
        alert("Please type a valid number.");
    }
}