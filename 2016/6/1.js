var rl = require('readline').createInterface({
	input: require('fs').createReadStream('input')
});

var chars = [];

rl.on('line', (line) => {
	var pos = 0;

	for (var char of line) {
		if (chars[pos] == undefined) {
			chars[pos] = {};
		}

		if (chars[pos][char] == undefined) {
			chars[pos][char] = 1;
		} else {
			chars[pos][char] += 1;
		}

		pos++;
	}
});

rl.on('close', () => {
	for (var char of chars) {
		var biggest = {'size': 0, 'char': ''};

		Object.keys(char).forEach(function(key) {
			if (char[key] > biggest.size) {
				biggest.size = char[key];
				biggest.char = key;
			}
		});

		console.log(biggest.char);
	}
});

// umcvzsmw