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
		var smallest = {'size': 10000000, 'char': ''};

		Object.keys(char).forEach(function(key) {
			if (char[key] < smallest.size) {
				smallest.size = char[key];
				smallest.char = key;
			}
		});

		console.log(smallest.char);
	}
});

// rwqoacfz