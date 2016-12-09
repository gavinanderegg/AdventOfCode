var _ = require('./lodash');

var lineReader = require('readline').createInterface({
	input: require('fs').createReadStream('input')
});

lineReader.on('line', function (line) {


	console.log('Line from file:', line);

	process.exit();
});

