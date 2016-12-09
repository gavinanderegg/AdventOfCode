right = 0
lineNum = 0
first = []
second = []
third = []

File.readlines('input').each do |line|
  m = line.match(/(\d+)\s+(\d+)\s+(\d+)/)

  first << m.captures[0]
  second << m.captures[1]
  third << m.captures[2]

  lineNum += 1

  if lineNum > 0 and lineNum % 3 == 0
    firstSides = first.map {|x| x.to_i }.sort
    if firstSides[0] + firstSides[1] > firstSides[2]
      right += 1
    end

    secondSides = second.map {|x| x.to_i }.sort
    if secondSides[0] + secondSides[1] > secondSides[2]
      right += 1
    end

    thirdSides = third.map {|x| x.to_i }.sort
    if thirdSides[0] + thirdSides[1] > thirdSides[2]
      right += 1
    end

    first = []
    second = []
    third = []
  end
end

puts right