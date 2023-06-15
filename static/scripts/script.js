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
    window.location.href = "after_file.html";
};

function handleButtonClick() {
    window.location.href = "before_file.html";
}

function handleFileSelect(event) {
    const file = event.target.files[0]; // Get the selected file
    localStorage.setItem("selectedFileName", file.name);
    /*
      Math.round((file.size/1000)*10)/10
    */
    var file_size = file.size/1000;
    if(file_size < 1){
      localStorage.setItem("selectedFileSize", Math.round((file.size/1000)*10)/10 + " KB");
    }
    else{
      localStorage.setItem("selectedFileSize", Math.round(file.size/1000) + " KB");
    }

  }

function front_file(event){
    window.location.href = 'before_file.html';
}
function text_file(event){
    window.location.href = 'site.html';
}


function selectLang(event) {
  //let translationType;
  let selectedLanguage = String(event.target.id);
  // Make a fetch request to send the selected language to the server
  fetch('/language', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({lang:selectedLanguage})
  })
    .then(response => {
      if (response.ok) {
        console.log('Language selection sent successfully!');
        // Do something with the response if needed
      } else {
        console.error('Error sending language selection.');
      }
    })
    .catch(error => {
      console.error('Error sending language selection:', error);
    });
}

function getBeforeTranslate(event){
  var textarea = document.getElementById("before_translate");
  var before_trans = textarea.value;

  var after_trans = document.getElementById("after_translate1");

  // Make a fetch request to send the selected language to the server
  fetch('/before_translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({beforeTranslateText:before_trans})
  })
    .then(response => {
      if (response.ok) {
        console.log('Before translated text sent successfully!');
        // Do something with the response if needed
      } else {
        console.error('Error sending text.');
      }
    })
    .catch(error => {
      console.error('Error sending text:', error);
    });

    fetch('/before_translate')
    .then(response => response.text())
    .then(text => (after_trans.innerHTML = text));
}

/*
function getText(event){
  var textarea = document.getElementById("from_detected_language");
  var text = textarea.value;
  //const text = event.target.value;

  fetch('/before_translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({beforeTranslateText:text})
    })
    .then(response => {
      if (response.ok) {
        console.log('Before translated text sent successfully!');
        // Do something with the response if needed
      } else {
        console.error('Error sending text.');
      }
    })
    .catch(error => {
      console.error('Error sending text:', error);
    });
    fetch('/detected-language')
    .then(response => response.text())
    .then(text => (textarea.innerHTML = text));
}
*/






