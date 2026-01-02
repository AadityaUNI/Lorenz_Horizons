from GraphPlot import Plotter
from Model import LorenzModel
import numpy as np
from math import sqrt, ceil

# elements per window
WINDOW_SIZE = 50

N = LorenzModel.N
T = LorenzModel.T

# number of windows (sliding)
NUM_WINDOWS = N - WINDOW_SIZE + 1
    
# time for a single frame
DT = T/(N - 1)

# threshold for predictability:
P_THRESHOLD = 0.5 

# number of windows that should be under threshold (K) to mark it as sensibly unpredictable anymore
K = ceil(15 / DT) + 1 # 15 ~ time period for 2 oscillations of the model meaning we want this many windows to stay under the horizon for 15 seconds

class PredictabilityHorizon:

    def __init__(self, LM1, LM2):
        self.LM1 = LM1
        self.LM2 = LM2
    
    @staticmethod
    def calculateCorrelation(rad1, rad2):
        # radius1 and 2 are x^2 + y^2 + z^2 during a time interval.
        
        mergedRad = np.zeros((2, WINDOW_SIZE))
        mergedRad[0] = rad1
        mergedRad[1] = rad2
        corrArr = np.corrcoef(mergedRad)
        return corrArr[0][1]
        
    def runCorrelationsPlot(self):
        sol1 = self.LM1.solution
        sol2 = self.LM2.solution
        
        x1 = sol1.y[0]
        y1 = sol1.y[1]
        z1 = sol1.y[2]
        
        x2 = sol2.y[0]
        y2 = sol2.y[1]
        z2 = sol2.y[2]
        
        r1 = np.zeros(N)
        r2 = np.zeros(N)
        for i in range(0, N):
            r1[i] = sqrt(x1[i]*x1[i] + y1[i]*y1[i] + z1[i]*z1[i])
            r2[i] = sqrt(x2[i]*x2[i] + y2[i]*y2[i] + z2[i]*z2[i])

    

        # data to pass to the plotting function
        windowedCorr = np.zeros(NUM_WINDOWS)
        corrTimes = np.zeros(NUM_WINDOWS)

        # getting the time the horizon was passed
        horizonTime = float('inf')
        currLen = 0
        startTime = float('inf')
    
        for i in range(0, NUM_WINDOWS):
            w1 = r1[i : i + WINDOW_SIZE]
            w2 = r2[i : i + WINDOW_SIZE]
            
            centerIdx = i + WINDOW_SIZE // 2
            windowedCorr[i] = self.calculateCorrelation(w1, w2)
            corrTimes[i] = centerIdx*DT

            if (horizonTime != float('inf')):
                continue
            
            if (windowedCorr[i] < P_THRESHOLD):
                if currLen == 0:
                    startTime = i
                currLen += 1
            else:
                if currLen >= K:
                    horizonTime = corrTimes[startTime]
                currLen = 0
                
            
        if (currLen >= K):
            horizonTime = corrTimes[startTime]
        
        Plotter.plotCorrelation(windowedCorr, corrTimes, horizonTime, P_THRESHOLD)
        
        
