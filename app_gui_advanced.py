# app_gui_advanced.py
# Advanced Frontend GUI for File Integrity Checker using Tkinter
# Features: Multiple algorithms, batch processing, export/import, themes

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import json
from datetime import datetime
from hash_generator_advanced import (
    generate_file_hash, 
    generate_multiple_hashes,
    compare_hashes, 
    get_file_info,
    export_hashes_to_file,
    import_hashes_from_file,
    batch_hash_files
)


class AdvancedFileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced File Integrity Checker")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Variables
        self.selected_file = ""
        self.original_hashes = {}
        self.current_algorithm = tk.StringVar(value="SHA256")
        self.dark_mode = tk.BooleanVar(value=False)
        self.recent_files = []
        self.max_recent = 10
        
        # Color schemes
        self.light_theme = {
            'bg': '#f0f0f0',
            'fg': '#2c3e50',
            'header_bg': '#3498db',
            'header_fg': 'white',
            'frame_bg': '#ffffff',
            'entry_bg': '#ecf0f1',
            'button_bg': '#3498db',
            'button_fg': 'white',
            'success': '#27ae60',
            'error': '#e74c3c',
            'warning': '#f39c12'
        }
        
        self.dark_theme = {
            'bg': '#2c3e50',
            'fg': '#ecf0f1',
            'header_bg': '#34495e',
            'header_fg': '#ecf0f1',
            'frame_bg': '#34495e',
            'entry_bg': '#2c3e50',
            'button_bg': '#3498db',
            'button_fg': 'white',
            'success': '#27ae60',
            'error': '#e74c3c',
            'warning': '#f39c12'
        }
        
        self.current_theme = self.light_theme
        
        # Create GUI components
        self.create_widgets()
        self.load_recent_files()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Menu Bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.select_file)
        file_menu.add_command(label="Open Multiple Files", command=self.select_multiple_files)
        file_menu.add_separator()
        file_menu.add_command(label="Export Hashes", command=self.export_hashes)
        file_menu.add_command(label="Import Hashes", command=self.import_hashes)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Tools Menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Batch Hash Generator", command=self.batch_hash_window)
        tools_menu.add_command(label="Hash Comparison Tool", command=self.hash_comparison_window)
        
        # View Menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_checkbutton(label="Dark Mode", variable=self.dark_mode, command=self.toggle_theme)
        
        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="User Guide", command=self.show_guide)
        
        # Title Frame
        self.title_frame = tk.Frame(self.root, bg=self.current_theme['header_bg'], height=70)
        self.title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            self.title_frame,
            text="🔒 Advanced File Integrity Checker",
            font=("Arial", 18, "bold"),
            bg=self.current_theme['header_bg'],
            fg=self.current_theme['header_fg']
        )
        title_label.pack(pady=15)
        
        # Main Content Frame
        self.main_frame = tk.Frame(self.root, bg=self.current_theme['bg'])
        self.main_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)
        
        # Algorithm Selection
        algo_frame = tk.LabelFrame(
            self.main_frame,
            text="Hash Algorithm",
            font=("Arial", 11, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg'],
            padx=10,
            pady=5
        )
        algo_frame.pack(fill=tk.X, pady=5)
        
        algorithms = ["MD5", "SHA1", "SHA256", "SHA512"]
        for algo in algorithms:
            rb = tk.Radiobutton(
                algo_frame,
                text=algo,
                variable=self.current_algorithm,
                value=algo,
                font=("Arial", 10),
                bg=self.current_theme['frame_bg'],
                fg=self.current_theme['fg'],
                selectcolor=self.current_theme['entry_bg']
            )
            rb.pack(side=tk.LEFT, padx=10)
        
        # Multi-hash button
        multi_btn = tk.Button(
            algo_frame,
            text="Generate All Hashes",
            command=self.generate_all_hashes,
            font=("Arial", 9, "bold"),
            bg=self.current_theme['warning'],
            fg="white",
            padx=15,
            pady=3,
            relief=tk.FLAT,
            cursor="hand2"
        )
        multi_btn.pack(side=tk.RIGHT, padx=5)
        
        # File Selection Section
        file_frame = tk.LabelFrame(
            self.main_frame,
            text="File Selection",
            font=("Arial", 11, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg'],
            padx=10,
            pady=10
        )
        file_frame.pack(fill=tk.X, pady=5)
        
        self.file_label = tk.Label(
            file_frame,
            text="No file selected - Click Browse to select a file",
            font=("Arial", 10),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg'],
            wraplength=800
        )
        self.file_label.pack(pady=5)
        
        btn_frame = tk.Frame(file_frame, bg=self.current_theme['frame_bg'])
        btn_frame.pack(pady=5)
        
        select_btn = tk.Button(
            btn_frame,
            text="📁 Browse File",
            command=self.select_file,
            font=("Arial", 10, "bold"),
            bg=self.current_theme['button_bg'],
            fg=self.current_theme['button_fg'],
            padx=15,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2"
        )
        select_btn.pack(side=tk.LEFT, padx=5)
        
        multi_select_btn = tk.Button(
            btn_frame,
            text="📂 Multiple Files",
            command=self.select_multiple_files,
            font=("Arial", 10, "bold"),
            bg=self.current_theme['button_bg'],
            fg=self.current_theme['button_fg'],
            padx=15,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2"
        )
        multi_select_btn.pack(side=tk.LEFT, padx=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(
            file_frame,
            orient=tk.HORIZONTAL,
            length=400,
            mode='determinate'
        )
        self.progress.pack(pady=5)
        
        # File Info Section
        info_frame = tk.LabelFrame(
            self.main_frame,
            text="File Information",
            font=("Arial", 11, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg'],
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.X, pady=5)
        
        self.info_text = tk.Text(
            info_frame,
            height=4,
            font=("Arial", 9),
            bg=self.current_theme['entry_bg'],
            fg=self.current_theme['fg'],
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.info_text.pack(fill=tk.X, pady=5)
        self.info_text.insert('1.0', "File information will appear here...")
        self.info_text.config(state=tk.DISABLED)
        
        # Hash Display Section
        hash_frame = tk.LabelFrame(
            self.main_frame,
            text="Hash Values",
            font=("Arial", 11, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg'],
            padx=10,
            pady=10
        )
        hash_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Original Hash
        tk.Label(
            hash_frame,
            text="Original Hash:",
            font=("Arial", 9, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg']
        ).pack(anchor=tk.W)
        
        self.original_hash_text = tk.Text(
            hash_frame,
            height=2,
            font=("Courier", 9),
            bg=self.current_theme['entry_bg'],
            fg=self.current_theme['fg'],
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.original_hash_text.pack(fill=tk.X, pady=(0, 10))
        
        # Current Hash
        tk.Label(
            hash_frame,
            text="Current Hash:",
            font=("Arial", 9, "bold"),
            bg=self.current_theme['frame_bg'],
            fg=self.current_theme['fg']
        ).pack(anchor=tk.W)
        
        self.current_hash_text = tk.Text(
            hash_frame,
            height=2,
            font=("Courier", 9),
            bg=self.current_theme['entry_bg'],
            fg=self.current_theme['fg'],
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.current_hash_text.pack(fill=tk.X)
        
        # Action Buttons
        button_frame = tk.Frame(self.main_frame, bg=self.current_theme['bg'])
        button_frame.pack(pady=10)
        
        recheck_btn = tk.Button(
            button_frame,
            text="🔄 Recheck File",
            command=self.recheck_file,
            font=("Arial", 10, "bold"),
            bg=self.current_theme['success'],
            fg="white",
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        recheck_btn.pack(side=tk.LEFT, padx=5)
        
        copy_btn = tk.Button(
            button_frame,
            text="📋 Copy Hash",
            command=self.copy_hash,
            font=("Arial", 10, "bold"),
            bg=self.current_theme['warning'],
            fg="white",
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
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
            self.main_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg=self.current_theme['bg']
        )
        self.result_label.pack(pady=5)
        
        # Status Bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 9),
            bg=self.current_theme['header_bg'],
            fg=self.current_theme['header_fg'],
            anchor=tk.W,
            relief=tk.SUNKEN
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def update_progress(self, value):
        """Update progress bar"""
        self.progress['value'] = value
        self.root.update_idletasks()
        
    def select_file(self):
        """Handle single file selection"""
        file_path = filedialog.askopenfilename(
            title="Select a File to Verify",
            filetypes=[("All Files", "*.*")]
        )
        
        if file_path:
            self.process_file(file_path)
            
    def select_multiple_files(self):
        """Handle multiple file selection"""
        file_paths = filedialog.askopenfilenames(
            title="Select Files to Verify",
            filetypes=[("All Files", "*.*")]
        )
        
        if file_paths:
            self.batch_process_files(list(file_paths))
            
    def process_file(self, file_path):
        """Process a single file"""
        self.selected_file = file_path
        self.file_label.config(
            text=f"📄 {os.path.basename(file_path)}",
            fg=self.current_theme['fg']
        )
        
        # Update status
        self.status_bar.config(text=f"Processing: {os.path.basename(file_path)}")
        
        # Get file info
        file_info = get_file_info(file_path)
        if file_info:
            info_text = f"Name: {file_info['name']}\n"
            info_text += f"Size: {self.format_size(file_info['size'])}\n"
            info_text += f"Modified: {file_info['modified']}\n"
            info_text += f"Path: {file_info['path']}"
            
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete('1.0', tk.END)
            self.info_text.insert('1.0', info_text)
            self.info_text.config(state=tk.DISABLED)
        
        # Generate hash
        try:
            algorithm = self.current_algorithm.get()
            hash_value = generate_file_hash(file_path, algorithm, self.update_progress)
            
            self.original_hashes[algorithm] = hash_value
            
            self.original_hash_text.delete('1.0', tk.END)
            self.original_hash_text.insert('1.0', f"{algorithm}: {hash_value}")
            
            self.current_hash_text.delete('1.0', tk.END)
            self.current_hash_text.insert('1.0', f"{algorithm}: {hash_value}")
            
            self.result_label.config(
                text="✅ Hash generated successfully",
                fg=self.current_theme['success']
            )
            self.status_bar.config(text="Ready")
            
            # Add to recent files
            self.add_to_recent(file_path)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate hash:\n{str(e)}")
            self.status_bar.config(text="Error occurred")
            
    def generate_all_hashes(self):
        """Generate all hash types for current file"""
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
            
        try:
            self.status_bar.config(text="Generating multiple hashes...")
            algorithms = ['md5', 'sha1', 'sha256', 'sha512']
            hashes = generate_multiple_hashes(self.selected_file, algorithms, self.update_progress)
            
            # Display all hashes
            hash_text = ""
            for algo, hash_val in hashes.items():
                hash_text += f"{algo}: {hash_val}\n"
                self.original_hashes[algo] = hash_val
            
            self.original_hash_text.delete('1.0', tk.END)
            self.original_hash_text.insert('1.0', hash_text)
            
            self.current_hash_text.delete('1.0', tk.END)
            self.current_hash_text.insert('1.0', hash_text)
            
            self.result_label.config(
                text="✅ All hashes generated successfully",
                fg=self.current_theme['success']
            )
            self.status_bar.config(text="Ready")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate hashes:\n{str(e)}")
            
    def recheck_file(self):
        """Recheck file integrity"""
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
            
        if not self.original_hashes:
            messagebox.showwarning("Warning", "No original hash available!")
            return
            
        try:
            algorithm = self.current_algorithm.get()
            new_hash = generate_file_hash(self.selected_file, algorithm, self.update_progress)
            
            self.current_hash_text.delete('1.0', tk.END)
            self.current_hash_text.insert('1.0', f"{algorithm}: {new_hash}")
            
            if algorithm in self.original_hashes and compare_hashes(self.original_hashes[algorithm], new_hash):
                self.result_label.config(
                    text="✅ SAFE - File is intact, no modifications detected",
                    fg=self.current_theme['success']
                )
                messagebox.showinfo("Success", "File integrity verified!\nNo changes detected.")
            else:
                self.result_label.config(
                    text="⚠️ WARNING - File has been modified!",
                    fg=self.current_theme['error']
                )
                messagebox.showwarning(
                    "Warning",
                    "File has been modified!\nThe file integrity is compromised."
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to recheck file:\n{str(e)}")
            
    def copy_hash(self):
        """Copy current hash to clipboard"""
        hash_value = self.current_hash_text.get('1.0', tk.END).strip()
        if hash_value:
            self.root.clipboard_clear()
            self.root.clipboard_append(hash_value)
            self.status_bar.config(text="Hash copied to clipboard")
            messagebox.showinfo("Success", "Hash copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No hash to copy!")
            
    def export_hashes(self):
        """Export hashes to file"""
        if not self.original_hashes:
            messagebox.showwarning("Warning", "No hashes to export!")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Export Hashes",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
        )
        
        if file_path:
            try:
                data = {
                    'file': self.selected_file,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'hashes': self.original_hashes
                }
                export_hashes_to_file(data, file_path)
                messagebox.showinfo("Success", "Hashes exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export:\n{str(e)}")
                
    def import_hashes(self):
        """Import hashes from file"""
        file_path = filedialog.askopenfilename(
            title="Import Hashes",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                data = import_hashes_from_file(file_path)
                self.original_hashes = data.get('hashes', {})
                
                hash_text = ""
                for algo, hash_val in self.original_hashes.items():
                    hash_text += f"{algo}: {hash_val}\n"
                
                self.original_hash_text.delete('1.0', tk.END)
                self.original_hash_text.insert('1.0', hash_text)
                
                messagebox.showinfo("Success", "Hashes imported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import:\n{str(e)}")
                
    def batch_process_files(self, file_paths):
        """Process multiple files"""
        result_window = tk.Toplevel(self.root)
        result_window.title("Batch Processing Results")
        result_window.geometry("700x500")
        
        text_widget = tk.Text(result_window, font=("Courier", 9), wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(text_widget)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)
        
        algorithm = self.current_algorithm.get().lower()
        text_widget.insert('1.0', f"Batch Hash Generation ({algorithm.upper()})\n")
        text_widget.insert(tk.END, "="*70 + "\n\n")
        
        for file_path in file_paths:
            try:
                hash_val = generate_file_hash(file_path, algorithm)
                text_widget.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
                text_widget.insert(tk.END, f"Hash: {hash_val}\n\n")
            except Exception as e:
                text_widget.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
                text_widget.insert(tk.END, f"Error: {str(e)}\n\n")
                
        text_widget.config(state=tk.DISABLED)
        
    def batch_hash_window(self):
        """Open batch hash generator window"""
        messagebox.showinfo("Batch Hash", "Use File → Open Multiple Files to batch process files")
        
    def hash_comparison_window(self):
        """Open hash comparison tool"""
        comp_window = tk.Toplevel(self.root)
        comp_window.title("Hash Comparison Tool")
        comp_window.geometry("600x400")
        
        tk.Label(comp_window, text="Hash 1:", font=("Arial", 10, "bold")).pack(pady=5)
        hash1_entry = tk.Text(comp_window, height=3, font=("Courier", 9))
        hash1_entry.pack(fill=tk.X, padx=10)
        
        tk.Label(comp_window, text="Hash 2:", font=("Arial", 10, "bold")).pack(pady=5)
        hash2_entry = tk.Text(comp_window, height=3, font=("Courier", 9))
        hash2_entry.pack(fill=tk.X, padx=10)
        
        result_label = tk.Label(comp_window, text="", font=("Arial", 12, "bold"))
        result_label.pack(pady=10)
        
        def compare():
            hash1 = hash1_entry.get('1.0', tk.END).strip()
            hash2 = hash2_entry.get('1.0', tk.END).strip()
            
            if compare_hashes(hash1, hash2):
                result_label.config(text="✅ Hashes Match!", fg="green")
            else:
                result_label.config(text="⚠️ Hashes Do Not Match!", fg="red")
        
        tk.Button(
            comp_window,
            text="Compare",
            command=compare,
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=8
        ).pack(pady=10)
        
    def toggle_theme(self):
        """Toggle between light and dark theme"""
        if self.dark_mode.get():
            self.current_theme = self.dark_theme
        else:
            self.current_theme = self.light_theme
        
        # Refresh the UI
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()
        
    def clear_all(self):
        """Clear all fields"""
        self.selected_file = ""
        self.original_hashes = {}
        self.file_label.config(text="No file selected - Click Browse to select a file")
        
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert('1.0', "File information will appear here...")
        self.info_text.config(state=tk.DISABLED)
        
        self.original_hash_text.delete('1.0', tk.END)
        self.current_hash_text.delete('1.0', tk.END)
        self.result_label.config(text="")
        self.progress['value'] = 0
        self.status_bar.config(text="Ready")
        
    def format_size(self, size_bytes):
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"
        
    def add_to_recent(self, file_path):
        """Add file to recent files list"""
        if file_path not in self.recent_files:
            self.recent_files.insert(0, file_path)
            if len(self.recent_files) > self.max_recent:
                self.recent_files = self.recent_files[:self.max_recent]
            self.save_recent_files()
            
    def load_recent_files(self):
        """Load recent files from config"""
        try:
            if os.path.exists('recent_files.json'):
                with open('recent_files.json', 'r') as f:
                    self.recent_files = json.load(f)
        except:
            pass
            
    def save_recent_files(self):
        """Save recent files to config"""
        try:
            with open('recent_files.json', 'w') as f:
                json.dump(self.recent_files, f)
        except:
            pass
            
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About",
            "Advanced File Integrity Checker v2.0\n\n"
            "Features:\n"
            "• Multiple hash algorithms (MD5, SHA1, SHA256, SHA512)\n"
            "• Batch file processing\n"
            "• Export/Import functionality\n"
            "• Dark/Light themes\n"
            "• Progress tracking\n\n"
            "Created for Cybersecurity Education"
        )
        
    def show_guide(self):
        """Show user guide"""
        guide_text = """
        USER GUIDE
        
        1. Select a file using Browse or drag & drop
        2. Choose hash algorithm (MD5, SHA1, SHA256, SHA512)
        3. Click 'Generate All Hashes' for multiple algorithms
        4. Modify the file if testing
        5. Click 'Recheck File' to verify integrity
        6. Export hashes for future verification
        7. Use batch processing for multiple files
        
        Features:
        - Real-time progress tracking
        - Dark mode support
        - Hash comparison tool
        - Recent files history
        """
        messagebox.showinfo("User Guide", guide_text)


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = AdvancedFileIntegrityChecker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
