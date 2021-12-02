input = File.read("input.txt")

forward = Int64.new(0)
depth = Int64.new(0)
aim = 0

input.each_line do |data|
  instruction = data.split(" ")

  case instruction[0]
  when "forward"
    forward += instruction[1].to_i
    if aim != 0
      depth += instruction[1].to_i * aim
    end
  when "up"
    aim -= instruction[1].to_i
  when "down"
    aim += instruction[1].to_i
  end
end

puts "Forward: " + forward.to_s
puts "Height: " + depth.to_s
puts "Mult: " + (forward * depth).to_s
