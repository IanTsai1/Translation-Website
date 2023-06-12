/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

/*
function toggleDropdown(event) {
    var dropdown = document.getElementById("myDropdown");
    if (event.target.classList.contains('dropdown-content')){
        dropdown.classList.toggle('show');
    } else {
        dropdown.classList.remove('show');
    }
}*/

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


