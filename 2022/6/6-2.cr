input = File.read("input.txt")

signal_buffer = [] of Char
signal_index = 0
buffer_size = 14

input.each_char_with_index do |char, index|
  signal_index = index

  if signal_buffer.size < buffer_size
    signal_buffer << char
    next
  else
    signal_buffer.delete_at(0, 1)
    signal_buffer << char
  end

  same = 0

  (0...signal_buffer.size).each do |x|
    unique_array = signal_buffer.select { |i| i == signal_buffer[x] }
    same += unique_array.size
  end

  if same == buffer_size
    break
  end
end

puts signal_index + 1