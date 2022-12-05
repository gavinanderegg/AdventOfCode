input = File.read("input.txt")

points = 0

input.each_line do |line|
  plays = line.split

  if plays.size > 0
    # A = Rock (1), B = Paper (2), C = Scissors (3)
    # X = lose, Y = draw, Z = win

    opp = plays[0]
    me = plays[1]

    print opp, me, "\n"

    if opp == "A"
      if me == "X"
        points += 0 + 3
      elsif me == "Y"
        points += 3 + 1
      elsif me == "Z"
        points += 6 + 2
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
        points += 0 + 2
      elsif me == "Y"
        points += 3 + 3
      elsif me == "Z"
        points += 6 + 1
      end
    end
  end
end

puts points
