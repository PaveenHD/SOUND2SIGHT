let selectedAudioFile = null;
let selectedStyle = null;
let selectedResolution = null;

function fileUpload() {
    document.getElementById('fileInput').addEventListener('change', function(event) {
        const file = event.target.files[0];
        const allowedTypes = ['audio/wav'];

        if (file && allowedTypes.includes(file.type)) {
            document.getElementById('text1').innerText = ""
            document.getElementById('fileinp').innerText = file.name + " has been uploaded"
            console.log('Audio File uploaded successfully:', file.name);
            selectedAudioFile = file;
        } else {
            document.getElementById('errorMessage').textContent = 'Please upload a valid WAV audio file.||The file is invalid';
            document.getElementById('errorMessage').style.display = 'block';
            event.target.value = '';
        }
    });
}

function processValues() {
    if (selectedAudioFile && selectedStyle && selectedResolution) {
        const audioFilename = selectedAudioFile.name;
        console.log( audioFilename, selectedStyle, selectedResolution);
        // playAudio(selectedAudioFile);
    } else {
        console.log('Please upload an audio file and select an art style and resolution.');
    }
}

document.getElementById('standardButton').addEventListener('click', function() {
    selectedResolution = 'Standard';
    processValues();
});

document.getElementById('hdButton').addEventListener('click', function() {
    selectedResolution = 'HD';
    processValues();
});

document.querySelectorAll('input[name="artStyle"]').forEach(input => {
    input.addEventListener('change', function() {
        selectedStyle = this.value;
    });
});

