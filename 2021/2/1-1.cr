input = File.read("input.txt")

forward = 0
depth = 0

input.each_line do |data|
  instruction = data.split(" ")

  case instruction[0]
  when "forward"
    forward += instruction[1].to_i
  when "up"
    depth -= instruction[1].to_i
  when "down"
    depth += instruction[1].to_i
  end
end

puts "Forward: " + forward.to_s
puts "Height: " + depth.to_s
puts "Mult: " + (forward * depth).to_s
