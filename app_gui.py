# app_gui.py
# Frontend GUI for File Integrity Checker using Tkinter

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from hash_generator import generate_file_hash, compare_hashes, get_file_info
import os


class FileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker (Hash Verifier)")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        # Variables
        self.selected_file = ""
        self.original_hash = ""
        
        # Configure style
        self.setup_styles()
        
        # Create GUI components
        self.create_widgets()
        
    def setup_styles(self):
        """Configure GUI styles and colors"""
        self.root.configure(bg="#f0f0f0")
        
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="File Integrity Checker",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main Content Frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # File Selection Section
        file_frame = tk.LabelFrame(
            main_frame,
            text="Select File",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50",
            padx=10,
            pady=10
        )
        file_frame.pack(fill=tk.X, pady=10)
        
        self.file_label = tk.Label(
            file_frame,
            text="No file selected",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#7f8c8d",
            wraplength=600
        )
        self.file_label.pack(pady=5)
        
        select_btn = tk.Button(
            file_frame,
            text="Browse File",
            command=self.select_file,
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        select_btn.pack(pady=5)
        
        # File Info Section
        info_frame = tk.LabelFrame(
            main_frame,
            text="File Information",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50",
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.X, pady=10)
        
        self.info_label = tk.Label(
            info_frame,
            text="File info will appear here",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#7f8c8d",
            justify=tk.LEFT
        )
        self.info_label.pack(pady=5)
        
        # Hash Display Section
        hash_frame = tk.LabelFrame(
            main_frame,
            text="Hash Values",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50",
            padx=10,
            pady=10
        )
        hash_frame.pack(fill=tk.X, pady=10)
        
        # Original Hash
        tk.Label(
            hash_frame,
            text="Original Hash:",
            font=("Arial", 9, "bold"),
            bg="#f0f0f0"
        ).pack(anchor=tk.W)
        
        self.original_hash_var = tk.StringVar()
        original_hash_entry = tk.Entry(
            hash_frame,
            textvariable=self.original_hash_var,
            font=("Courier", 9),
            state="readonly",
            readonlybackground="#ecf0f1",
            fg="#2c3e50"
        )
        original_hash_entry.pack(fill=tk.X, pady=(0, 10))
        
        # New Hash
        tk.Label(
            hash_frame,
            text="Current Hash:",
            font=("Arial", 9, "bold"),
            bg="#f0f0f0"
        ).pack(anchor=tk.W)
        
        self.new_hash_var = tk.StringVar()
        new_hash_entry = tk.Entry(
            hash_frame,
            textvariable=self.new_hash_var,
            font=("Courier", 9),
            state="readonly",
            readonlybackground="#ecf0f1",
            fg="#2c3e50"
        )
        new_hash_entry.pack(fill=tk.X)
        
        # Action Buttons
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        recheck_btn = tk.Button(
            button_frame,
            text="Recheck File",
            command=self.recheck_file,
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        recheck_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_all,
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Result Display
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        )
        self.result_label.pack(pady=10)
        
    def select_file(self):
        """Handle file selection"""
        file_path = filedialog.askopenfilename(
            title="Select a File to Verify",
            filetypes=[("All Files", "*.*")]
        )
        
        if file_path:
            self.selected_file = file_path
            self.file_label.config(
                text=f"Selected: {os.path.basename(file_path)}",
                fg="#2c3e50"
            )
            
            # Get file info
            file_info = get_file_info(file_path)
            if file_info:
                info_text = f"Name: {file_info['name']}\n"
                info_text += f"Size: {self.format_size(file_info['size'])}\n"
                info_text += f"Path: {file_info['path']}"
                self.info_label.config(text=info_text, fg="#2c3e50")
            
            # Generate initial hash
            try:
                hash_value = generate_file_hash(file_path)
                self.original_hash_var.set(hash_value)
                self.original_hash = hash_value
                self.new_hash_var.set(hash_value)
                self.result_label.config(text="[OK] Original hash generated successfully", fg="#27ae60")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate hash:\n{str(e)}")
                
    def recheck_file(self):
        """Recheck file integrity"""
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
            
        if not self.original_hash:
            messagebox.showwarning("Warning", "No original hash available!")
            return
            
        try:
            new_hash = generate_file_hash(self.selected_file)
            self.new_hash_var.set(new_hash)
            
            if compare_hashes(self.original_hash, new_hash):
                self.result_label.config(
                    text="[SAFE] File is Safe - No modifications detected",
                    fg="#27ae60"
                )
                messagebox.showinfo("Success", "File integrity verified!\nNo changes detected.")
            else:
                self.result_label.config(
                    text="[WARNING] File Modified - Integrity compromised!",
                    fg="#e74c3c"
                )
                messagebox.showwarning(
                    "Warning",
                    "File has been modified!\nThe file integrity is compromised."
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to recheck file:\n{str(e)}")
            
    def clear_all(self):
        """Clear all fields"""
        self.selected_file = ""
        self.original_hash = ""
        self.file_label.config(text="No file selected", fg="#7f8c8d")
        self.info_label.config(text="File info will appear here", fg="#7f8c8d")
        self.original_hash_var.set("")
        self.new_hash_var.set("")
        self.result_label.config(text="")
        
    def format_size(self, size_bytes):
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = FileIntegrityChecker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
