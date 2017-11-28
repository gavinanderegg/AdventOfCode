right = 0

File.readlines('input').each do |line|
  m = line.match(/(\d+)\s+(\d+)\s+(\d+)/)
  sides = m.captures.map {|x| x.to_i }.sort

  if sides[0] + sides[1] > sides[2]
    right += 1
  end
end

puts right