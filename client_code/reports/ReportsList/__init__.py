from ._anvil_designer import ReportsListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window


class ReportsList(ReportsListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    if self.item:
      if window.innerHeight > window.innerWidth:
        self.phone_panel.visible = True
        self.pc_panel.visible = False
        self.fill_phone_content()
      else:
        self.phone_panel.visible = False
        self.pc_panel.visible = True
        self.fill_pc_content()

    # Any code you write here will run before the form opens.

  def view_button_show(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    pass

  def edit_button_click(self, **event_args):
    from ..createReport import createReport
    popup = createReport(self.item)
    open_form(popup)
    

  def delete_button_click(self, **event_args):
    deleted = anvil.server.call("delete_report", self.item.get("id", 0))
    open_form('Reports')

  def fill_pc_content(self):
    insights = {insight["name"]:{"quantity": insight["count"], "money":insight["money"]} for insight in self.item.get("insights", {})}
    normal = insights.get("Normales", {}) if "Normales" in insights else {"quantity": 0, "money":0}
    telematic = insights.get("Telematicos", {}) if "Telematicos" in insights else {"quantity": 0, "money":0}
    urgent = insights.get("Urgentes", {}) if "Urgentes" in insights else {"quantity": 0, "money":0}
    private = insights.get("Privados", {}) if "Privados" in insights else {"quantity": 0, "money":0}
    total = {"quantity": normal["quantity"] + telematic["quantity"] + urgent["quantity"] + private["quantity"],
            "money": normal["money"] + telematic["money"] + urgent["money"] + private["money"]}
    self.interval_dates.content = f"""
        <div style="font-size: 1.rem; color: #6b7280; border-right: 1px solid #e5e7eb; padding-right: 0.75rem; width: 8rem;">
              <div style="font-weight: 700; color: #374151;">Periodo</div>
              <div>{self.item.get("initdate").split("T")[0]}</div>
              <div>{self.item.get("enddate").split("T")[0]}</div>
            </div>
      """
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
            <div style="text-align: center;">Brutos: {self.item.get("grossincome")}€</div>
            <div>Netos: {self.item.get("netincome")}€</div>
          </div>
    """
    
  def fill_phone_content(self):
    insights = {insight["name"]:{"quantity": insight["count"], "money":insight["money"]} for insight in self.item.get("insights", {})}
    normal = insights.get("Normales", {}) if "Normales" in insights else {"quantity": 0, "money":0}
    telematic = insights.get("Telematicos", {}) if "Telematicos" in insights else {"quantity": 0, "money":0}
    urgent = insights.get("Urgentes", {}) if "Urgentes" in insights else {"quantity": 0, "money":0}
    private = insights.get("Privados", {}) if "Privados" in insights else {"quantity": 0, "money":0}
    total = {"quantity": normal["quantity"] + telematic["quantity"] + urgent["quantity"] + private["quantity"],
            "money": normal["money"] + telematic["money"] + urgent["money"] + private["money"]}
    self.interval_dates_copy.content = f"""
        <div style="font-size: 1.rem; color: #6b7280; border-right: 1px solid #e5e7eb; padding-right: 0.75rem; width: 8rem;">
              <div style="font-weight: 700; color: #374151;">Periodo</div>
              <div>{self.item.get("initdate").split("T")[0]}</div>
              <div>{self.item.get("enddate").split("T")[0]}</div>
            </div>
      """
    self.total_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Total</div>
            <div style="text-align: center;">{total.get("quantity")}</div>
            <div>{total.get("money")}€</div>
          </div>
    """
    self.normal_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Normales</div>
            <div style="text-align: center;">{normal.get("quantity")}</div>
            <div>{normal.get("money")}€</div>
          </div>
    """
    self.telematic_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Telem</div>
            <div style="text-align: center;">{telematic.get("quantity")}</div>
            <div>{telematic.get("money")}€</div>
          </div>
    """
    self.urgent_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Urgentes</div>
            <div style="text-align: center;">{urgent.get("quantity")}</div>
            <div>{urgent.get("money")}€</div>
          </div>
    """
    self.private_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem;border-right: 1px solid #e5e7eb; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Privados</div>
            <div style="text-align: center;">{private.get("quantity")}</div>
            <div>{private.get("money")}€</div>
          </div>
    """
    self.income_text_copy.content = f"""
      <div style="font-size: 1.rem; color: #6b7280; padding-right: 0.75rem; width: 8rem;">
            <div style="font-weight: 700; color: #374151;">Ingresos</div>
            <div style="text-align: center;">Brutos: {self.item.get("grossincome")}€</div>
            <div>Netos: {self.item.get("netincome")}€</div>
          </div>
    """