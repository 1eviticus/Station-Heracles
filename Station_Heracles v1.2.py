name = input("What is your name?\n")
print("Hello, " + name + ". Welcome to Station Heracles.")

print("You are a new employee working for Zeus Corp. "
      "It is your first day, and you need to report to your new boss, Eury.")
answer = input("As you walk towards his office, the hallway splits and you are unsure which way to go.\n" 
               "To the left you hear mechanical noises and to the right you hear voices.\n" 
               "       Do you go left or right?\n")

if answer == "left":
    print("You enter a narrow hallway full of exposed pipes and gears.\n"
          "Your jumpsuit is caught in a gear and ripped off just as Eury rounds the corner.\n"
          "You are fired for nudity in the office.\n"
          "     Game over.")

elif answer == "right":
    answer = input("You walk down the hallway and find two employees who introduce themselves as Janet and Clarence.\n"
                   "Janet is drinking a cup of coffee and Clarence is eating a donut.\n"
                   "       Do you ask Janet or Clarence for directions?\n")
    if answer == "Janet":
        print("Janet gives you clear directions to Eury's office.\n"
              "Phew, you never would have found that on your own.\n"
              "        Congratulations on your new job! You win the game.")
    elif answer == "Clarence":
        answer = input("Clarence says he thinks it is on the second floor and directs you to the stairs.\n"
                       "You walk to the stairs and then realize you do not know your current floor.\n"
                       "        Do you go up or down?\n")
        if answer == "up":
            print("You go up the stairs and open what you assume is a door, but which is in fact an airlock.\n"
                  "You are sucked out into space.\n"
                  "        Game over.")
        elif answer == "down":
            print("You go down the stairs and are greeted by your new boss Eury,\n"
                  "who was just on his way to find if you were lost.\n"
                  "Impressed with your resourcefulness navigating the station, you are given a raise.\n"
                  "        You win the game.")
        else:
            print("You took too long to make a decision and are fired for being late on your first day")
    else:
        print("Janet and Clarence were very unimpressed that you couldn't remember their names.\n"
              "        They recommended your position be terminated. Game over.")

else:
    print("Forging your own path, you wander into a restricted are and are fired.\n"
          "        Game Over.")
