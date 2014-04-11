var express = require('express');
var app = express();

app.get('/', function(req,res){
	res.send('Under Construction');
});

var server = app.listen(3000, function(){
	console.log('Listening on port '+server.address().port);
}
