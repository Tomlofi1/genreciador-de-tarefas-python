import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciador de Tarefas')
        self.root.geometry('400x400')

        self.tasks = []

        self.task_label = tk.Label(self.root, text='Suas Tarefas', font=('Helvetica', 14))
        self.task_label.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text='Adicionar Tarefa', command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text='Editar Tarefa', command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button= tk.Button(self.root, text='Excluir Tarefa', command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.notify_button = tk.Button(self.root, text='Notificar', command=self.notify_task)
        self.notify_button.pack(pady=5)

        self.done_button = tk.Button(self.root, text='Concluido', command=self.done_task)
        self.done_button.pack(pady=5)

        self.timer_button = tk.Button(self.root, text='Adicionar Timer', command=self.timer_task)
        self.timer_button.pack(pady=5)

        self.timer_active = False
        self.timer_running = False

    def add_task(self):
        new_task = simpledialog.askstring('Adicionar Tarefa', 'Digite o nome da nova tarefa: ')
        if new_task:
            self.tasks.append(new_task)
            self.update_task_listbox()

    def edit_task(self):
        select_task_index = self.task_listbox.curselection()
        if select_task_index:
            current_task = self.tasks[select_task_index[0]]
            updated_task = simpledialog.askstring('Editar Tarefa', 'Atualizar Tarefa: ', initialvalue=current_task)
            if updated_task:
                self.tasks[select_task_index[0]] = updated_task
                self.update_task_listbox()
            else:
                messagebox.showwarning('Nenhuma Seleção', 'Selecione uma nova tarefa para editar.')

    def delete_task(self):
        select_task_index = self.task_listbox.curselection()
        if select_task_index:
            self.tasks.pop(select_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning('Nenhuma Selecao', 'Selecione uma tarefa para excluir')

    def notify_task(self):
        select_task_index = self.task_listbox.curselection()
        if select_task_index:
            task = self.tasks[select_task_index[0]]
            messagebox.showinfo('Notificacao', f'Lembre-se de completar a sua Tarefa: {task}')
        else:
            messagebox.showwarning('Nenhuma Selecao', 'Selecione uma tarefa para notificar')

    def done_task(self):
        select_task_index = self.task_listbox.curselection()
        if select_task_index:
            task = self.tasks[select_task_index[0]]
            messagebox.showinfo('Notificacao', f'Tarefa concluida: {task}')
            self.tasks.pop(select_task_index[0])
            self.update_task_listbox()

           
            if self.timer_active:
                self.timer_running = False  
                self.timer_active = False
                self.timer_button.config(state='normal')
        else:
            messagebox.showwarning('Nenhuma Selecao', 'Selecione uma tarefa para concluir')

    def timer_task(self):
        if not self.timer_active:
            self.timer_active = True
            self.timer_button.config(state='disabled')
            self.timer_running = True  
            pomodoro_time = 25 * 60
            self.start_timer(pomodoro_time)

    def start_timer(self, remaining_time):
        if self.timer_running and remaining_time > 0:
            minutes = remaining_time // 60
            seconds = remaining_time % 60

            self.root.title(f'Tempo restante: {minutes:02}:{seconds:02}')

            
            self.root.after(1000, self.start_timer, remaining_time - 1)
        elif remaining_time == 0:
            messagebox.showinfo('Pomodoro Concluído', 'O tempo de 25 minutos acabou!')
            self.root.title('Gerenciador de Tarefas')
            self.timer_active = False
            self.timer_button.config(state='normal')
        else:
            
            self.root.title('Gerenciador de Tarefas')
            self.timer_button.config(state='normal')

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
