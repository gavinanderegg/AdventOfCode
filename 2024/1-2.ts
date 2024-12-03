const data = await Deno.readTextFile('./input/1.txt')
const lines = data.split('\n')

let left = []
let right = {}

let similarityTotal = 0

lines.forEach((item) => {
	let numbers = item.split(/\s+/)

	left.push(numbers[0])

	let count = right[numbers[1]] ?? 0
	count += 1
	right[numbers[1]] = count
})

left.forEach((item, index) => {
	var similarity = item *= (right[item] ?? 0)

	similarityTotal += similarity
})

console.log(similarityTotal)
