$(function (){
  var h1 = document.getElementById('title');
  h1.innerHTML = titles[randInt(0, titles.length)];

  // var date = document.getElementById('date');
  // date.innerHTML = ;

  $('input:radio[name="r"]').change(function (){
    window.location.reload();
  });
});

function randInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}