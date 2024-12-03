const data = await Deno.readTextFile('./input/3.txt')

let newString = ''
let currentOffset = 0

const slice = [...data.matchAll(/don't\(\).*?do\(\)/gm)]

slice.forEach((item) => {
	newString += data.slice(currentOffset, item.index)

	currentOffset = currentOffset + item.index + item[0].length
})

newString += data.slice(currentOffset, data.length)

console.log(newString)

const matches = [...newString.matchAll(/mul\((\d+),(\d+)\)/gm)]

let total = 0

matches.forEach((item) => {
	total += item[1] * item[2]
})

console.log(total)
