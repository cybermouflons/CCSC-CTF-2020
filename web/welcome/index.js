var express = require('express');
var mongoose = require('mongoose');

var UserSchema = new mongoose.Schema({
	name: String,
	user: String,
	pass: String
});

var User = mongoose.model('User', UserSchema);

[['Administrator', 'admin', 'KOtsios334454!!fdgfdg676565'], ['User', 'kotsios', 'kotsios8743435KK43432!!']].forEach(function (cred) {
	var instance = new User();

	instance.name = cred[0];
	instance.user = cred[1];
	instance.pass = cred[2];

	instance.save();
});

var app = express();

var publicDir = require('path').join(__dirname,'/public');
app.use(express.static(publicDir));

app.set('views', __dirname);
app.set('view engine', 'jade');

app.use(require('body-parser').urlencoded({extended: true}));

app.get('/', function(req, res) {
	res.render('index', {});
});

app.post('/', function(req, res) {
	User.findOne({user: req.body.user, pass: req.body.pass}, function (err, user) {
		if (err) {
			return res.render('index', {message: err.message});
		}

		if (!user) {
			return res.render('index', {message: 'Try again!'});
		}

		return res.render('index', {message: 'Welcome The witcher Geralt!!! Your Flag is CCSC{Auth3ntic@ti0n_w1th_N0_$QL_1s_FuN}'});
	});
});

var server = app.listen(35000, function () {
	mongoose.connect('mongodb://localhost/welcome');

	console.log('listening on port %d', server.address().port);
});

