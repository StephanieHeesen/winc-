# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goal1gescoord = 'Ruud Gullit'
goal2gescoord = 'Marco van Basten'

#minuten dat de goals gemaakt zijn.
goal_0 = 32
goal_1 = 54

scorers = (goal1gescoord + ' ' + str(goal_0) + ", " + goal2gescoord + ' ' + str(goal_1) )

report = f'{goal1gescoord} scored in the {goal_0}nd minute\n{goal2gescoord} scored in the {goal_1}th minute'

player = 'Hans van Breukelen'
first_name = player[:player.find(" ")] 
last_name_len = len(player[player.find(" "):])
name_short = player[0]+ '.'+ player[player.find(" "):] 
chant = f'{first_name}! '*(len(first_name)-1) + f'{first_name}!'
good_chant = chant[-1] != " "








