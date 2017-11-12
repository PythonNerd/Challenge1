''' Malthusian.py '''
# The Malthusian scissors were a theory that human population will outgrow resources. 
# The population will grow based on a set growth rate, RT. 
# RT will be set to 1.27. 
# This program will take in user input: P being the number of people and R being the current resources. 
# The program will calculate the next 100 years and return the final population.
# If at any point the population exceeds resources as they grow linearly, the population will be cut by 60% to represent famine and disease and war. 
# Each year subtract P from R to represent food usage.

''' Example I/O '''
#P: 10
#R: 1000
# At the end of year one, the P is 50 while the R is 1950. 
# At the end of year two, the P is 250 while the R is 3650. 
# And so on.

''' Malthusian Function
Input: P, R, RT
Output: Prints population and resources after 100 years
'''
def malthusian(P, R, RT):
    for i in range(100):
        P = int(P * RT)
        R = int(R + R)
        if P >= R:
            P = P // 6
            R = R - P
        else:
            R = R - P
            print(R)
            
        if R < 0:
            P = P // 2
            R = 1000
            
    print("Population after 100 years: " + str(P))
    print("Resources afrer 100 years: " + str(R))
    
malthusian(10, 1000, 5.7)
