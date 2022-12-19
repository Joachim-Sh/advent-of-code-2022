# Memory Complexity: O(n_items + n_monk)
# Runtime Complexity: O(n*n_monk*n_items)

import numpy as np
from tqdm import tqdm

if __name__ == "__main__":

    monkeys_test = [
        {'items':[79,98],
        'operation': lambda x: x * 19,
        'Test': 23,
        'true': 2,
        'false': 3
        },
        {'items':[54,65,75,74],
        'operation': lambda x: x + 6,
        'Test': 19,
        'true': 2,
        'false': 0
        },
        {'items':[79,60,97],
        'operation': lambda x: x * x,
        'Test': 13,
        'true': 1,
        'false': 3
        },
        {'items':[74],
        'operation': lambda x: x + 3,
        'Test': 17,
        'true': 0,
        'false': 1
        },
    ]

    monkeys = [
        {'items':[66, 59, 64, 51],
        'operation': lambda x: x * 3,
        'Test': 2,
        'true': 1,
        'false': 4
        },
        {'items':[67, 61],
        'operation': lambda x: x * 19,
        'Test': 7,
        'true': 3,
        'false': 5
        },
        {'items':[86, 93, 80, 70, 71, 81, 56],
        'operation': lambda x: x + 2,
        'Test': 11,
        'true': 4,
        'false': 0
        },
        {'items':[94],
        'operation': lambda x: x * x,
        'Test': 19,
        'true': 7,
        'false': 6
        },
        {'items':[71, 92, 64],
        'operation': lambda x: x + 8 ,
        'Test': 3,
        'true': 5,
        'false': 1
        },
        {'items':[58, 81, 92, 75, 56],
        'operation': lambda x: x + 6 ,
        'Test': 5,
        'true': 3,
        'false': 6
        },
        {'items':[82, 98, 77, 94, 86, 81],
        'operation': lambda x: x + 7 ,
        'Test': 17,
        'true': 7,
        'false': 2
        },
        {'items':[54, 95, 70, 93, 88, 93, 63, 50],
        'operation': lambda x: x + 4 ,
        'Test': 13,
        'true': 2,
        'false': 0
        }
    ]

    def simulate_monkeys(monkeys,nmb_rounds,problem=0):
        activity_monkeys = [0] * len(monkeys)
        cnt = 0
        if problem==0:
            lcm =3
        else:
            lcm = 1
            for cnt in range(len(monkeys)):
                lcm *= monkeys[cnt]['Test']
        for i in tqdm(range(nmb_rounds)):
            for cnt in range(len(monkeys)):
                activity_monkeys[cnt] += len(monkeys[cnt]['items'])
                for _ in range(len(monkeys[cnt]['items'])):
                    if problem == 0:
                        monkeys[cnt]['items'][0] = monkeys[cnt]['operation'](monkeys[cnt]['items'][0]) // lcm
                    else:
                        monkeys[cnt]['items'][0] = monkeys[cnt]['operation'](monkeys[cnt]['items'][0]) % lcm
                    if monkeys[cnt]['items'][0] % monkeys[cnt]['Test'] == 0:
                        monkeys[monkeys[cnt]['true']]['items'].append(monkeys[cnt]['items'][0])
                    else:
                        monkeys[monkeys[cnt]['false']]['items'].append(monkeys[cnt]['items'][0])
                    monkeys[cnt]['items'].pop(0)
        return activity_monkeys


    # Problem 1 
    activity_monkeys = simulate_monkeys(monkeys_test,20,problem=0)
    print('Monkey Business: ' + str(np.prod(np.sort(activity_monkeys)[-2:])))
  
    activity_monkeys = simulate_monkeys(monkeys,10000,problem=1)
    sorted_monk = np.sort(activity_monkeys)
    print('Monkey Business: ' + str(sorted_monk[-1] * sorted_monk[-2]))
   


    





        

   
