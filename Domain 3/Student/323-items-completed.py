items = ['Wand', 'Rock', 'Pogo Stick']
levels = ['Level 1', 'Level 2', 'Level 3']
for item in items:
        for level in levels:
            if level == 2 and item == 'Rock':
                continue
            else:
                print(f"You can get a {item} at {level}.")