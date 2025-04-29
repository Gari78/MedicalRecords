from ._anvil_designer import statsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objs as go
from anvil.js import window
import anvil.js


class stats(statsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.income_per_type_plot_original_height = self.income_per_type_plot.height
    self.patients_per_type_plot_original_height = self.patients_per_type_plot.height
    self.income_plot_original_height = self.income_plot.height

    self.onResize()
      
    self.summary = anvil.server.call("get_all_reports")["content"][1]
    self.summary["patients"] = {data["name"]: {"quantity": data["count"], "money": data["money"]} for data in self.summary["insights"]}
    self.fill_pc_content()
    self.update_patients_per_type_plot()
    self.update_income_per_type_plot()
    self.update_income_plot()

    # Any code you write here will run before the form opens.

  def onResize(self):
    self.phone = True if window.innerHeight > window.innerWidth else False
    if self.phone:
      self.phone_recom_lbl.visible = True if self.phone else False
      self.income_per_type_plot.height = window.innerHeight * 0.5
      self.patients_per_type_plot.height = window.innerHeight * 0.5
      self.income_plot.height = window.innerWidth * 0.6
    else:
      self.phone_recom_lbl.visible = False if self.phone else True
      self.income_per_type_plot.height = self.income_per_type_plot_original_height
      self.patients_per_type_plot.height = self.patients_per_type_plot_original_height
      self.income_plot.height = self.income_plot_original_height
  
  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.statisticsLink.role = 'selected'

  def fill_pc_content(self):
    print()
    insights = self.summary["patients"]
    normal = insights.get("Normales", {}) if "Normales" in insights else {"quantity": 0, "money":0}
    telematic = insights.get("Telemáticos", {}) if "Telemáticos" in insights else {"quantity": 0, "money":0}
    urgent = insights.get("Urgentes", {}) if "Urgentes" in insights else {"quantity": 0, "money":0}
    private = insights.get("Privados", {}) if "Privados" in insights else {"quantity": 0, "money":0}
    total = {"quantity": normal["quantity"] + telematic["quantity"] + urgent["quantity"] + private["quantity"],
            "money": normal["money"] + telematic["money"] + urgent["money"] + private["money"]}
    self.total_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Total</div>
            <div style="text-align: center;">{total.get("quantity")}</div>
            <div>{total.get("money")}€</div>
          </div>
    """
    self.normal_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Normales</div>
            <div style="text-align: center;">{normal.get("quantity")}</div>
            <div>{normal.get("money")}€</div>
          </div>
    """
    self.telematic_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Telem</div>
            <div style="text-align: center;">{telematic.get("quantity")}</div>
            <div>{telematic.get("money")}€</div>
          </div>
    """
    self.urgent_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Urgentes</div>
            <div style="text-align: center;">{urgent.get("quantity")}</div>
            <div>{urgent.get("money")}€</div>
          </div>
    """
    self.private_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem;border-right: 1px solid #e5e7eb; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Privados</div>
            <div style="text-align: center;">{private.get("quantity")}</div>
            <div>{private.get("money")}€</div>
          </div>
    """
    self.income_text.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Ingresos</div>
            <div style="text-align: center;">Brutos: {self.summary.get("grossincome")}€</div>
            <div>Netos: {self.summary.get("netincome")}€</div>
          </div>
    """
    
  def update_patients_per_type_plot(self):
    labels = [label for label in self.summary["patients"].keys() if "total" not in label.lower()]
    values = [self.summary["patients"][type].get("quantity",0) for type in labels]
    data = go.Pie(labels=labels, values=values, hole=0.15)  # hole=0.3 si quieres que sea tipo "donut"
    
    layout = go.Layout(
        showlegend=True,
        margin=dict(l=15, r=15, t=15, b=15),
        height=None, 
        autosize=True 
    )
    
    self.patients_per_type_plot.data = [data]
    self.patients_per_type_plot.layout = layout
    
  def update_income_per_type_plot(self):
    labels = [label for label in self.summary["patients"].keys() if "total" not in label.lower()]
    values = [self.summary["patients"][type].get("money",0) for type in labels]
    data = go.Pie(labels=labels, values=values, hole=0.15)  # hole=0.3 si quieres que sea tipo "donut"
    
    layout = go.Layout(
        showlegend=True,
        margin=dict(l=15, r=15, t=15, b=15),
        height=None, 
        autosize=True 
    )

    self.income_per_type_plot.data = [data]
    self.income_per_type_plot.layout = layout

  def update_income_plot(self):
    data = [
        {"date": "2025-04-05", "income": 320},
        {"date": "2025-04-06", "income": 410},
        {"date": "2025-04-07", "income": 280},
        {"date": "2025-04-08", "income": 390},
        {"date": "2025-04-09", "income": 420},
        {"date": "2025-04-10", "income": 450},
        {"date": "2025-04-11", "income": 500},
    ]
    dates = [d.get("date") for d in data]
    daily_income = [d.get("income") for d in data]
    
    # Compute cumulative income
    cumulative_income = []
    total = 0
    for amount in daily_income:
        total += amount
        cumulative_income.append(total)
    
    # Bar trace: daily income
    bar_trace = go.Bar(
        x=dates,
        y=daily_income,
        name="Ingreso diario (€)",
        marker=dict(color="rgba(100,150,250,0.7)"),
        text=[f"{val}€" for val in daily_income],
        textposition="auto"
    )
    
    # Line trace: cumulative income
    line_trace = go.Scatter(
        x=dates,
        y=cumulative_income,
        name="Ingreso Acumulado (€)",
        mode="lines+markers+text",
        line=dict(color="rgba(20,40,100,0.8)", width=3, shape="spline"),
        marker=dict(size=6),
        text=[f"{val}€" for val in cumulative_income],
        textposition="top center"
    )
    
    # Layout
    layout = go.Layout(
        showlegend=False if self.phone else True,
        margin=dict(l=80, r=80, t=80, b=80),
        yaxis=dict(title="Ingresos Brutos (€)"),
        xaxis=dict(title="Fecha"),
        barmode="group",
        showgrid = True
    )
    
    self.income_plot.data = [bar_trace, line_trace]
    self.income_plot.layout = layout

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

