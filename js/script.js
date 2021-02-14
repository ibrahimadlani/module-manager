var day = JSON.parse(json);

var container = document.getElementById("tablebody");

var d = new Date();
var n = d.toLocaleTimeString();


day.forEach(events => {
    var tr = document.createElement("tr");
    var a = document.createElement("td")
    a.innerText = events.debut + " à "+ events.fin;

    tr.appendChild(a);
    

    var b = document.createElement("td")
    b.innerText = events.type;
    tr.appendChild(b);
    
    var c = document.createElement("td")
    c.innerText = events.nom;
    tr.appendChild(c);

    var d = document.createElement("td")
    d.innerText = events.module;
    tr.appendChild(d);

    var e = document.createElement("td")
    e.innerText = events.prof;
    tr.appendChild(e);

    var e = document.createElement("td")
    e.innerText = events.exam;
    tr.appendChild(e);

    if(events.debut < n && events.fin > n){
        tr.classList = ["cours"];
    }else if (events.debut > n) {
        tr.classList = ["attente"];
    }else if (events.fin < n) {
        tr.classList = ["fini"];
    } 
    container.appendChild(tr);
});
