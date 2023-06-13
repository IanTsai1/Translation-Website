document.addEventListener('click', function (event) {
    var dropdown = document.querySelector('.dropdown-menu');
    if (!event.target.closest('.dropdown')) {
      dropdown.classList.remove('show');
    }
  });

function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
        } else {
        a[i].style.display = "none";
        }
    }
}

document.addEventListener1('click', function (event) {
    var dropdown = document.querySelector('.dropdown-menu1');
    if (!event.target.closest('.dropdown1')) {
      dropdown.classList.remove('show');
    }
  });

function filterFunction1() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput1");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown1");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
        } else {
        a[i].style.display = "none";
        }
    }
}


document.getElementById("file_name").onclick = function () {
    //location.href = "www.yoursite.com";
    window.location.href = "after_file.html";
};

function handleButtonClick() {
    // Add your desired code or functionality here
    window.location.href = "before_file.html";
}

function handleFileSelect(event) {
    const file = event.target.files[0]; // Get the selected file
    localStorage.setItem("selectedFileName", file.name);
    localStorage.setItem("selectedFileSize", Math.round(file.size/1000) + " KB");
    window.location.href = 'after_file.html';
  }


