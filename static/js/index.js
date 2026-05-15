document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', document.getElementById('csvFile').files[0]);

    const response = await fetch('/upload-inventory', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('resultado').textContent = data.reporte;
});