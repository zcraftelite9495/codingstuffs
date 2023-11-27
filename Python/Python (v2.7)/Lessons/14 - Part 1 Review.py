## My Code

# First we create the variable skill_completed and set it to "Python Syntax"
skill_completed = "Python Syntax"

# Now we put the exercises completed
exercises_completed = 13
# And how many points we get per exercise
# Was forced to put the below comment
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5

# Then we set a point total
point_total = 100

# Now we update it to make it the real point total
point_total += exercises_completed * points_per_exercise

# Now we finally can print the string
print ("I got " + str(point_total) + " Points")