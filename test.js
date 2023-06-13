function handleFileSelect(event) {
    const file = event.target.files[0]; // Get the selected file

    // Display the file name on the page
    const fileNameDisplay = document.getElementById("file_name_display");
    fileNameDisplay.textContent = file.name;
    const fileSizeDisplay = document.getElementById('file_size_display');
    fileSizeDisplay.textContent = Math.round(file.size/1000) + " KB";

    //file.size;
  }
