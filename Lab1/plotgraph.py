import numpy as np
import matplotlib.pyplot as plt
#import testResult as tR
import json

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


"""data = {'a': np.arange(5),
        'c': np.random.randint(0, 5, 5),
        'd': np.random.randn(5)}
data['b'] = [1,1,2,2,5]
data['d'] = np.abs(data['d']) * 100
print (data)
plt.scatter('a', 'b', c='c', s=20, data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()"""
