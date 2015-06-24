#!/usr/bin/env python3

# errorbar plot for Sarah's Iron Ratios
# Robert Howie, June 2015

#import modules
import matplotlib.pyplot as plt
import numpy as np

def main():
    #data
    sample_lables = np.array(["one rock", "two rock", "red rock", "blue rock", "tasty rock", "ca$h\nmoney\nrock"])
    iron_ratio = np.array([23, 53, 23, 52, 42, 77])
    iron_ratio_errors = np.array([0.1, 3, 0.8, 3, 2, 0.5])
    grade = np.array([4, 6, 7, 8, 4, 3])
    #see http://matplotlib.org/api/markers_api.html#module-matplotlib.markers for marker styles
    markers = np.array([".", "o", "^", ">", "v", "<", "1", "2", "3", "4", "8", "s", "p"])
    
    #create figure and axes
    fig = plt.figure(facecolor="white")
    fig.subplots_adjust(bottom=0.1, left=0.15, right=0.7)
    ax = fig.add_subplot(111)
    
    #plot lines
    for i in range(len(iron_ratio)):
        ax.errorbar(grade[i], iron_ratio[i], yerr=iron_ratio_errors[i], label=sample_lables[i], linestyle="None", marker=markers[i])
    
    #add titles and labels
    ax.set_title("Iron Ratios of Rock Things", y=1.05)
    ax.set_ylabel("Iron ratio (%)")
    ax.set_xlabel("Grade (units)")
    ax.yaxis.set_label_coords(-0.15, 0.5) #move y axis title a little to the left
    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.) #legend on top, needs some tweaking
    #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) #draw the legend to the right of the axes up the top
    ax.legend(bbox_to_anchor=(1.05, .5), loc=6, borderaxespad=0.) #draw the legend to the right of the axes in the centre
    ax.set_xlim([grade.min()-0.5, grade.max()+0.5]) #set x limits of axes
    ax.set_xlim([grade.min()-0.5, grade.max()+0.5]) #set x limits of axes
    
    plt.show() #show the plot
#end main

if __name__ == "__main__":
    main()
#end if  __name__ == "__main__"
