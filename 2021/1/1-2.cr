input = File.read("input.txt")

input_array = input.split
input_size = input_array.size

increases = 0
prev = 0
current = 0
line = 1

input_array.each do |data|
  if line + 2 <= input_size
    current = data.to_i + input_array[line].to_i + input_array[line + 1].to_i

    if current > prev && prev != 0
      increases += 1
    end
  end

  prev = current
  line += 1
end

puts increases