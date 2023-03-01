document.querySelectorAll(".fileInput").forEach(inputElement =>{

    const dropZoneElement = inputElement.closest(".fileDrop");

    dropZoneElement.addEventListener("click", e => {
        inputElement.click(); 
    });

    inputElement.addEventListener("change", e => {
        if (inputElement.files.length) {
            updateThumbnail(dropZoneElement, inputElement.files[0]);
        }
    });

    dropZoneElement.addEventListener("dragover", e=> {
        dropZoneElement.classList.add("fileDropDropped");
        e.preventDefault();
    });

    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, e => {
            dropZoneElement.classList.remove("fileDropDropped");
        });
    });

    dropZoneElement.addEventListener("drop", e =>{
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            inputElement.files = e.dataTransfer.files;
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }

        dropZoneElement.classList.remove("fileDropDropped");
    });
});

function updateThumbnail(dropZoneElement, file){
    let thumbnailElement = dropZoneElement.querySelector(".fileThumb");

    if (dropZoneElement.querySelector(".fileDropPrompt")){
        dropZoneElement.querySelector(".fileDropPrompt").remove();
    }

    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("fileThumb");
        dropZoneElement.appendChild(thumbnailElement);
    }

    thumbnailElement.dataset.label = file.name;

    if (file.type.startsWith("image/")){
        const reader = new FileReader();

        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
        };
    } else {
        thumbnailElement.style.backgroundImage = null;
    }

}