ssl = 0

File.readlines('input').each do |line|
  good = false

  first = line.match(/[^\[]*(.)(.)\1[^\[]*\[.*[^\]]*(\2\1\2)/)
  second = line.match(/\[[^\]]*(.)(.)\1[^\]]*\].*[\[]*(\2\1\2)/)

  if first != nil
    ssl += 1
  end

  if second != nil
    ssl += 1
  end
end

puts ssl