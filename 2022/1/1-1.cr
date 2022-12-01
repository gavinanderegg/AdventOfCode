input = File.read("input.txt")

index = 0
elves = Hash(Int32, Int32).new(0)

input.each_line do |line|
  if line == ""
    index += 1
  else
    elves[index] += line.to_i32
  end
end

print elves.values.sort.last
