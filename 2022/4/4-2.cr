input = File.read("test.txt")

subsets = 0

input.each_line do |line|
  ranges = line.split(",")
  range1 = ranges[0].split("-")
  range2 = ranges[1].split("-")
  range1_array = (range1[0].to_i..range1[1].to_i).to_a
  range2_array = (range2[0].to_i..range2[1].to_i).to_a

  if ((range1_array & range2_array).size > 0)
    subsets += 1
  end
end

puts subsets
