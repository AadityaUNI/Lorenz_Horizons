
import plotly.graph_objects as go
import plotly.express as px

from Model import *

import plotly.io as pio

# Use system default browser via xdg-open
pio.renderers.default = "browser"

class Plotter:
    # Utility class for graphing plots.
    
    @classmethod
    def plotSingle(cls, lm1):
        s = lm1.solution
        x = s.y[0]
        y = s.y[1]
        z = s.y[2]

        # inital values for data
        xm = np.min(x) - 1.5
        xM = np.max(x) + 1.5
        
        ym = np.min(y) - 1.5
        yM = np.max(y) + 1.5
        
        zm = np.min(z) - 1.5
        zM = np.max(z) + 1.5


        # Create figure
        fig = go.Figure(
            data=[go.Scatter3d(x=[x[0]], y=[y[0]] ,z=[z[0]],
                            mode="lines",
                            showlegend=True,
                            line=dict(width=2, color="blue"), name=lm1.behavior)])
        
        fig.update_layout(autosize=True,
                scene = {"xaxis": dict(range=[xm, xM], autorange=False, zeroline=False),
                "yaxis": dict(range=[ym, yM], autorange=False, zeroline=False),
                "zaxis": dict(range=[zm, zM],autorange=False,zeroline=False)},
                
                title_text="Lorenz Attractor Model", title_x=0.5,
                updatemenus = [dict(type = "buttons",
                buttons = [
                    
                    dict(
                        args = [None, {"frame": {"duration": 50, "redraw": True},
                                        "fromcurrent": True, "transition": {"duration": 0}}],
                        label = "Play",
                        method = "animate",

                        ), dict(
                        args = [[None], {"frame": {"duration": 0, "redraw": True},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                        label = "Pause",
                        method = "animate")
                        
                    ])])

        fig.update(frames=[go.Frame(
                                data=[go.Scatter3d(
                                        x=x[:k],
                                        y=y[:k], z=z[:k])],
                                traces=[0]) # fig.data[0] is updated by each frame
            for k in range(len(x))])

        fig.show()
    
    @classmethod
    def plotDouble(cls, lm1, lm2):
        
        sol1 = lm1.solution
        sol2 = lm2.solution
        
        x1,x2 = sol1.y[0], sol2.y[0]
        y1, y2 = sol1.y[1], sol2.y[1]
        z1, z2 = sol1.y[2], sol2.y[2]
        
        xm = min(np.min(x1), np.min(x2)) - 1.5
        xM = max(np.max(x1), np.max(x2)) + 1.5
        
        ym = min(np.min(y1), np.min(y2)) - 1.5
        yM = max(np.max(y1), np.max(y2)) + 1.5
        
        zm = min(np.min(z1), np.min(z2)) - 1.5
        zM = max(np.max(z1), np.max(z2)) + 1.5
        
        # Create figure
        fig = go.Figure(
            data=[go.Scatter3d(x=[x1[0]], y=[y1[0]] ,z=[z1[0]],
                            mode="lines",
                            line=dict(width=2, color="blue"), name=lm1.behavior),
                go.Scatter3d(x=[x2[0]], y=[y2[0]] ,z=[z2[0]],
                            mode="lines",
                            line=dict(width=2, color="red"), name=lm2.behavior)])
        
        fig.update_layout(autosize=True,
                scene = {"xaxis": dict(range=[xm, xM], autorange=False, zeroline=False),
                "yaxis": dict(range=[ym, yM], autorange=False, zeroline=False),
                "zaxis": dict(range=[zm, zM],autorange=False,zeroline=False)},
                
                title_text="Double Lorenz Simulator", title_x=0.5,
                updatemenus = [dict(type = "buttons",
                buttons = [
                    
                    dict(
                        args = [None, {"frame": {"duration": 50, "redraw": True},
                                        "fromcurrent": True, "transition": {"duration": 0}}],
                        label = "Play",
                        method = "animate",

                        ), dict(
                        args = [[None], {"frame": {"duration": 0, "redraw": True},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                        label = "Pause",
                        method = "animate")
                        
                    ])])

        fig.update(frames=[go.Frame(
                                data=[go.Scatter3d(
                                        x=x1[:k],
                                        y=y1[:k], z=z1[:k]), go.Scatter3d(x=x2[:k], y=y2[:k], z=z2[:k])],
                                traces=[0, 1]) # fig.data[0, 1] is updated by each frame
            for k in range(min(len(x1), len(x2)))])

        fig.show()
        
    @classmethod
    def plotCorrelation(cls, corrArr, timeArr, horizonTime, threshold):
        fig = px.line(x=timeArr, y=corrArr,labels={"x": "Time", "y": "Correlation"},
            title="Correlation vs Time" )
        
        fig.add_hline(threshold, line_dash="dot", line_color="blue", annotation_text="Under = Unpredictable")
        fig.add_vline(horizonTime, line_dash="dash", line_color="red", annotation_text="Horizon to significant unpredictability")
        fig.show()


