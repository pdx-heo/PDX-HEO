/*
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitra Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 */


function search() {
  var input = document.getElementById("search_field");
  var filter = input.value.toUpperCase();
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 1; i < tr.length; i++) {
    var tds = tr[i].getElementsByTagName("td");
    var j;

    var tr_match = false;
    for (j = 0; j < tds.length; j++) {
      var td = tds[j];
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr_match = true;
        break;
      }
    }

    if (tr_match) {
      tr[i].style.display = "";
    }
    else {
      tr[i].style.display = "none";
    }
  }
}

function filter(filter) {
  filter = filter.toUpperCase();
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      }
      else {
        tr[i].style.display = "none";
      }
    }
  }
}

function filterOut(filter) {
  filter = filter.toUpperCase();
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "none";
      }
      else {
        tr[i].style.display = "";
      }
    }
  }
}

function filterClear() {
  var table = document.getElementById("finder_table");
  var tr = table.getElementsByTagName("tr");
  var i;
  for (i = 0; i < tr.length; i++) {
    tr[i].style.display = "";
  }
}

function allSearch() {
  filterClear();
  filterOut("Organization");

  setButtonActive("services_button");
  setButtonActive("all_button");
  setButtonInactive("shelters_button");
  setButtonInactive("food_button");
  setButtonInactive("health_button");
}

function shelterSearch() {
  filter("Shelter");

  setButtonActive("services_button");
  setButtonInactive("all_button");
  setButtonActive("shelters_button");
  setButtonInactive("food_button");
  setButtonInactive("health_button");
}

function foodSearch() {
  filter("Food");

  setButtonActive("services_button");
  setButtonInactive("all_button");
  setButtonInactive("shelters_button");
  setButtonActive("food_button");
  setButtonInactive("health_button");
}

function healthSearch() {
  filter("Healthcare");

  setButtonActive("services_button");
  setButtonInactive("all_button");
  setButtonInactive("shelters_button");
  setButtonInactive("food_button");
  setButtonActive("health_button");
}


function serviceSearch() {
  if (document.getElementById("services_button").classList.contains("pure-button-active")) {
    filterClear();

    setButtonInactive("organizations_button");
    setButtonInactive("services_button");
    setButtonInactive("all_button");
    setButtonInactive("shelters_button");
    setButtonInactive("food_button");
    setButtonInactive("health_button");

  } else {
    filterOut("Organization");

    setButtonInactive("organizations_button");
    setButtonActive("services_button");
    setButtonActive("all_button");
    setButtonInactive("shelters_button");
    setButtonInactive("food_button");
    setButtonInactive("health_button");
  }
}

function organizationSearch() {
  if (document.getElementById("organizations_button").classList.contains("pure-button-active")) {
    filterClear();

    setButtonInactive("organizations_button");
    setButtonInactive("services_button");
    setButtonInactive("all_button");
    setButtonInactive("shelters_button");
    setButtonInactive("food_button");
    setButtonInactive("health_button");

  } else {
    filter("Organization");

    setButtonActive("organizations_button");
    setButtonInactive("services_button");
    setButtonDisabled("all_button");
    setButtonDisabled("shelters_button");
    setButtonDisabled("food_button");
    setButtonDisabled("health_button");
  }
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