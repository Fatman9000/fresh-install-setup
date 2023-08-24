import tkinter as tk
from tkinter import filedialog
import subprocess


def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Ansible Playbooks", "*.yml")])
    playbook_entry.delete(0, tk.END)
    playbook_entry.insert(0, file_path)


def run_playbook():
    playbook_path = playbook_entry.get()
    tasks = task_entry.get()
    cmd = f"ansible-playbook -i localhost, -e 'tasks={tasks}' {playbook_path}"

    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result.stdout)
    output_text.insert(tk.END, result.stderr)


# Create the main window
window = tk.Tk()
window.title("Ansible GUI")

# Create and place widgets
tk.Label(window, text="Select Ansible Playbook:").pack()
playbook_entry = tk.Entry(window)
playbook_entry.pack()
tk.Button(window, text="Browse", command=open_file_dialog).pack()

tk.Label(window, text="Select Tasks (comma-separated):").pack()
task_entry = tk.Entry(window)
task_entry.pack()

tk.Button(window, text="Run Playbook", command=run_playbook).pack()

output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Start the GUI event loop
window.mainloop()
