tls = 0

File.readlines('input').each do |line|
  good = false

  outside = line.match(/(.)(.)\2\1/)
  brace = line.match(/\[[^\]]*?(.)(.)\2\1[^\]]*?\]/)

  if outside && outside[0]
    if outside[0][0] != outside[0][1]
      good = true
    end
  end

  if brace && brace[0]
    inside = brace[0].match(/(.)(.)\2\1/)

    if inside && inside[0]
      if inside[0][0] != inside[0][1]
        good = false
      end
    end
  end

  if good
    tls += 1
  end
end

puts tls