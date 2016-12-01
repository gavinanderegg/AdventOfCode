nice = 0

File.readlines('input').each do |line|
  next if line.scan(/(..).*(\1)/).first == nil or line.scan(/(..).*(\1)/).first.length < 2
  next if line.scan(/(.).(\1)/).first == nil or line.scan(/(.).(\1)/).first.length < 1

  nice += 1
end

puts nice
