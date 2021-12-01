input = File.read("input.txt")

increases = 0
prev = 0

input.each_line do |line|
  current = line.to_i

  if current > prev && prev != 0
    increases += 1
  end

  prev = current
end

puts increases