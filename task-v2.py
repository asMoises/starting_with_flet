import flet as ft

class TaskApp(ft.UserControl):
  def build(self):
    self.textField = ft.TextField(width=350)
    self.addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.addClick)
    self.tasks = ft.Column() #coluna vazia?
    
    
    taskRow = ft.Column( #Nessa coluna eu passo o 1 controle com dois elementos e o self.task
      controls=[# nesse controle eu quero o alinhamento e um novo controle com 2 componentes 
        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
               controls=[self.textField, self.addBtn]),
        self.tasks]
      )
    
    # retorna a linha com os componentes
    return taskRow
    
  def addClick(self, e):
    task = Task(self.textField.value, self.taskDelete) #função taskDelete
    self.tasks.controls.append(task)
    self.textField.value = ""
    self.update()
  
  def taskDelete(self, task):
    self.tasks.controls.remove(task)
    self.update()

## Classe Task  
class Task(ft.UserControl):
  def __init__(self, taskName, taskDelete):
    super().__init__()
    self.taskName = taskName
    self.taskDelete = taskDelete  
  
  def build(self):
    self.checkBoxTask = ft.Checkbox(label=self.taskName, value=False)
    self.editName = ft.TextField()
    
    # Agrupei os botões editar e excluir em linha
    self.btnsEditLine = ft.Row(controls=[
      ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.editClick),
      ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.deleteClick)
      ])
    
    # Criei uma view da linha com o checkbox e a linha de botoes
    self.displayView = ft.Row( 
      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
      controls=[self.checkBoxTask, self.btnsEditLine]
      )
    
    # Criei o botõ salvar
    self.btnDone = ft.IconButton(ft.icons.DONE_ALL_OUTLINED, on_click=self.saveClick)    
    
    self.editView = ft.Row(
      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
      visible=False, # linha da tarefa que estava sendo mostrada fica oculta
      controls=[self.editName, self.btnDone]
      )
    
    
    return ft.Column(controls=[self.displayView, self.editView])
    
        
  def editClick(self, e):
    self.displayView.visible = False
    self.editView.visible = True
    self.editName.value = self.checkBoxTask.label
    self.update()
  
  def saveClick(self, e):
    self.displayView.visible = True
    self.editView.visible = False
    self.checkBoxTask.label = self.editName.value
    self.update()
  
  def deleteClick(self, e):
    self.taskDelete(self)
  
    
## Main  
def main(pg: ft.page):
  pg.title="Tasking App By Moiss"
  pg.window_width=500
  pg.window_height=700
  pg.bgcolor = "GRAY"
  
  # taskingApp = TaskApp()
  pg.add(TaskApp())
  

ft.app(target=main)