input = File.read("input.txt")

input_array = input.split

ones_array = Array(Int32).new
zeros_array = Array(Int32).new

input_array.each_with_index do |data, i|
  bits = data.split("")

  bits.each_with_index do |bit, j|
    if i == 0
      if bit.to_i == 1
        ones_array << 1
        zeros_array << 0
      else
        ones_array << 0
        zeros_array << 1
      end
    else
      if bit.to_i == 1
        ones_array[j] += 1
      else
        zeros_array[j] += 1
      end
    end
  end
end

gamma_array = Array(Int32).new
epsilon_array = Array(Int32).new

(0...ones_array.size).to_a.each do |i|
  if ones_array[i] > zeros_array[i]
    gamma_array << 1
    epsilon_array << 0
  else
    gamma_array << 0
    epsilon_array << 1
  end
end

gamma = gamma_array.join("").to_i(2)
epsilon = epsilon_array.join("").to_i(2)

puts gamma * epsilon
