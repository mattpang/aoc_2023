file = File.open('input2.txt')
lines = file.read.split("\n")
file.close
puts(lines)
puts(lines.length)

max_r = 12
max_g = 13
max_b = 14
total = 0
for line in lines do
  game_id = line.split(":")[0].split(" ")[1].to_i
  keep_id = true
  colour_list = line.split(":")[1].split(";")
  for colours in colour_list do
    for c in colours.split(",") do
      amnt = c.strip.split(" ")[0].to_i

      case c.strip.split(" ")[1]
      when 'red'
        keep_id = false if amnt > max_r

      when 'green'
        keep_id = false if amnt > max_g

      when 'blue'
        keep_id = false if amnt > max_b

      end

    end
  end

  if keep_id
    total += game_id 
  else
    puts("invalid:",game_id)
  end
end

puts total

# part 2

part2 = 0 
for line in lines do
    colour_list = line.split(":")[1].split(";")
    count = {"red"=>0,"green"=>0,"blue"=>0}
    for colours in colour_list do
    # for each colour section, get the max of the colours seen
        for c in colours.split(",") do
            amnt = c.strip.split(" ")[0].to_i
    
            case c.strip.split(" ")[1]
            when 'red'
                if amnt>count["red"]
                    count["red"] = amnt
                end
        
            when 'green'
                if amnt>count["green"]
                    count['green'] = amnt
                end        
            when 'blue'
                if amnt>count["blue"]
                    count["blue"] = amnt
                end        
            end 
        end
    end
    part2 += count['red']*count['green']*count['blue']
end

puts part2