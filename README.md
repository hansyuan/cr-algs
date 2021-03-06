# Cruz Roja Ambulance Algorithms WI 18

The lab notebook I will use is in `sim.ipynb` not `simulator.ipnyb`.

## Clean Signals and Levers to Pull

- Ambulance chooser should cause a reaction in the GUI.

- The one-second-per-stack should have one pi chart and 
ambulance bar table per event.

## Random Updates

- Sleeping better nowadays.

- Using Jupyter Lab -- it is amazing. 

- Sorry, I didn't name my classes using capital letters.

## Tips

- Tip 1.  Start simple
- Tip 2.  Look at raw data
- Tip 3.  Be concrete
- Tip 4.  Incremental results
- Tip 5.  Find something interesting
- Tip 6.  Push hard on clean signals
- Tip 7.  Actionable
- Tip 8.  Comparative advantage is key
- Tip 9.  Find solid levers to pull
- Tip 10. Document successes and failures
- Tip 11. Inspect outliers
- Tip 12. Eliminate sources of bias

- Use sim.sh

- Use pydoc3 -w class

- Use IPython.embed() and ipdb.set\_trace()


## Goals

**Big Picture**: have a program that takes locations as input, then creating
recommendations using those metrics.

- Improve the metric. Can the numbers give better intuitive understanding?

	- This can be done by looking at how the data is being used to calculate the 
	numbers. 

- Scale up the metric. Can it be made more useful for a more realistic scenario,
like multiple ambulances in action at once? Simultaneous dispatch?

	- Should it consider one and then another? That would be one case. Simultaneous 
	consideration is another case. 

## Past FA 18

In the previous quarter, we came up with a few metrics. These included:

- _Overall coverage_: x/y where x is number of covered demand points 
and y the size of the set of bases

- _Disruption_: (x1-x2)/y where x1 is the original covered demand
points, x2 is the loss in coverage, and y is the total number of bases. 

- _Travel Time_: t where t is the number of seconds it takes for 
an ambulance to leave the base and arrive at the patient.

- _Desirability (new)_: a new relational metric between disruption and 
travel time





# Old CSE 199 Incomplete Notes
## Week 7 Notes are available.
### Summary 
- Using numpy to program high level study 

### Suggestions
- Find the closest base to demand points

- Be able to change the radius from the ambulance

- Map the ambulance to the closest base
