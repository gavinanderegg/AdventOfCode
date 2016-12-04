right = 0

File.readlines('input').each do |line|
  m = line.match(/(\d+)\s+(\d+)\s+(\d+)/)
  sides = m.captures.map {|x| x.to_i }
  sides = sides.sort
  if sides[0] + sides[1] > sides[2]
    right += 1
  else
    puts "Wrong: " + sides[0].to_s + " " + sides[1].to_s + " " + sides[2].to_s
  end
end

puts right