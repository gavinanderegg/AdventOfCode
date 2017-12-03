chk = 0

File.readlines('input').each do |line|
  cells = line.split.map(&:to_i)

  cells.each do |cell_outer|
    cells.each do |cell_inner|
      if cell_outer != cell_inner
        if cell_outer % cell_inner == 0
          chk += cell_outer / cell_inner
        end
      end
    end
  end
end

puts chk
