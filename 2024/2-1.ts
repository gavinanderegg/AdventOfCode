const data = await Deno.readTextFile('./input/2.txt')
const lines = data.split('\n')

var safeCount = 0

lines.forEach((item) => {
	let nums = item.split(' ').map((num) => Number(num))
	let lastNum = null
	var isSafe = true
	var direction = 0

	nums.forEach((num, iter) => {
		var newDirection = 0

		if (isSafe === true) {
			if (lastNum === null) {
				lastNum = num
				return

			} else {
				if (direction === 0) {
					direction = num - lastNum
					direction = direction / Math.abs(direction)

					if (Math.abs(num - lastNum) > 3 || Math.abs(num - lastNum) < 1) {
						isSafe = false
						return
					}

					lastNum = num

					return

				} else {
					newDirection = num - lastNum
					newDirection = newDirection / Math.abs(newDirection)

					if (newDirection !== direction) {
						isSafe = false
						return
					}

					if (Math.abs(num - lastNum) > 3 || Math.abs(num - lastNum) < 1) {
						isSafe = false
						return
					}

					lastNum = num

					if (iter === (nums.length - 1)) {
						safeCount += 1
					}
				}
			}
		}
	})
})

console.log(safeCount)
