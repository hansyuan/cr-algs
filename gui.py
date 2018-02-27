#!/usr/local/bin/python3
import matplotlib.pyplot as plot 
import numpy as np
import time

def draw_pie(covered):

    labels = ['covered', 'not covered']
    sizes = [90, 10]
    colors = ['lightblue', 'grey']

    

    plot.pie([covered, 100-covered], colors=colors, startangle=0, autopct='')
    plot.show()




num_ambs = range(0,11)

ambulances = [str(x) for x in num_ambs]
y_pos = np.arange(len(ambulances))
performance = [0 for x in num_ambs]
performance[5] = 6

plot.barh(y_pos, performance, align='center', alpha=0.5)
plot.yticks(y_pos, ambulances)
plot.ylabel('Ambulances')
plot.xlabel("Availability")
plot.title('Ambulance statuses')

plot.show()



# pie = plot.pie(sizes, colors=colors, shadow=True, startangle=0, autopct='%.1f%%')
# patches = pie[0]
# plot.legend(patches, labels, loc='best')
# plot.axis('equal')
# plot.tight_layout()
# plot.show()


