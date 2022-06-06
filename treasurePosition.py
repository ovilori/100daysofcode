#This program will mark a spot with an X.
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
#nested list
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (Enter a two digit number): ")

#grab the first digit as column
column = int(position[0])
#grab the second digit as row
row = int(position[1])

if row > 0 and row <= len(map):
    if column > 0 and column <= len(map):
        map[row - 1][column - 1] = "x"
    else:
        print(f'Please enter two digit numbers between 1 and {len(map)}.')
else:
    print(f'Please enter two digit numbers between 1 and {len(map)}.')

print(f"{row1}\n{row2}\n{row3}")
