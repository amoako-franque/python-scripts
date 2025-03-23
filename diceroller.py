#
# ● ┌ ─ ┐ │ └ ┘
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

import random

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", "│          │", "│    ●     │", "│          │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●       │", "│          │", "│      ●   │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●       │", "│    ●     │", "│      ●   │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●   │", "│          │", "│  ●   ●   │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●   │", "│    ●     │", "│  ●   ●   │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●   │", "│  ●   ●   │", "│  ●   ●   │", "└─────────┘"),
}

dice = []
total = 0


num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")

    print()

for die in dice:
    total += die
    # print(dice_art[die][0])
    # print(dice_art[die][1])
    # print(dice_art[die][2])
    # print(dice_art[die][3])
    # print(dice_art[die][4])

print(f"Total: {total}")
