var jsdom = require('jsdom');
var jsonfile = require('jsonfile');
var directory = {};

jsdom.env("https://www.800-numbers.net/all-companies/", function (err, window) {
  if (err) {
    console.error(err);
    return;
  }
  var $ = require("jquery")(window);

  $('.list-inline.companies li a').each(function (){
    var name = '';
    if (this.innerHTML === ''){
      name = this.pathname.replace(/\//g,'');
    } else {
      name = this.innerHTML;
    }

    directory[name] = {
      'url': this.href,
      'nums': {}
    };

  });

  var keys = Object.keys(directory);
  console.log(keys.length + ' companies found');
  var promises = [];
  for (var i = 0; i < keys.length; i++){
    promises.push(getNums(directory[keys[i]], i).then(function (response){
      console.log((response + 1) + ' / ' + keys.length);
    }, function (err){
      console.log('promise err index ' + err);
    }));
  }

  Promise.all(promises).then(function (results){
    console.log('writing to directory.json');
    jsonfile.writeFile('800-numbers.json', directory, {spaces: 2}, function (err) {
      if (err){
        console.log('err writing json file');
      } else {
        console.log('done');
      }
    });
  });
});

function getNums(obj, index){
  return new Promise(function (resolve, reject){

    function getNumps(){
      jsdom.env(obj['url'], function (err, window) {
        if (err){
          reject(index);
        } else {
          var $ = require("jquery")(window);

          var re = /\d{3}.?\d{3}.?\d{4}/;
          var numps = $('p').filter(function (){
            return re.test($(this).text());
          });

          $(numps).each(function (){
            var s = $(this).text();
            obj['nums'][s.split(':')[0]] = s.match(re)[0];
          });

          // console.log(obj);
          resolve(index);
        }
      });
    }

    setTimeout(getNumps, index * 200);
  });
}
