#CHALLENGE 2.1
print("Challenge 2.1:")
j_murray_scored = 46
f_vanvleet_scored = 43
j_harden_scored = 37

#CHALLENGE 2.2
print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {j_murray_scored} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {f_vanvleet_scored} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {j_harden_scored} 3 point shots")
print()

#CHALLENGE 2.3
print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
j_murray_attempts = 93
f_vanvleet_attempts = 110
j_harden_attempts = 109
print()

#CHALLENGE 2.4
print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {j_murray_scored} 3 point shots and {j_murray_attempts} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {f_vanvleet_scored} 3 point shots and {f_vanvleet_attempts} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {j_harden_scored} 3 point shots and {j_harden_attempts} 3 point shot attempts")
print()

#CHALLENGE 2.5
print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# ALSO LIKE THIS::: j_murray_percent = 46/93
j_murray_percent = j_murray_scored/j_murray_attempts
f_vanvleet_percent = f_vanvleet_scored/f_vanvleet_attempts
j_harden_percent = j_harden_scored/j_harden_attempts

print(f"In the 2020 NBA playoffs, Jamal Murray's shooting percentage was {j_murray_percent}")
print(f"In the 2020 NBA playoffs, Fred VanVleet's shooting percentage was {f_vanvleet_percent}")
print(f"In the 2020 NBA playoffs, James Harden's shooting percentage was {j_harden_percent}")

print()
#CHALLENGE 3.1
print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print()
print("""The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. 
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.
Those three have made good developments with the Pelicans, especially Brandon Ingram. 
But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. 
Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. 
The Lakers ended the season atop the Western Conference with a record of 49-14. 
They were narrowly behind the Bucks for the best record in the league. 
Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.
Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.""")
print()



#CHALLENGE 3.2
print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print("""The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. 
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.
Those three have made good developments with the Pelicans, especially Brandon Ingram. 
But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. 
Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. 
The Lakers ended the season atop the Western Conference with a record of 49-14. 
They were narrowly behind the Bucks for the best record in the league. 
Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.
Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.""".upper())

#CHALLENGE 3.3
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = True
print(f"It's {lakers_are_best}, I think the Lakers are the greatest of all time")
print("")

#CHALLENGE 3.4
print('Challenge 3.4: Type Conversion')
print(int(lakers_are_best))
print(float(lakers_are_best))
print("")

#CHALLENGE 3.5
print('Challenge 3.5: Type Conversion Part 2')
print("")
print(str(j_murray_percent))
print(str(f_vanvleet_percent))
print(str(j_harden_percent))

print("")
print(int(j_murray_percent))
print(int(f_vanvleet_percent))
print(int(j_harden_percent))

