const data = await Deno.readTextFile('./input/3.txt')

const matches = [...data.matchAll(/mul\((\d+),(\d+)\)/gm)]

let total = 0

matches.forEach((item) => {
	total += item[1] * item[2]
})

console.log(total)
