function handleFileSelect(event) {
    const file = event.target.files[0]; // Get the selected file
    localStorage.setItem("selectedFileName", file.name);
    localStorage.setItem("selectedFileSize", Math.round(file.size/1000) + " KB");
    window.location.href = 'after_file.html';
  }
