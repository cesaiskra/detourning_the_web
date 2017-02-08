var jsdom = require('jsdom');
var fs = require('fs');
var allText = '';

var letters = 'abcdefghijklmnopqrstuvwxyz';
var promises = [];
for (var i = 0; i < letters.length; i++){
  promises.push(
    getDiseases(letters[i], i).then(function (response){
      console.log('got diseases starting with ' + response);
    }, function (err){
      console.log('promise rejected on ' + err);
    })
  );
}

Promise.all(promises).then(function (results){
  console.log('got all diseases');
  fs.writeFile('cdc.txt', allText, 'utf8', function (){
    console.log('written to cdc.txt');
  });
});

function getDiseases(letter, index){
  return new Promise(function (resolve, reject){
    function scrape(){
      var url = 'https://www.cdc.gov/diseasesconditions/az/' + letter + '.html';
      
      jsdom.env(url, function (err, window) {
        if (err) {
          reject(letter);
        }
        var $ = require("jquery")(window);

        $('div.span16 a').each(function (){
          var text = $(this).text();
          if (text.indexOf('see also') !== 0){
            if (text.indexOf(' — see ') >= 0){
              allText += text.split(' — see ')[0] + '\n';
            } else if (text.indexOf(' - see ') >= 0){
              allText += text.split(' - see ')[0] + '\n';
            } else {
              allText += text + '\n';
            }
            resolve(letter);
          }
        });
      });
    }
    
    setTimeout(scrape, index * 200);
  });
}
