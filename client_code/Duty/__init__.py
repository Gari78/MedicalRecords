from ._anvil_designer import DutyTemplate
from anvil import *
import plotly.graph_objects as go

class Duty(DutyTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        
    def form_show(self, **event_args):
        """This event is triggered when the form is displayed on the screen"""
        self.layout.reset_links()
        self.layout.dutyLink.role = 'selected'
        self.update_progress_bar(60)  # Show the initial progress bar
        
    def update_progress_bar(self, percentage):
        """Update the progress bar using Plotly's basic functionality"""
        # Ensure percentage is between 0 and 100
        percentage = max(60, min(100, percentage))
        
        # Create a simple bar chart with one bar
        # Use a list to represent the full bar (100%)
        x_values = list(range(100))
        # Create color values: blue for progress, grey for remainder
        colors = ['rgb(72, 96, 181)' if i < percentage else 'rgb(224, 224, 224)' for i in x_values]
        
        # Create a basic bar chart
        fig = go.Figure(data=[
            go.Bar(
                x=x_values,
                y=[1] * 100,  # Constant height
                marker_color=colors,
                hoverinfo='none'
            )
        ])
        
        # Customize layout to make it look like a progress bar
        fig.update_layout(
            showlegend=False,
            xaxis=dict(
                showticklabels=False,
                showgrid=False,
                zeroline=False
            ),
            yaxis=dict(
                showticklabels=False,
                showgrid=False,
                zeroline=False
            ),
            margin=dict(l=5, r=5, t=5, b=5),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=50,  # Fixed height
            bargap=0,  # Elimina el espacio entre las barras
            annotations=[
                dict(
                    x=50,
                    y=0.5,
                    xref="x",
                    yref="y",
                    text=f"{int(percentage)}%",
                    showarrow=False,
                    font=dict(
                      size=30,
                      color="white" if percentage > 50 else "black",
                      family="Arial, sans-serif",  # Fuente estándar
                      weight="bold"  # Negrita
                  )
                )
            ]
        )
        
        # Set the figure to your plot component
        self.plot_1.figure = fig