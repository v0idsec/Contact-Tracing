import tkinter as tk
from tkinter import ttk
import random

class ContactTracingGUI:
    def __init__(self, root, grid_size=10, people_count=10):
        self.root = root
        self.grid_size = grid_size
        self.people_count = people_count
        self.positions = {}  # Stores (x, y) positions of people
        self.contacts = {i: set() for i in range(people_count)}
        
        self.canvas = tk.Canvas(root, width=500, height=500, bg='white')
        self.canvas.pack()
        
        self.table_frame = ttk.Frame(root)
        self.table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.table_frame, columns=("Person", "Contacts"), show='headings')
        self.tree.heading("Person", text="Person")
        self.tree.heading("Contacts", text="Contacts")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.setup_grid()
        self.initialize_people()
        self.update_gui()
    
    def setup_grid(self):
        cell_size = 500 // self.grid_size
        for i in range(self.grid_size + 1):
            self.canvas.create_line(i * cell_size, 0, i * cell_size, 500, fill='gray')
            self.canvas.create_line(0, i * cell_size, 500, i * cell_size, fill='gray')
    
    def initialize_people(self):
        for person_id in range(self.people_count):
            x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.positions[person_id] = (x, y)
    
    def move_people(self):
        for person_id in range(self.people_count):
            dx, dy = random.choice([(0,1), (1,0), (0,-1), (-1,0)])
            x, y = self.positions[person_id]
            new_x, new_y = max(0, min(self.grid_size - 1, x + dx)), max(0, min(self.grid_size - 1, y + dy))
            self.positions[person_id] = (new_x, new_y)
        self.detect_contacts()
    
    def detect_contacts(self):
        new_contacts = {i: set() for i in range(self.people_count)}
        position_map = {}
        
        for person_id, pos in self.positions.items():
            if pos in position_map:
                for other in position_map[pos]:
                    new_contacts[person_id].add(other)
                    new_contacts[other].add(person_id)
            position_map.setdefault(pos, []).append(person_id)
        
        for person_id in range(self.people_count):
            self.contacts[person_id].update(new_contacts[person_id])
    
    def update_gui(self):
        self.canvas.delete("people")
        cell_size = 500 // self.grid_size
        for person_id, (x, y) in self.positions.items():
            self.canvas.create_oval(
                x * cell_size + 5, y * cell_size + 5,
                (x + 1) * cell_size - 5, (y + 1) * cell_size - 5,
                fill='blue', tags="people"
            )
        
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for person_id, contact_list in self.contacts.items():
            self.tree.insert("", "end", values=(person_id, ", ".join(map(str, contact_list))))
        
        self.move_people()
        self.root.after(1000, self.update_gui)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Tracing Simulation")
    app = ContactTracingGUI(root, grid_size=10, people_count=10)
    root.mainloop()
