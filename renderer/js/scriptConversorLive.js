const video = document.getElementById('video');
const canvas = document.getElementById('canvasCamara');
const captura = document.getElementById('capturar');
const fs = require('fs');
var rp = require('request-promise');

var context = canvas.getContext('2d');

captura.addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480);
    guardarCanvas();
});

const variables = {
    audio: false,
    video: {
        width: 640,
        height: 480
    }
}

async function activarCamara() {
    fondo();
    try {
        const stream = await navigator.mediaDevices.getUserMedia(variables);
        handleSuccess(stream);
    } catch (e) {
        console.log(e.toString());
    }
}

function guardarCanvas() {
    var imagen = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
    fetch(imagen)
        .then(res => res.blob())
        .then(blob => {
            const file = new File([blob], 'imagen.png', blob);
            guardarImagen(file);
            detectar();
        })
}

function guardarImagen(imagen) {
    const archivosValidos = ['jpeg', 'jpg', 'png', 'webp'];
    var reader = new FileReader();
    reader.onloadend = function() {
        const archivo = reader.result.replace('data:image/octet-stream;base64,', "");
        const nombre = imagen.name.split('.');
        const extension = nombre[nombre.length - 1];

        if (!archivosValidos.includes(extension)) {
            return false;
        }

        let path = './renderer/images/imagen.png';

        fs.writeFile(path, archivo, 'base64', err => {
            if (err) {}
        });
    };
    reader.readAsDataURL(imagen);
}

function handleSuccess(stream) {
    window.stream = stream;
    video.srcObject = stream;
}

function fondo() {
    document.getElementById('botonSubmit').style.display = "none";
    document.getElementById('fondo').style.display = "none";
}

function detectar() {
    document.getElementById('cargando').style.display = "flex";

    const url = "../assets/pythonFiles/detector/runs/detect/exp/imagen.png?t=";
    const urlIf1 = "../assets/pythonFiles/web.txt?t=";
    const urlIf2 = "../assets/pythonFiles/web.html?t=";
    const urlImagen = "../../renderer/images/imagen.png";

    var options = {
        type: "POST",
        uri: "http://127.0.0.1:5000/detector",
        form: { value: urlImagen }
    }

    rp(options)
        .then(parsedBody => {
            var img = new Image();
            img.onload = function() {
                context.drawImage(img, 0, 0);
            };
            img.src = url + new Date().getTime();
            document.getElementById('if1').setAttribute('src', urlIf1 + new Date().getTime());
            document.getElementById('if2').setAttribute('src', urlIf2 + new Date().getTime());
            document.getElementById('cargando').style.display = "none";
            document.getElementById("botonGuardar").style.opacity = 1;
            document.getElementById("botonGuardar").disabled = false;
            return null;
        })
        .catch(err => {
            console.log(err);
            return null;
        });
}

document.getElementById("botonGuardar")
    .addEventListener("click", function() {
        const zip = new JSZip();

        fetch('../assets/pythonFiles/web.html')
            .then(res => res.arrayBuffer())
            .then(ab => {
                zip.file("web.html", ab);
                fetch('../assets/pythonFiles/style.css')
                    .then(res => res.arrayBuffer())
                    .then(ab => {
                        zip.file("style.css", ab);
                        zip.generateAsync({ type: "blob" }).then(function(content) {
                            saveAs(content, "conversorHTML.zip");
                        });
                    });
            });
    }, false);

document.querySelector('#botonSubmit').addEventListener('click', activarCamara);