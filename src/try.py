# https://github.com/TomSchimansky/CustomTkinter/issues/1129


# import customtkinter

# class myDragManager():
#     def add_draggable_widget(self, widget):
#         self.widget = widget
#         self.root = widget.winfo_toplevel()
#         self.widget.bind("<B1-Motion>", self.on_drag)
    
#     def on_drag(self, event):
#         self.widget.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(), y=self.root.winfo_pointery()-self.root.winfo_rooty())

# win = customtkinter.CTk()
# win.geometry("650x650")
# win.title("Draggable Widgets")

# style = customtkinter.CTkFont(size=20)

# wrapper =  customtkinter.CTkFrame(win, bg_color="blue")
# wrapper.pack(fill="both", expand=True)

# label1 =  customtkinter.CTkLabel(wrapper, text="I am dragable label", font=style)
# label1.place(x=10, y=10)

# button =  customtkinter.CTkButton(wrapper, text="I am draggable button", font=style)
# button.place(x=50, y=50)

# mydrag1 = myDragManager()
# mydrag1.add_draggable_widget(label1)

# mydrag2 = myDragManager()
# mydrag2.add_draggable_widget(button)

# win.mainloop()

######################################################################################################

# import customtkinter

# class myDragManager():
#     def add_draggable_widget(self, widget):
#         self.widget = widget
#         self.root = widget.winfo_toplevel()
#         self.widget.bind("<Button-1>", self.on_start)
#         self.widget.bind("<B1-Motion>", self.on_drag)

#     def on_start(self, event):
#         self.offset_x = event.x
#         self.offset_y = event.y

#     def on_drag(self, event):
#         new_x = self.root.winfo_pointerx() - self.root.winfo_rootx() - self.offset_x
#         new_y = self.root.winfo_pointery() - self.root.winfo_rooty() - self.offset_y
#         self.widget.place(x=new_x, y=new_y)

# win = customtkinter.CTk()
# win.geometry("800x600")
# win.title("Flowchart Builder")

# style = customtkinter.CTkFont(size=16)

# wrapper = customtkinter.CTkFrame(win)
# wrapper.pack(fill="both", expand=True)

# def create_flow_block(text, x, y):
#     block = customtkinter.CTkFrame(wrapper, width=150, height=80, fg_color="#4A90E2", corner_radius=10)
#     label = customtkinter.CTkLabel(block, text=text, font=style)
#     label.place(relx=0.5, rely=0.5, anchor="center")
#     block.place(x=x, y=y)

#     dragger = myDragManager()
#     dragger.add_draggable_widget(block)
#     return block

# # Create some blocks
# create_flow_block("Start", 100, 100)
# create_flow_block("Process", 300, 100)
# create_flow_block("Decision", 500, 100)
# create_flow_block("End", 300, 300)

# win.mainloop()

##################################################################################################


# import tkinter as tk
# import customtkinter
# class myDragManager():
#     def __init__(self, canvas, connections):
#         self.canvas = canvas
#         self.connections = connections

#     def add_draggable_widget(self, widget, widget_id):
#         widget.bind("<Button-1>", self.on_start)
#         widget.bind("<B1-Motion>", lambda event, w=widget: self.on_drag(event, w))
#         widget._id = widget_id

#     def on_start(self, event):
#         self.offset_x = event.x
#         self.offset_y = event.y

#     def on_drag(self, event, widget):
#         new_x = widget.winfo_x() + event.x - self.offset_x
#         new_y = widget.winfo_y() + event.y - self.offset_y
#         widget.place(x=new_x, y=new_y)
#         self.update_lines()

#     def update_lines(self):
#         for line_id, (start_widget, end_widget) in self.connections.items():
#             x1 = start_widget.winfo_x() + start_widget.winfo_width() // 2
#             y1 = start_widget.winfo_y() + start_widget.winfo_height() // 2
#             x2 = end_widget.winfo_x() + end_widget.winfo_width() // 2
#             y2 = end_widget.winfo_y() + end_widget.winfo_height() // 2
#             self.canvas.coords(line_id, x1, y1, x2, y2)


# win = customtkinter.CTk()
# win.geometry("900x700")
# win.title("Flowchart Builder")

# style = customtkinter.CTkFont(size=16)

# wrapper = customtkinter.CTkFrame(win)
# wrapper.pack(fill="both", expand=True)

# canvas = tk.Canvas(wrapper)

# canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

# blocks = {}
# connections = {}
# dragger = myDragManager(canvas, connections)

# def create_flow_block(name, x, y):
#     block = customtkinter.CTkFrame(wrapper, width=150, height=80, fg_color="#4A90E2", corner_radius=10)
#     label = customtkinter.CTkLabel(block, text=name, font=style)
#     label.place(relx=0.5, rely=0.5, anchor="center")
#     block.place(x=x, y=y)
#     blocks[name] = block
#     dragger.add_draggable_widget(block, name)
#     return block

# def connect_blocks(name1, name2):
#     b1 = blocks[name1]
#     b2 = blocks[name2]
#     x1 = b1.winfo_x() + b1.winfo_width() // 2
#     y1 = b1.winfo_y() + b1.winfo_height() // 2
#     x2 = b2.winfo_x() + b2.winfo_width() // 2
#     y2 = b2.winfo_y() + b2.winfo_height() // 2
#     line = canvas.create_line(x1, y1, x2, y2, width=2, fill="black", arrow=tk.LAST)
#     connections[line] = (b1, b2)

# # Create and connect blocks after mainloop starts to ensure layout is ready
# def setup():
#     create_flow_block("Start", 100, 100)
#     create_flow_block("Process", 300, 100)
#     create_flow_block("Decision", 500, 100)
#     create_flow_block("End", 300, 300)

#     connect_blocks("Start", "Process")
#     connect_blocks("Process", "Decision")
#     connect_blocks("Decision", "End")

# win.after(100, setup)

# win.mainloop()
