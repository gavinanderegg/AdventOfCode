ssl = 0

File.readlines('input').each do |line|
  good = false

  # Ok, what am I trying to do here?
  # I need to find out if there's a ABA outside of braces, and then I need to confirm that there's a BAB in braces. I should stop trying to do this all at the same time...

  # ^aaaabaa[ or ]aabaaaa[ or ]aaabaaaa$
  #  AND
  # [aaaababaa]

  first = line.match(/\][a-z]*([a-z])([a-z])\1.*?\[[^\]]*(\2\1\2)/)
  second = line.match(/\[[a-z]*([a-z])([a-z])\1[^\]]*\].*?[\[]*(\2\1\2)/)

  if (first != nil) && (first[1] != first[2])
    ssl += 1
  elsif (second != nil) && (second[1] != second[2])
    ssl += 1
  end
end

puts ssl

# 231

# aaaabaa[aaaababaa]aaaaaaa[ or ]aaabaaaa$
  #  AND
  # ($|\])(?=[a-z]*)([a-z])([a-z])\1[a-z]*?($|\[)