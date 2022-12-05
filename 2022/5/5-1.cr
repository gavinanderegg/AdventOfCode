input = File.read("test.txt")

state = Hash(Int32, Array(Char)).new
state_finished = false

input.each_line do |line|
  if state_finished == false
    if (line.size + 1) % 4 != 0
      state_finished = true
      next
    end

    puts ((line.size + 1) / 4).to_s + " containers"
    # load the contents into state
    # (0..line.size).each do |x|
    #
    # end
  end

  if state_finished == true
    # start moving the state around

  end
end

# print the top of the state stacks

