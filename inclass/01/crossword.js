// http://www.nytimes.com/crosswords/game/mini

index = 0;
sindex = 0;
var string = 'lolcapitalism';
var boxes = document.querySelectorAll('div.guess');

function guess(){
  if (index > boxes.length - 1){
    index = 0;
  }

  if (sindex > string.length - 1){
    sindex = 0;
  }
  boxes[index].innerHTML = string[sindex];

  index++;
  sindex++;

  setTimeout(guess, 100);
}

guess();
