var express = require('express');
var cors = require('cors')
var fs = require('fs');

var app = express();

app.use(cors())

app.get('/flag', function(req, res, next){
  res.send("Good job, the flag is: ccsc{eba43052b3fc1d5cdcf0a8809e0bdbdd}");
});

app.listen(1337);
