var cDiv = document.getElementById('checkboxes');
var dDiv = document.getElementById('diagnoses');

var dd = document.getElementById('definitely-div');
var pd = document.getElementById('probably-div');
var md = document.getElementById('might-div');
var cd = document.getElementById('could-div');

var du = document.getElementById('definitely-ul');
var pu = document.getElementById('probably-ul');
var mu = document.getElementById('might-ul');
var cu = document.getElementById('could-ul');

var divs = [dd, pd, md];
var lists = [du, pu, mu];

for (var i = 0; i < asymptomatics.length; i++){
  var li = document.createElement('li');
  li.innerHTML = asymptomatics[i];
  cu.appendChild(li);
}

var count = 0;
for (var key in symptoms){
  if (symptoms.hasOwnProperty(key)){
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.className = 'cbox';
    checkbox.value = key;

    var label = document.createElement('label');
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(key));
    cDiv.appendChild(label);
    $(label).after('<br>');
    count++;
  }
}

$('.cbox').click(function (){
  for (var k = 0; k < lists.length; k++){
    lists[k].innerHTML = '';
  }

  var diagnoses = [];

  $('.cbox:checked').each(function (){
    var causes = symptoms[this.value]['causes'];
    $.merge(diagnoses, causes);
  });

  diagnoses.sort();

  var count = 1;
  for (var i = 0; i < diagnoses.length; i++){
    if (diagnoses[i] == diagnoses[i + 1]){
      count++;
    } else {
      var li = document.createElement('li');
      li.innerHTML = diagnoses[i];

      switch (count){
        case 1:
          mu.appendChild(li);
          break;
        case 2:
          pu.appendChild(li);
          break;
        default:
          du.appendChild(li);
          break;
      }
      count = 1;
    }
  }

  var still = false;
  for (var j = 0; j < divs.length; j++){
    if (lists[j].children.length > 0){
      still = true;
      divs[j].removeAttribute('style');
    } else {
      divs[j].style.display = 'none';
    }
  }

  if (still){
    document.getElementById('could-h3').innerHTML = 'You could still have:';
  } else {
    document.getElementById('could-h3').innerHTML = 'You could have:';
  }
});
