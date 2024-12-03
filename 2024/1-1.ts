const data = await Deno.readTextFile('./input/1.txt')
const lines = data.split('\n')

let left = []
let right = []

let distanceTotal = 0

lines.forEach((item) => {
	let numbers = item.split(/\s+/)

	left.push(numbers[0])
	right.push(numbers[1])
})

left.sort()
right.sort()

left.forEach((item, index) => {
	var distance = Math.abs(item - right[index])

	distanceTotal += distance
})

console.log(distanceTotal)
