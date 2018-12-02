lines = File.readlines('input.txt')
lineArrays = []

lines.each do |line|
  letters = line.strip().split('')

  lineArrays.each do |la|
    wrong = 0

    la.each_with_index do |letter, index|
      wrong += 1 if letter != letters[index]
    end

    if wrong == 1
      puts line.strip()
      puts la.join('')

      break
    end

  end

  lineArrays.push(letters)
end
