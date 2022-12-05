input = File.read("input.txt")

points = 0

input.each_line do |line|
  plays = line.split

  if plays.size > 0
    # A/X = Rock (1), B/Y = Paper (2), C/Z = Scissors (3)

    opp = plays[0]
    me = plays[1]

    print opp, me, "\n"

    if opp == "A"
      if me == "X"
        points += 3 + 1
      elsif me == "Y"
        points += 6 + 2
      elsif me == "Z"
        points += 0 + 3
      end
    elsif opp == "B"
      if me == "X"
        points += 0 + 1
      elsif me == "Y"
        points += 3 + 2
      elsif me == "Z"
        points += 6 + 3
      end
    elsif opp == "C"
      if me == "X"
        points += 6 + 1
      elsif me == "Y"
        points += 0 + 2
      elsif me == "Z"
        points += 3 + 3
      end
    end
  end
end

puts points
