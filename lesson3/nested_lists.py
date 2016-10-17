mixed_up = [1,2,4,'asda',[1,2,['alpha','beta']]]
beatles = [['John',1940],['Paul',1942],['George',1943],['Ringo',1940]]


print mixed_up[4][2][0]


# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

population_of_China = countries[0][2]
population_of_Romania = countries[2][2]

print population_of_China / population_of_Romania