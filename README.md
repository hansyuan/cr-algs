Immediate step up from previous work

Given base A and demand B, quickly estimate amount of time
it will take to travel.

(1) database exists. Implement this first.

(2) query Google Maps API. Approximately Sunday.


Related to the study:


read.py
- contains functions to read the data


util.py
- contains functions to play around with the data


study.py
- contains high level tasks, like sifting through times



Determine closeness
- Map by longitude, then lattitude. Determine a delta for both. 
Then find something about the travel times to the point, and 
the surrounding deltas.