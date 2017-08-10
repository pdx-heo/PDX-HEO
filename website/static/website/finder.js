function filterShelters() {
  
}

function filterFood() {
  
}

function filterHealthcare() {
  
}

function filterOutOrganizations() {
  var filter = "Organization";
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.indexOf(filter) > -1) {
        tr[i].style.display = "none";
      }
      else {
        tr[i].style.display = "";
      }
    }
  }

  setButtonInactive("organizations_button");
  setButtonActive("services_button");
  setButtonActive("all_button");
  setButtonInactive("shelters_button");
  setButtonInactive("food_button");
  setButtonInactive("healthcare_button");
}

function filterOutServices() {
  var filter = "Organization";
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.indexOf(filter) > -1) {
        tr[i].style.display = "";
      }
      else {
        tr[i].style.display = "none";
      }
    }
  }

  setButtonActive("organizations_button");
  setButtonInactive("services_button");
  setButtonDisabled("all_button");
  setButtonDisabled("shelters_button");
  setButtonDisabled("food_button");
  setButtonDisabled("healthcare_button");
}

function setButtonActive(button) {
  document.getElementById(button).className = "pure-button";
  document.getElementById(button).classList.add("pure-button-active", "pure-button-primary");
}

function setButtonInactive(button) {
  document.getElementById(button).className = "pure-button";
}

function setButtonDisabled(button) {
  document.getElementById(button).className = "pure-button";
  document.getElementById(button).classList.add("pure-button-disabled")
}