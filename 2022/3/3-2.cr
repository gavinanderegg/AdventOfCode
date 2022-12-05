input = File.read_lines("input.txt")

priority_sum = 0
values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

(0...input.size).step(3) do |line|
  common = input[line].split("") & input[line + 1].split("") & input[line + 2].split("")

  priority_sum += values.index(common.first).as(Int32) + 1
end

puts priority_sum