print('''                                                                                  
                                        .  ....... ..                                               
                                     .....:-=++=-:.....                                             
                                     .:*@@@@@@@@@@@%+...                                            
                                  ..:@@@@@@@@@@@@@@@@@#:...............                             
                                  .+@@@@@@@@@@@@@@@@@@@@-.:=*##%##*+-..                             
                               ...-@@@@@@@@@@@@@@@@@@@@@@#@@%##%@@@@@@@#:.                          
                                 .*@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@#%*=:....                          
                                 .+@%##%%@@%%%@@@%%@@%##%%%@@@@@@@@%=..                             
                              ....+@@@@@@@@@@@@@@@@@@@@@@@#...-=*##%#*.                             
                              ....%@@@+....-@@@@@=....-%@@@:...........                             
                                ..%@@%:.....#@@@%:.....#@@@:..                                      
                                ..+@@@#--+#@@@@@@@#+--*@@@#...                                      
                                  :#@@@@@@@@@%:*@@@@@@@@@@-...                                      
                                ..-@@@@@@@@@@-.:%@@@@@@@@@+...                                      
                                ..=@@@@@@@@@*...=@@@@@@@@@*...                                      
                                  ..@@@@@@@@@@@@@@@@@@@@@:.                                         
                                  ...#@*-#@@@@@@@@@%=#@%:..                                         
                                   ...#@=.==+++++++.=@%-...                                         
                                     ..%@@@@@@@@@@@@@@-.                                            
                                     ...*@@@@@@@@@@@%...                                            
                           ...=%%+...   .-%@@@@@@@@+.......=%%*..                                   
                           ..#@@@@@=.......:+*##+-.......:@@@@@@....                                
                          ..-%@@@@@%:...   ........ .....%@@@@@@+...                                
                        ...:@@@@@@@@@@%+-...........:=%@@@@@@@@@@=..                                
                        ....+@@@@@%@@@@@@@%#-...:*%@@@@@@@%%@@@@#...                                
                           ..........-#@@@@@@@@@@@@@@@#=.........                                   
                           .............=%@@@@@@@@@@+:...........                                   
                           ...==:...-%@@@@@@@@#@@@@@@@@@=...:++:.                                   
                        ....#@@@@@@@@@@@@%*-.....:+%@@@@@@@@@@@@%-..                                
                        ...:@@@@@@@@@%+:.............:=#@@@@@@@@@=..                                
                           ..*@@@@@*....              ...=@@@@@#....                                
                           ..*@@@@%-....               ...#@@@@%....                                
                           ....--....                  .....:-...     ''') 
print(""" Hello my friend welcome to my mystry island.
to get out from here you must solve my small puzzle.
don't worry we will enjoy togather.
""")
# using if statment to make user choose from to doors (red and blue)

door = input(' Now choose one of  those door\n you have red door 🚪 and blue door 🚪\n--->')

# if user choose red door he will face Crocodiles` lake and lose

if door.lower() == 'red' :
	print('oops, you reach Crocodiles` lake 🐊🐊🐊.  ')

# if user choose blue door greet him and let him choose from 3 boxes( yellow , green and white)

elif door.lower() =='blue':
	print('good job, let`s go to the next challenge.')
	box = input('choose one of those box and you have green box  📦 , yellow box 📦 and white box 📦. \n ---> ')
	 
# if user choose white box he will surprised by ants moving on his hand and lose

	if box.upper() == 'WHITE':
		print('sorry , you opened a box of bees 🐝🐝🐝. ')
		
# if user choose the green box he will face bees flyes around him and lose			

	elif box.lower() == 'green':
		print('sorry , you opened a box of spiders 🕷🕷🕸🕸. ')
		
# if user choose yellow box greet him and tell him he find the treasure

	elif box.upper() =='YELLOW':
		print('CONGRATULATIONS!! , you finally found the treasure .💰💰💰\nGAME OVRE!!!')
		
# give the user attention to write correctly

	else:
			print(f'excuse me, I can`t understand {box} please follow the instruction ❤.  ')
# if user enter anything except red door and blue door			
else:
	    print(f'please follow instruction , I can`t understand {door} ❤.')