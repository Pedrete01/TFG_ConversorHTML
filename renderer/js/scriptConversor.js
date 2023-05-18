const fs = require('fs');
const express = require('express');
const JSZip = require('jszip');
const saveAs = require('file-saver');
const { request } = require('http');
var rp = require('request-promise');
var app = express();

const form = document.querySelector('.conversorBody');

function loadImage(e) {
    const file = e.target.files[0];

    if (!isFileImage(file)) {
        alert('Please select an image file');
        return;
    }

    const url = window.URL.createObjectURL(file);

    document.getElementById('imagen').setAttribute('src', url);

    guardarImagen();

    document.getElementById("botonImg").style.opacity = 1;
    document.getElementById("botonImg").disabled = false;
}

function isFileImage(file) {
    const acceptedImageTypes = ['image/jpeg', 'image/png'];
    return file && acceptedImageTypes.includes(file['type'])
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
            document.getElementById('imagenResultado').setAttribute('src', url + new Date().getTime());
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

function guardarImagen() {
    const archivosValidos = ['jpeg', 'jpg', 'png', 'webp'];
    const imagen = cargarImagen();

    var reader = new FileReader();
    reader.onloadend = function() {
        const archivo = reader.result.replace('data:application/octet-stream;base64,', "");
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

function cargarImagen() {
    var output = document.getElementById('img').files[0];
    var imagefile = new File([output], output.name);
    return imagefile;
}

document.querySelector('#img').addEventListener('change', loadImage);
document.querySelector('#botonImg').addEventListener('click', detectar);