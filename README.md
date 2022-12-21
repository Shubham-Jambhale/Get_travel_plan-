# Get_travel_plan

# Question


Erin is a wanderlust, and she has a list of cities that she wants to visit. She would like to visit
some cities before others. For example, she wants to visit London before Medellín, Medellín
before São Paulo, Prague before Berlin, and so on. She has a huge list of such priorities. Help
Erin form a travel plan, so she can visit the cities in order. A travel plan is a list of cities such
that if Erin prioritizes city A over city B, city A has to occur earlier than city B in that list.
Write a function get_travel_plan that takes a list of cities and a list of priorities as input and
returns another list which is a travel plan for Erin.

Note: priorities is a list of tuples (A, B) such that Erin prioritizes city A over city B.

# Example 1

cities = [’London’, ’Berlin’, ’Medellín’, ’São Paulo’, ’Prague’, ’Ladakh’, ’Nice’]

priorities = [(’London’, ’Medellín’), (’Medellín’, ’São Paulo’), (’Prague’, ’Berlin’)]

when invoked get_travel_plan(cities, priorities) will give ouput:

[’Nice’, ’London’, ’Medellín’, ’Prague’, ’São Paulo’, ’Berlin’, ’Ladakh’]

# Example 2:

cities = [’New York’, ’Honolulu’]

priorities = [(’New York’, ’Honolulu’), (’Honolulu’, ’New York’)]

when invoked get_travel_plan(cities, priorities) will give ouput: []

These priorities cannot be turned into a travel plan
