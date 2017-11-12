## Question
- What time and day are the data estimates based on? I thought it was clustered by time and type of day. 

## Findings so far
- Demand points are not very close to each other. Estimations for 
points that are in between demand points within the database are
are not likely confident. 

## Progress
- Given a set of points, a central point (x, y), and a delta d, find
all the points within (x and x+d, y and y+d)



## Goal

Given base A and demand B, quickly estimate amount of time
it will take to travel.

- database exists. Implement this first.
- query Google Maps API. Approximately Sunday.


Python files:

read.py contains functions to read the data

util.py contains functions to play around with the data

study.py contains high level tasks, like sifting through times

## Determine closeness

- Map by longitude, then lattitude. Determine a delta for both. 
Then find something about the travel times to the point, and 
the surrounding deltas.
