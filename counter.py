import flet as ft 

def main(page: ft.Page):
  # Page's Settings
  page.title = "Flet Counter Example"
  page.vertical_alignment=ft.MainAxisAlignment.CENTER
  page.window_width=400
  page.window_height=300
  page.bgcolor = "GRAY"  

  # Functions off Main Class
  def minus_click(e):
    txt_number.value = str(int(txt_number.value) - 1)
    page.update()

  def plus_click(e):
    txt_number.value = str(int(txt_number.value) + 1)
    page.update()

  ## **********************Criando componentes *************************
  #criando o text filed do nome
  textName = ft.TextField(label="Type your name here:", hint_text="Your name...", width=250)
  addBtn = ft.ElevatedButton("Add",animate_opacity=True)
  
  # Inserindo na página
  identificador = ft.Row(
    controls=[textName, addBtn], 
    alignment=ft.MainAxisAlignment.CENTER
    )
    
  # Criando o textfield contador
  txt_number = ft.TextField(read_only=True,value="0",text_align=ft.TextAlign.RIGHT,width=100)  
  minusBtn = ft.IconButton(ft.icons.REMOVE, on_click=minus_click)
  plusBtn = ft.IconButton(ft.icons.ADD, on_click=plus_click)
  
  # Inserindo a linha contadora na página
  contador = ft.Row(
    controls=[minusBtn,txt_number,plusBtn],
    alignment=ft.MainAxisAlignment.CENTER
    )
  
  # **************** Inserindo na pag
  page.add(identificador)
  page.add(contador)  
  page.update()  
  
ft.app(main)