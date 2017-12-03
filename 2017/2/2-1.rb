chk = 0

File.readlines('input').each do |line|
  largest = 0
  smallest = 999999999 # Ruby doesn't have a maxint?

  line.split.map(&:to_i).each do |cell|
    largest = cell if cell > largest
    smallest = cell if cell < smallest
  end

  chk += largest - smallest
end

puts chk
