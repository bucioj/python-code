################################################################################
# Description: Draws a sine and cosine from 0 to 2pi with every pi/2 on x-axis and
# between -1 and 1 on y-axis
################################################################################
import matplotlib.pyplot as plt
import numpy as np

def main():
    # set x range from 0 to 2pi
    x = np.linspace(0, 2* np.pi, 1000)
    #x = np.arange(0, 2 * np.pi, 0.1)
    #x = np.linspace(0, 2 * np.pi, 1000)
    y_1 = np.sin(x) # declare sine
    y_2 = np.cos(x) # delcare cosine 
    # create graph
    graph = plt.figure()
    ax = graph.add_subplot(1, 1, 1)

    # set positions
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_position('zero')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_position('center')
    #ax.yaxis.set_ticks_position('bottom')
    #ax.yaxis.set_ticks_position('left')

    # make x axis to center
    #ax.spines['bottom'].set_position('center')

    # tick marks with respect to x and y axis
    plt.xticks((0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi), ('$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'))
    plt.yticks((-1, 1))
    # remove the label value under the ticks
    #ax.set_xticklabels([])
    #ax.set_yticklabels([])

    # increase the x value more than 2pi and increase y value to 1.2
    #plt.xlim(0,7)
    #plt.ylim(-1.2, 1.2)

    # remove top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    #plt.yticks(np.arange())

    # plot sin & color with red & blue
    plt.plot(x, y_1, color = 'red')
    plt.plot(x, y_2, color = 'blue')
    plt.savefig("sin_cos_pyplot.pdf")
    #plt.show()

if __name__ == '__main__':
    main()
    plt.show()
