nice = 0

File.readlines('input').each do |line|
  next if line.scan(/(.*?[aeiou])/).length < 3
  next if line.scan(/(.)\1{1,}/).length < 1
  next if line.scan(/ab|cd|pq|xy/).length > 0

  nice += 1
end

puts nice
