import os
import platform

# Classe responsável por gerenciar as tarefas
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task_description, task_status):
        task_id = len(self.tasks)
        task = {
            "id": task_id,
            "description": task_description,
            "status": task_status
        }
        self.tasks.append(task)
        return task

    def get_all(self):
        return self.tasks

    def update_status(self, task_id, new_status):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                return task
        return None

    def remove(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        return self.tasks

# Instância principal do gerenciador
task_manager = TaskManager()

# Função para limpar o terminal
def clear_terminal():
    sistema = platform.system()
    os.system('cls' if sistema == 'Windows' else 'clear')

# Função para adicionar nova tarefa
def add_new_task():
    clear_terminal()
    print("Adicionando nova tarefa...")
    description = input("Digite a descrição da tarefa: ")
    task_manager.add(description, "Pendente")
    print("Tarefa adicionada com sucesso.")
    input("\nPressione Enter para continuar...")

# Função para exibir todas as tarefas
def view_all_tasks():
    clear_terminal()
    print("Lista de Tarefas:\n")
    tasks = task_manager.get_all()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for task in tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}")
    input("\nPressione Enter para continuar...")

# Função para atualizar o status de uma tarefa
def update_existing_task():
    clear_terminal()
    print("Atualizar Tarefa\n")
    try:
        task_id = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        input("\nPressione Enter para continuar...")
        return

    if task_id < 0 or task_id >= len(task_manager.tasks):
        print("ID de tarefa não encontrado.")
        input("\nPressione Enter para continuar...")
        return

    print("""
Selecione o novo status:
[1] Pendente
[2] Concluída
""")
    status_input = input("Opção: ")
    status_map = {"1": "Pendente", "2": "Concluída"}

    if status_input not in status_map:
        print("Opção inválida.")
    else:
        task_manager.update_status(task_id, status_map[status_input])
        print("Status atualizado com sucesso.")

    input("\nPressione Enter para continuar...")

# Função para marcar tarefa como concluída diretamente
def mark_task_as_done():
    clear_terminal()
    print("Concluir Tarefa\n")
    try:
        task_id = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        input("\nPressione Enter para continuar...")
        return

    updated = task_manager.update_status(task_id, "Concluída")
    if updated:
        print("Tarefa marcada como concluída.")
    else:
        print("Tarefa não encontrada.")

    input("\nPressione Enter para continuar...")

# Função para remover uma tarefa
def finish_task():
    clear_terminal()
    print("Finalizar (remover) Tarefa\n")
    try:
        task_id = int(input("Digite o ID da tarefa a ser removida: "))
    except ValueError:
        print("ID inválido.")
        input("\nPressione Enter para continuar...")
        return

    task_manager.remove(task_id)
    print("Tarefa removida com sucesso.")
    input("\nPressione Enter para continuar...")

# Função para sair do programa
def exit_program():
    print("Até mais!")
    exit()

# Dicionário de opções do menu
options = {
    "1": ("Adicionar nova tarefa", add_new_task),
    "2": ("Ver todas as tarefas", view_all_tasks),
    "3": ("Atualizar tarefa existente", update_existing_task),
    "4": ("Marcar tarefa como concluída", mark_task_as_done),
    "5": ("Finalizar tarefa", finish_task),
    "6": ("Sair", exit_program)
}

# Função principal
def main():
    while True:
        clear_terminal()
        print("""
===== MENU - GERENCIADOR DE TAREFAS =====

[1] Adicionar nova tarefa
[2] Ver todas as tarefas
[3] Atualizar tarefa existente
[4] Marcar tarefa como concluída
[5] Finalizar tarefa
[6] Sair
""")
        user_choice = input("Digite a opção desejada: ")

        option = options.get(user_choice, ("Opção inválida", None))
        if option[1]:
            print(f"\n{option[0]}\n")
            option[1]()
        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")

# Execução do programa
if __name__ == "__main__":
    main()
