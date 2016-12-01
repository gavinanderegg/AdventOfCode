lights = []
lightsCount = 0

(0..999).each do |x|
  lightsCol = []

  (0..999).each do |y|
    lightsCol[y] = 0
  end

  lights[x] = lightsCol
end

File.readlines('input').each do |line|
  m = line.match(/(\w+\s?\w[^\s\d,]+) (\d+),(\d+) through (\d+),(\d+)/)

  command = m.captures[0]
  startX = Integer(m.captures[1])
  startY = Integer(m.captures[2])
  endX = Integer(m.captures[3])
  endY = Integer(m.captures[4])

  (startY..endY).each do |row|
    (startX..endX).each do |col|
      if command == 'turn on'
        lights[col][row] = 1
      elsif command == 'turn off'
        lights[col][row] = 0
      else command == 'toggle'
        if lights[col][row] == 1
          lights[col][row] = 0
        else
          lights[col][row] = 1
        end
      end
    end
  end
end

(0..999).each do |x|
  (0..999).each do |y|
    if lights[x][y] == 1
      lightsCount += 1
    end
  end
end

p lightsCount
