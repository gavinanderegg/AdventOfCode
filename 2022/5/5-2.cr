input = File.read("input.txt")

state = Hash(Int32, Array(Char)).new
state_finished = false

input.each_line do |line|
  if state_finished == false
    if (line.size + 1) % 4 != 0
      state_finished = true
      next
    end

    (0...((line.size + 1) / 4)).to_a.each_index do |index|
      crate = line[(index * 4) + 1]
      if crate != ' '
        if state.has_key?(index)
          state[index] << crate
        else
          state[index] = [crate]
        end
      end
    end
  end

  if state_finished == true
    if line != ""
      args = /move (\d+) from (\d+) to (\d+)/.match(line)

      if args
        amount = args[1].to_i
        from = args[2].to_i
        to = args[3].to_i

        to_move = state[from - 1].delete_at(0, amount)
        to_move.concat(state[to - 1])
        state[to - 1] = to_move
      end
    end
  end
end

state.keys.sort.each do |key|
  puts state[key]
end

