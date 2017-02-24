var jsdom = require('jsdom');
var jsonfile = require('jsonfile');
var fs = require('fs');
var request = require('request');
var imgDir = './images';
if (!fs.existsSync(imgDir)){
  fs.mkdirSync(imgDir);
}

jsdom.env("http://www.ratemypoo.com/xyzzy/search?search=10+am", function (err, window) {
  if (err) {
    console.error(err);
    return;
  }
  var $ = require("jquery")(window);

  $('center center tr').each(function (){
    var data = {};

    var fonts = $(this).find('font');
    data['title'] = $(fonts[0]).find('a')[0].innerHTML;

    var description = fonts[1].innerHTML;
    var lines = description.replace(/\s/g, "").split(/<.*?>/);
    for (var i = 0; i < lines.length; i++){
      if (lines[i] !== ''){
        var kv = lines[i].split(':');
        data[kv[0].toLowerCase()] = kv[1];
      }
    }

    var imgSrc = $(this).find('img')[0].src;
    data['imgSrc'] = imgSrc.replace('/t/', '/b/');

    // console.log(data);
    // console.log('');

    download(data['imgSrc'], data['title'] + '.jpg', function (){
      // console.log('downloaded ' + data['title'] + '.jpg');
    });

  });
});

var download = function(uri, filename, callback){
  request.head(uri, function (err, res, body){
    // console.log('content-type:', res.headers['content-type']);
    // console.log('content-length:', res.headers['content-length']);
    var path = imgDir + '/' + filename;
    var count = 1
    var duplicate;
    while (fs.existsSync(path)){
      duplicate = path + '(' + count + ')';
      count++;
    }
    if (duplicate){
      path = duplicate;
    }
    request(uri).pipe(fs.createWriteStream(path)).on('close', callback);
  });
};