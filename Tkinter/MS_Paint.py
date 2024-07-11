import tkinter as tk
from tkinter import FALSE, TRUE, colorchooser

# Global Variables
current_tool = "pen"
pen_color = "black"
brush_size = 2

# Function to handle pen tool
def use_pen():
  global current_tool
  current_tool = "pen"

# Function to handle brush tool
def use_brush():
  global current_tool
  current_tool = "brush"

# Function to handle eraser tool
def use_eraser():
  global current_tool
  current_tool = "eraser"

# Function to choose a color
def choose_color():
  global pen_color
  color = colorchooser.askcolor()
  if color:
    pen_color = color[1]

# Function to change brush/pen size
def change_size(val):
  global brush_size
  brush_size = int(val)

# Function to paint on canvas
def paint(event):
  x1, y1 = (event.x - brush_size) , (event.y - brush_size)
  x2, y2 = (event.x + brush_size) , (event.y + brush_size)
  if current_tool == "pen":
    canvas.create_line(x1, y1, x2, y2, fill=pen_color, width=brush_size*2)
  elif current_tool == "brush":
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline = pen_color)
  elif current_tool == "eraser":
    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

# Main tkinter window
root = tk.Tk()
root.title("MS Paint")

# Canvas
canvas = tk.Canvas(root, bg = "white", width = 500, height = 500)
canvas.pack(fill=tk.BOTH, expand=TRUE)

# Pen Button
pen_button = tk.Button(root, text="Pen", command=use_pen)
pen_button.pack(side=tk.LEFT)

# Brush Button
brush_button = tk.Button(root, text="Brush", command=use_brush)
brush_button.pack(side=tk.LEFT)

# Eraser Button
eraser_button = tk.Button(root, text="Eraser", command=use_eraser)
eraser_button.pack(side=tk.LEFT)

# Color Button
color_button = tk.Button(root, text="Color", command=choose_color)
color_button.pack(side=tk.LEFT)

# Size Scale
size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Size", command=change_size)
size_slider.pack(side=tk.LEFT)

# Binding mouse motion event to paint function
canvas.bind("<B1-Motion>", paint)

# Start the Tkinter event loop
root.mainloop()