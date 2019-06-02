function XMLget(type, url, value){
    var xmlhttp;
    if (window.XMLHttpRequest)
    {
        xmlhttp=new XMLHttpRequest();
    }
    else
    {
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }

    let easy = {
        'type': 1,
        'input': value
    };
    let re = {
        'type': 2,
        'input': value
    };

    var mode = null;

    if (type === 1){
        mode = easy;
    }
    else if (type === 2){
        mode = re;
    }
    else{
        alert("mode值错误")
    }

    mode = JSON.stringify(mode);
    xmlhttp.open("POST",url,true);
    xmlhttp.setRequestHeader("Content-type","application/json;charset=UTF-8")
    xmlhttp.send(mode);
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            document.getElementById('cards').innerHTML = '';
            let data = JSON.parse(xmlhttp.responseText);
            console.log(data);
            if (data['status'] == 'Succeed') {
                for (let item in data['data']) {
                    let card = document.createElement("div");
                    card.className = 'card';
                    let card_body = document.createElement("div");
                    card_body.className = 'card_body';

                    let title = document.createElement("h5");
                    title.className = 'card-title';
                    title.innerHTML = data['data'][item]['word'];

                    let unit = document.createElement("h6");
                    unit.className = 'card-text';
                    unit.innerHTML = data['data'][item]['unit'];

                    let ul = document.createElement("ul");
                    let translation = data['data'][item]['translation'];

                    for (let trans in translation){

                        let li = document.createElement("li");
                        let p = document.createElement("p");
                        p.className = "card-text";
                        p.innerHTML = translation[trans];
                        li.appendChild(p);
                        ul.appendChild(li);
                    }

                    card_body.appendChild(title);
                    card_body.appendChild(unit);
                    card_body.appendChild(ul);

                    card.appendChild(card_body);

                    document.getElementById('cards').appendChild(card)

                }
            }
            else{
                alert(data['status'])
            }

        }
    }
}
