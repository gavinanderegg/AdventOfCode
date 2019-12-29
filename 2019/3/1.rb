# require 'pry'; binding.pry

lines = []

File.readlines('sample').each do |line|
    x = 0
    y = 0

    points = {}

    path = line.chop!.split(',')

    path.each do |stop|
        point = stop.match('([A-Z])(\d+)')

        # require 'pry'; binding.pry

        if point != nil
            direction = point[1]
            length = point[2].to_i

            if direction == 'R'
                x += length
            elsif direction == 'L'
                x -= length
            elsif direction == 'U'
                y += length
            elsif direction == 'D'
                y -= length
            end

            if points.key?(x)
                points[x].push(y)
            else
                points[x] = [y]
            end
        end
    end

    lines.push(points)
end

require 'pry'; binding.pry