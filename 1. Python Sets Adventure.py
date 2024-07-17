# Task 1: Flight Route Comparison Imagine you work for an 
# airline and need to compare the flight routes of your 
# airline with a competitor. You have two sets of flight destinations, 
# one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.
#Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print(f"Both routes fly to: {common_destinations}")

unique_our_routes = our_routes.difference(competitor_routes)
print(f"Our airline's unique routes are: {unique_our_routes}")

destinations_not_shared = our_routes.symmetric_difference(competitor_routes)
print(f"The routes neither airline share are: {destinations_not_shared}")