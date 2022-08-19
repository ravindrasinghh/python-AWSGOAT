#
When you run the prewritten code, food will be randomly assigned.  You task is to write code that will classify what food is.  

If food is set to either 'apple' or 'grape', your code should print 'fruit'.
If food is set to either 'bacon' or 'steak', your code should print 'meat'
If food is set to either 'dirt' or 'worm' your code should print 'yuck'

#
'# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

if str(food) == "apple" or "grape":
    print("fruit")
elif str(food) == "bacon" or "streak":
    print("meat")
elif str(food) == "dirt" or "worm":     
    print("yuck")
else:
    print("suck")
