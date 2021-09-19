import numpy as np
import matplotlib.pyplot as plt

def pso(problem,):
    func = problem['func']
    nVar = problem['nVar']
   
    VarMin = problem['VarMin']
    VarMax = problem['VarMax']
    
    MaxIt = params['MaxIt']
    nPop = params['nPop']
    w = params['w']
    wdamp = params['wdamp']
    c1 = params['c1']
    c2 = params['c2']

    ShowIterInfo = params['ShowIterInfo']

    MaxVelocity = 0.2*(VarMax-VarMin)
    MinVelocity = -MaxVelocity

    Position = []
    Velocity = []
    Cost = []
    BestPosition = []
    BestCost = []

    GlobalBestCost = np.inf

    for i in range(0, nPop):

       Position[i] = np.random(VarMin, VarMax, ...) 

       Velocity[i] = np.zeros(...)

       Cost[i] = func(Position[i])

       BestPosition[i] = Position[i]
       BestCost[i] = Cost[i]

       if BestCost[i] < GlobalBestCost:
           GlobalBestPosition = BestPosition[i]
           GlobalBestCost = BestCost[i]


    BestCosts= np.zeros(MaxIt,1)

   

    for it in range(0, MaxIt-1):

        for i in range(0, nPop-1):

            Velocity[i] = Velocity[i] + c1 * np.random((nVar,)) * ( BestPosition[i] - Position[i] )
            + c2 * np.random((nVar,)) * ( GlobalBestPosition - Position[i] )

            Velocity[i] = np.max(Velocity[i], MinVelocity)
            Velocity[i] = np.min(Velocity[i], MaxVelocity)

            Position[i] = Position[i] + Velocity[i] 

            Position[i] = np.max(Position[i], VarMin)
            Position[i] = np.min(Position[i], VarMax)

            Cost[i] = func(Position[i])

            if Cost[i] < BestCost[i]:
                BestPosition[i] = Position[i]
                BestCost[i] = Cost[i]

                if BestCost[i] < GlobalBestCost:
                    GlobalBestPosition = BestPosition[i]
                    GlobalBestCost = BestCost[i]

        BestCost[it] = GlobalBestCost

        if ShowIterInfo:
            print ("Iteration %s :Best Cost = %s" %(it , BestCost[it]))

        w = w * wdamp

        return it 
                

def sphere(x):
    z = sum(x ^ 2)

    return z

if __name__ == "__main__":

    problem = {
        "func": sphere,
        "nVar": 5,
        "VarMin": -10,
        "VarMax": 10
    }

    params = {
        "MaxIt": 1000,
        "nPop": 50,
        "w": 1,
        "wdamp": 0.99,
        "c1": 2,
        "c2": 2,
        "ShowIterInfo": True
    }


    pso(problem)

    

    fig, ax = plt.subplots()

    ax.setxlabel('Iteration')
    ax.setylabel('Best Cost')


    plt.show()

