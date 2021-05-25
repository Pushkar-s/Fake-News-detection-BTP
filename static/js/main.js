console.log("connected");
var code = document.getElementById("pycode")
var editor = CodeMirror.fromTextArea(code, {
    lineNumbers : true,
    styleActiveLine: true,
    matchBrackets: true,
    theme: "abcdef"
});
// editor.setOption("theme","abcdef");


async function runit() {
    
    var pythonCode = editor.getValue();
    // var pythonCode = document.getElementById('pycode').value 

    console.log(pythonCode)
    url = '/run'
    let data = {
        code : pythonCode
    }
    // const resp = await fetch(url, {
    //     method : 'POST',
    //     body : JSON.stringify(data),
    //     headers: {'Content-Type': 'application/json','Content-Length': data.length}    
    // });
    // const result = resp.json();
    // console.log(result)
    // var div = document.getElementById('output')
    // div.value= result
    // then(res => {
    //     console.log('hi')
    //     console.log(res.status)
    //     return res.text()
    // })
    // .then(data => {
    //     console.log(data)
    // })

    fetch(url, {
        method : 'POST',
        body : JSON.stringify(data),
        headers : {'Content-Type' : 'application/json', 'Content-Length' : data.length}
    })
    .then( a => a.json())
    .then( a => {
        console.log(a)
        var div = document.getElementById('output')
        div.value= a.output
        var diverr = document.getElementById('outputerr')
        diverr.value = a.error
    })


}
var btn = document.getElementById('runBtn')
btn.addEventListener('click',runit)




async function runmodel() {
    var strinp = document.getElementById("stringinput").value;
    var modtyp = document.getElementById("modeltype").value;
    url = '/runinput'
    console.log(strinp)
    let data = {
        str : strinp,
        mod : modtyp
    }
    // const resp = await fetch(url, {
    //     method : 'POST',
    //     body : JSON.stringify(data),
    //     headers : {
    //         'Content-Type': 'application/json',
    //         'Content-Length': data.length
    //     }
    // });
    // const result = resp.json();
    // console.log(result)
    // var div = document.getElementById('output')
    // div.value= result
    fetch(url, {
        method : 'POST',
        body : JSON.stringify(data),
        headers : {
            'Content-Type': 'application/json',
            'Content-Length': data.length
        }
    })
    .then(a => a.json())
    .then(a => {
        console.log(a)
        var div = document.getElementById('output')
        div.value= a.output
        var diverr = document.getElementById('outputerr')
        diverr.value = a.error
    })
}
var submodel = document.getElementById('runselectedmodel')
submodel.addEventListener('click',runmodel)