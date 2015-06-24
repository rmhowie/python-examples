#!/usr/bin/env python3

# errorbar plot for Brett's Oxygen isotopes
# Robert Howie, May 2015

#import modules
import matplotlib.pyplot as plt
import numpy as np

def main():
    #data
    species = np.array(["Pseudanthias dispar", "Ecsenius bicolor", "Gobiodon citrinus"])
    base = np.array([-5, -13, -7])
    base_std_dev = np.array([0.2, 0.3, 0.7])
    dentine = np.array([-6, -5, -9])
    dentine_std_dev = np.array([0.3, 0.8, 0.1])
    enamel = np.array([-3, -17, -15])
    enamel_std_dev = np.array([0.4, 0.6, 0.1])
    
    #create figure and axes
    fig = plt.figure(facecolor="white")
    fig.subplots_adjust(bottom=0.3, left=0.15, right=0.75)
    ax = fig.add_subplot(111)
    
    #plot lines
    ax.errorbar(np.arange(np.size(species)), base, yerr=base_std_dev, label="base", linestyle="None", marker="D")
    ax.errorbar(np.arange(np.size(species)), dentine, yerr=dentine_std_dev, label="dentine", linestyle="None", marker="s")
    ax.errorbar(np.arange(np.size(species)), enamel, yerr=enamel_std_dev, label="enamel", linestyle="None", marker="o")
    
    #add titles and labels
    ax.set_title("Oxygen isotopes of selected marine ornamental fish", y=1.05)
    ax.set_ylabel("Oxygen isotope ratio (units)")
    ax.yaxis.set_label_coords(-0.15, 0.5) #move y axis title a little to the left
    ax.set_xticks(np.arange(np.size(species))) #set the positions of the x ticks
    ax.set_xticklabels(species) #label the x ticks
    fig.autofmt_xdate() #auto format the labels to fit
    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.) #legend on top, needs some tweaking
    #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) #draw the legend to the right of the axes up the top
    ax.legend(bbox_to_anchor=(1.05, .5), loc=6, borderaxespad=0.) #draw the legend to the right of the axes in the centre
    ax.set_xlim([-0.5, np.size(species)-0.5]) #set x limits of axes
    
    plt.show() #show the plot
#end main

if __name__ == "__main__":
    main()
#end if  __name__ == "__main__"
