
function loadImages() {
  var xhttp = new XMLHttpRequest();

//  xhttp.onreadystatechange = function() {
//	console.log(this);
//	console.log("status = ", this.status);
//    if (this.readyState == 4 && this.status == 200) {
//		document.getElementById("centers").innerHTML = this.responseText;
//		console.log(this.respoonseText);
//    }
//  };
//  xhttp.open("POST", "localhost:5000/", true);
//  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
//  xhttp.send(JSON.stringify({n_clusters: 3}));
//    console.log("inside request")
//    xhttp.open("GET", "localhost:5000/", true);
//    xhttp.send();
    //Call the open function, GET-type of request, url, true-asynchronous
    xhttp.open('POST', 'http://0.0.0.0:8080', true)
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({n_clusters: 3}));
    //call the onload
    xhttp.onload = function()
        {
            //check if the status is 200(means everything is okay)
            if (this.status === 200)
                {
                    //return server response as an object with JSON.parse
                    console.log(JSON.parse(this.responseText));
        }
                }
    //call send
    xhttp.send();
}
