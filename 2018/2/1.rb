twos = 0
threes = 0

File.readlines('input.txt').each do |line|
  thisTwo = 0
  thisThree = 0

  line.strip().split('').each do |letter|
    thisTwo += 1 if line.count(letter) == 2
    thisThree += 1 if line.count(letter) == 3
  end

  twos += 1 if thisTwo > 0
  threes += 1 if thisThree > 0
end

puts twos * threes