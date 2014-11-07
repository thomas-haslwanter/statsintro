import matplotlib
import matplotlib.pyplot as plt
import os

def despine(axis='right'):
    '''Despine the plot'''
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.yaxis.set_ticks_position('left')

def set(fs=18):
    '''Set my favorite defaulte fonts'''
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : fs}

    xtick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    ytick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    axes = {'labelsize': fs,
            'titlesize': fs}
    
    legend = {'fontsize': fs}
    
    figure = {'autolayout': True}
    
    matplotlib.rc('font', **font)
    matplotlib.rc('xtick', **xtick)
    matplotlib.rc('ytick', **ytick)
    matplotlib.rc('axes', **axes)
    matplotlib.rc('legend', **legend)
    matplotlib.rc( 'figure', **figure)
    
def printout(outFile, xlabel = '', ylabel='', title='', outDir = 'C:\Users\p20529\Documents\Teaching\Master_FH\Stats\Images'):
    '''Save the current figure to a file, and then display it'''
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.tight_layout
    
    xlim = plt.gca().get_xlim()
    plt.hlines(0, xlim[0], xlim[1], linestyles='--', colors='#999999')
    plt.gca().set_xlim(xlim)
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()

def printout_plain(outFile, outDir = 'C:\Users\p20529\Documents\Teaching\Master_FH\Stats\Images'):
    '''Save a figure with subplots to a file, and then display it'''
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()


if __name__ == '__main__':
    set()
