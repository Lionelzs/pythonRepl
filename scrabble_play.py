letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = { key:value for key, value in zip(letters, points)}
letter_to_points[""]= 0

def score_word(word):
  point_total=0
  for a in word:
    point_total+= letter_to_points[a]
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

print(score_word('AMER'))

player_to_words= {"player1": ["BLUE", "TENNIS","EXIT"],
                  "wordNerd": ["EARTH","EYES","MACHINE"],
                  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                  "Prof Reader":["ZAP", "COMA", "PERIOD"]
                 }
print(player_to_words)

player_to_points={}

for k,v in player_to_words.items():
  player_points =0
  for i in v:
    player_points += score_word(i)
  player_to_points[k]= player_points
  
print(player_to_points)

print(score_word('BLUE'))
print(score_word('TENNIS'))
print(score_word('EXIT'))
print(score_word('EARTH'))
print(score_word('EYES'))
print(score_word('MACHINE'))
