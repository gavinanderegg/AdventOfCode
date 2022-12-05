input = File.read("input.txt")

priority_sum = 0
values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input.each_line do |line|
  first = line[0, (line.size/2).to_i].split("")
  last = line[(line.size/2).to_i, line.size].split("")

  common = first & last

  priority_sum += values.index(common.first).as(Int32) + 1
end

puts priority_sum