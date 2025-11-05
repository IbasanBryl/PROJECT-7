import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from attendance_system import AttendanceSystem

class AttendanceGUI:
    #GUI class for Attendance System
    
    def __init__(self):
        self.system = AttendanceSystem()
        self.root = tk.Tk()
        self.root.title("Student Attendance Monitoring System")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.primary_color = "#2196F3"
        self.success_color = "#4CAF50"
        self.danger_color = "#f44336"
        self.text_color = "#333333"
        
        self.root.configure(bg=self.bg_color)
        
        self.show_login_screen()
    
    def clear_window(self):
        #Clear all widgets from window
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        #Display login screen
        self.clear_window()
        
        # Login frame
        login_frame = tk.Frame(self.root, bg="white", padx=40, pady=40)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = tk.Label(
            login_frame, 
            text="Attendance System", 
            font=("Arial", 24, "bold"),
            bg="white",
            fg=self.primary_color
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        subtitle = tk.Label(
            login_frame,
            text="Teacher Login",
            font=("Arial", 12),
            bg="white",
            fg=self.text_color
        )
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Username
        tk.Label(
            login_frame, 
            text="Username:", 
            font=("Arial", 11),
            bg="white"
        ).grid(row=2, column=0, sticky="w", pady=5)
        
        self.username_entry = tk.Entry(login_frame, font=("Arial", 11), width=25)
        self.username_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Password
        tk.Label(
            login_frame, 
            text="Password:", 
            font=("Arial", 11),
            bg="white"
        ).grid(row=3, column=0, sticky="w", pady=5)
        
        self.password_entry = tk.Entry(login_frame, font=("Arial", 11), width=25, show="*")
        self.password_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        # Login button
        login_btn = tk.Button(
            login_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            command=self.handle_login
        )
        login_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Info label
        info_label = tk.Label(
            login_frame,
            text="Default: admin / admin123",
            font=("Arial", 9, "italic"),
            bg="white",
            fg="gray"
        )
        info_label.grid(row=5, column=0, columnspan=2)
        
        # Bind Enter key
        self.password_entry.bind("<Return>", lambda e: self.handle_login())
    
    def handle_login(self):
       #Handle login button click
        try:
            username = self.username_entry.get().strip()
            password = self.password_entry.get().strip()
            
            if self.system.authenticate_teacher(username, password):
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.show_main_dashboard()
            else:
                messagebox.showerror("Error", "Invalid username or password")
                self.password_entry.delete(0, tk.END)
        
        except Exception as e:
            messagebox.showerror("Error", f"Login error: {str(e)}")
    
    def show_main_dashboard(self):
        #Display main dashboard
        self.clear_window()
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="Student Attendance Monitoring System",
            font=("Arial", 20, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(side="left", padx=20, pady=20)
        
        logout_btn = tk.Button(
            header_frame,
            text="Logout",
            font=("Arial", 10),
            bg=self.danger_color,
            fg="white",
            cursor="hand2",
            command=self.handle_logout
        )
        logout_btn.pack(side="right", padx=20)
        
        teacher_label = tk.Label(
            header_frame,
            text=f"Logged in as: {self.system.current_teacher}",
            font=("Arial", 10),
            bg=self.primary_color,
            fg="white"
        )
        teacher_label.pack(side="right", padx=20)
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left panel - Menu buttons
        menu_frame = tk.Frame(content_frame, bg="white", width=200)
        menu_frame.pack(side="left", fill="y", padx=(0, 10))
        menu_frame.pack_propagate(False)
        
        tk.Label(
            menu_frame,
            text="Menu",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=20)
        
        menu_buttons = [
            ("Mark Attendance", self.show_mark_attendance),
            ("Add Student", self.show_add_student),
            ("View Students", self.show_view_students),
            ("Daily Report", self.show_daily_report),
            ("Student History", self.show_student_history),
            ("Statistics", self.show_statistics)
        ]
        
        for text, command in menu_buttons:
            btn = tk.Button(
                menu_frame,
                text=text,
                font=("Arial", 11),
                bg=self.primary_color,
                fg="white",
                width=18,
                height=2,
                cursor="hand2",
                command=command
            )
            btn.pack(pady=5, padx=10)
        
        # Right panel - Content area
        self.content_area = tk.Frame(content_frame, bg="white")
        self.content_area.pack(side="right", fill="both", expand=True)
        
        # Show statistics by default
        self.show_statistics()
    
    def handle_logout(self):
        #Handle logout
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.system.current_teacher = None
            self.show_login_screen()
    
    def clear_content_area(self):
        #Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
    
    def show_mark_attendance(self):
        #Show mark attendance interface
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="Mark Attendance",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        form_frame = tk.Frame(self.content_area, bg="white")
        form_frame.pack(pady=20)
        
        # Student ID
        tk.Label(
            form_frame,
            text="Student ID:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=10, padx=5)
        
        student_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
        student_id_entry.grid(row=0, column=1, pady=10, padx=5)
        
        # Status
        tk.Label(
            form_frame,
            text="Status:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=10, padx=5)
        
        status_var = tk.StringVar(value="Present")
        status_frame = tk.Frame(form_frame, bg="white")
        status_frame.grid(row=1, column=1, pady=10, padx=5, sticky="w")
        
        for status in ["Present", "Absent", "Late"]:
            tk.Radiobutton(
                status_frame,
                text=status,
                variable=status_var,
                value=status,
                font=("Arial", 10),
                bg="white"
            ).pack(side="left", padx=5)
        
        def mark_attendance():
            try:
                student_id = student_id_entry.get().strip()
                status = status_var.get()
                
                success, message = self.system.mark_attendance(student_id, status)
                
                if success:
                    messagebox.showinfo("Success", message)
                    student_id_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {str(e)}")
        
        tk.Button(
            form_frame,
            text="Mark Attendance",
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            command=mark_attendance
        ).grid(row=2, column=0, columnspan=2, pady=20)
    
    def show_add_student(self):
        #Show add student interface
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="Add New Student",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        form_frame = tk.Frame(self.content_area, bg="white")
        form_frame.pack(pady=20)
        
        # Student ID
        tk.Label(
            form_frame,
            text="Student ID:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=10, padx=5)
        
        student_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
        student_id_entry.grid(row=0, column=1, pady=10, padx=5)
        
        # Name
        tk.Label(
            form_frame,
            text="Name:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=10, padx=5)
        
        name_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
        name_entry.grid(row=1, column=1, pady=10, padx=5)
        
        # Grade
        tk.Label(
            form_frame,
            text="Grade:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=2, column=0, sticky="w", pady=10, padx=5)
        
        grade_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
        grade_entry.grid(row=2, column=1, pady=10, padx=5)
        
        def add_student():
            try:
                student_id = student_id_entry.get().strip()
                name = name_entry.get().strip()
                grade = grade_entry.get().strip()
                
                success, message = self.system.add_student(student_id, name, grade)
                
                if success:
                    messagebox.showinfo("Success", message)
                    student_id_entry.delete(0, tk.END)
                    name_entry.delete(0, tk.END)
                    grade_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {str(e)}")
        
        tk.Button(
            form_frame,
            text="Add Student",
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            command=add_student
        ).grid(row=3, column=0, columnspan=2, pady=20)
    
    def show_view_students(self):
        #Show all students
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="All Students",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Create treeview
        tree_frame = tk.Frame(self.content_area, bg="white")
        tree_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Name", "Grade"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        tree.heading("ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Grade", text="Grade")
        
        tree.column("ID", width=150)
        tree.column("Name", width=250)
        tree.column("Grade", width=100)
        
        # Iterate over DataFrame rows
        for index, student in self.system.students_df.iterrows():
            tree.insert("", "end", values=(
                student["id"],
                student["name"],
                student["grade"]
            ))
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=tree.yview)
        
        total_label = tk.Label(
            self.content_area,
            text=f"Total Students: {len(self.system.students_df)}",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        total_label.pack(pady=10)
    
    def show_daily_report(self):
        #Show daily attendance report
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="Daily Attendance Report",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        today = datetime.now().strftime("%Y-%m-%d")
        tk.Label(
            self.content_area,
            text=f"Date: {today}",
            font=("Arial", 12),
            bg="white"
        ).pack(pady=5)
        
        # Create treeview
        tree_frame = tk.Frame(self.content_area, bg="white")
        tree_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Name", "Grade", "Status", "Time"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        
        tree.heading("ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Grade", text="Grade")
        tree.heading("Status", text="Status")
        tree.heading("Time", text="Time")
        
        tree.column("ID", width=100)
        tree.column("Name", width=200)
        tree.column("Grade", width=80)
        tree.column("Status", width=100)
        tree.column("Time", width=100)
        
        records = self.system.get_daily_report(today)
        
        for record in records:
            tree.insert("", "end", values=(
                record["student_id"],
                record["name"],
                record["section"],
                record["status"],
                record["time"]
            ))
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=tree.yview)
        
        total_label = tk.Label(
            self.content_area,
            text=f"Total Records Today: {len(records)}",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        total_label.pack(pady=10)
    
    def show_student_history(self):
        #Show student attendance history
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="Student Attendance History",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        search_frame = tk.Frame(self.content_area, bg="white")
        search_frame.pack(pady=10)
        
        tk.Label(
            search_frame,
            text="Student ID:",
            font=("Arial", 11),
            bg="white"
        ).pack(side="left", padx=5)
        
        student_id_entry = tk.Entry(search_frame, font=("Arial", 11), width=20)
        student_id_entry.pack(side="left", padx=5)
        
        # Create treeview
        tree_frame = tk.Frame(self.content_area, bg="white")
        tree_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        tree = ttk.Treeview(
            tree_frame,
            columns=("Date", "Time", "Status", "Marked By"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")
        tree.heading("Status", text="Status")
        tree.heading("Marked By", text="Marked By")
        
        tree.column("Date", width=150)
        tree.column("Time", width=150)
        tree.column("Status", width=100)
        tree.column("Marked By", width=150)
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=tree.yview)
        
        def search_history():
            try:
                student_id = student_id_entry.get().strip()
                
                if not student_id:
                    messagebox.showwarning("Warning", "Please enter a Student ID")
                    return
                
                # Using .index on DataFrame is efficient
                if student_id not in self.system.students_df.index:
                    messagebox.showerror("Error", f"Student ID {student_id} not found")
                    return
                
                # Clear previous results
                for item in tree.get_children():
                    tree.delete(item)
                
                history = self.system.get_student_attendance_history(student_id)
                
                for record in history:
                    tree.insert("", "end", values=(
                        record["date"],
                        record["time"],
                        record["status"],
                        record["marked_by"]
                    ))
                
                if not history:
                    messagebox.showinfo("Info", "No attendance records found for this student")
            
            except Exception as e:
                messagebox.showerror("Error", f"Search error: {str(e)}")
        
        tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 11),
            bg=self.primary_color,
            fg="white",
            cursor="hand2",
            command=search_history
        ).pack(side="left", padx=5)
    
    def show_statistics(self):
        #Show attendance statistics
        self.clear_content_area()
        
        tk.Label(
            self.content_area,
            text="Attendance Statistics",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        stats = self.system.get_statistics()
        
        stats_frame = tk.Frame(self.content_area, bg="white")
        stats_frame.pack(pady=30)
        
        stat_items = [
            ("Total Students", stats.get("total_students", 0), self.primary_color),
            ("Total Records", stats.get("total_records", 0), self.primary_color),
            ("Present Today", stats.get("present_today", 0), self.success_color),
            ("Absent Today", stats.get("absent_today", 0), self.danger_color),
            ("Late Today", stats.get("late_today", 0), "#FF9800"),
            ("Attendance Rate", f"{stats.get('attendance_rate', 0)}%", self.success_color)
        ]
        
        row = 0
        col = 0
        for label, value, color in stat_items:
            card = tk.Frame(stats_frame, bg=color, width=200, height=120)
            card.grid(row=row, column=col, padx=15, pady=15)
            card.pack_propagate(False)
            
            tk.Label(
                card,
                text=str(value),
                font=("Arial", 28, "bold"),
                bg=color,
                fg="white"
            ).pack(pady=(20, 5))
            
            tk.Label(
                card,
                text=label,
                font=("Arial", 11),
                bg=color,
                fg="white"
            ).pack()
            
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Refresh button
        tk.Button(
            self.content_area,
            text="Refresh Statistics",
            font=("Arial", 11),
            bg=self.primary_color,
            fg="white",
            cursor="hand2",
            command=self.show_statistics
        ).pack(pady=20)
    
    def run(self):
        #Start the GUI application
        self.root.mainloop()