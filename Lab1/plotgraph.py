import numpy as np
import matplotlib.pyplot as plt
#import testResult as tR
import json


def plotAGraph():
  with open('testResult.json') as f:
    data = json.load(f)

  #for time in data:

  #print (data)

  # evenly sampled time at 200ms intervals

  """data = {'Brute_Force': data['Brute_Force'],
          'KMP': data['KMP'],
          'Boyer-Moore': data['Boyer-Moore']
          }
  """
  #print (data)
  #plt.scatter('a', 'b', c='c', s='d', data=data)

  plt.scatter('y','Brute_Force', s=20, marker='^',data=data)
  plt.scatter('y','KMP', s=40, marker='*', data=data)
  plt.scatter('y','Boyer-Moore', s=60, data=data)

  plt.xlabel('Searching Pattern Lens')
  plt.ylabel('Run Time /s')

  plt.show()

