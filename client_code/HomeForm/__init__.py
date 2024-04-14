import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, Menu
import re

# Custom highlighter for Python syntax
class PythonHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.setup_highlighting()

    def setup_highlighting(self):
        # Keywords for syntax highlighting
        keywords = ["def", "if", "else", "elif", "for", "while", "return", "import", "class", "break", "continue"]
        self.regex = re.compile(r"\b(" + "|".join(keywords) + r")\b")
        self.text_widget.tag_configure("keyword", foreground="#f1c40f", font=('Helvetica', 14, 'bold'))

    def highlight(self):
        text = self.text_widget.get("1.0", 'end-1c')
        for tag in self.text_widget.tag_names():
            self.text_widget.tag_remove(tag, "1.0", 'end')
        for match in self.regex.finditer(text):
            self.text_widget.tag_add("keyword", f"1.0+{match.start()}c", f"1.0+{match.end()}c")

# Main window class
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Interaction Platform")
        self.geometry("1200x800")
        self.create_widgets()

    def create_widgets(self):
        # Create a PanedWindow for resizable panels
        pwindow = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        pwindow.pack(fill=tk.BOTH, expand=True)

        # Left panel: AI Thinking Windows
        left_panel = ttk.Frame(pwindow, width=400)
        pwindow.add(left_panel, weight=1)

        self.thinking_windows = {}
        apis = ["Google Gemini", "OpenAI", "Claude AI", "Groq"]
        colors = {"Google Gemini": "#3498db", "OpenAI": "#2ecc71", "Claude AI": "#e74c3c", "Groq": "#9b59b6"}

        for api in apis:
            ttk.Label(left_panel, text=f"{api} Thinking:", font=('Helvetica', 16, 'bold')).pack(pady=10, padx=10, anchor='w')
            text_area = scrolledtext.ScrolledText(left_panel, wrap=tk.WORD, bg=colors[api], fg='white', font=('Helvetica', 14), height=4)
            text_area.pack(padx=20, pady=10, fill=tk.X)
            self.thinking_windows[api] = text_area

        # Right panel: User Code Area
        right_panel = ttk.Frame(pwindow, width=800)
        pwindow.add(right_panel, weight=3)

        ttk.Label(right_panel, text="Your Code:", font=('Helvetica', 16, 'bold')).pack(pady=10, padx=10, anchor='w')
        self.user_code = scrolledtext.ScrolledText(right_panel, wrap=tk.WORD, bg="#1e1e1e", fg="#ffffff", font=('Helvetica', 14))
        self.user_code.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.highlighter = PythonHighlighter(self.user_code)
        self.user_code.bind("<KeyRelease>", lambda e: self.highlighter.highlight())

        run_button = ttk.Button(right_panel, text="Run Code", command=self.run_code)
        run_button.pack(pady=10)

    def run_code(self):
        # Placeholder function to simulate code execution
        messagebox.showinfo("Run Code", "Executing the user's code...")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
