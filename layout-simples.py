import flet as ft


def main(page: ft.Page):
  page.window_width=800
  page.window_height=500
  page.title="AppBar Example"
  
 # page.horizontal_alignment = page.vertical_alignment = "center"

  page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
  page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

  def check_item_clicked(e):
    e.control.checked = not e.control.checked
    page.update()

  itensList = [
    ft.PopupMenuItem(text="Item 1"),
    ft.PopupMenuItem(text="Item 2"),
    ft.PopupMenuItem(text="Item 1"),
    ft.PopupMenuItem(),  # divider
    ft.PopupMenuItem(text="Checked item", checked=False, on_click=check_item_clicked)
    ] 
  actionslist = [
    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
    ft.IconButton(ft.icons.FILTER_3_ROUNDED),
    ft.PopupMenuButton(items=itensList)
    ]
  
  page.appbar = ft.AppBar(
    leading=ft.Icon(ft.icons.PALETTE),
    leading_width=30,
    title=ft.Text("Clique nos três pontinhos para dar um check!"),
    center_title=False,
    bgcolor=ft.colors.SURFACE_VARIANT,
    actions=actionslist
    )

  bottonListBtns = [
    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE), ft.Container(expand=True),
    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE)
    ]
  
  page.bottom_appbar = ft.BottomAppBar(
    bgcolor=ft.colors.SURFACE_VARIANT, 
    shape=ft.NotchShape.CIRCULAR,
    content=ft.Row(controls=bottonListBtns)
    )

  page.add(ft.Text("Body!"))


ft.app(target=main)
