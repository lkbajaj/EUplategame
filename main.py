from plate import (Sweden, Ukraine, Romania, 
                   Estonia, Bulgaria, Bosnia, 
                   Malta, Belgium, Spain,
                   Slovakia, Cyprus) 
import tkinter as tk
from plate_imager import back_matter
from PIL import Image, ImageTk
import random
import os


# remove previous files before running if they exist
current_dir = os.getcwd()
directory = f"{current_dir}/plate-outputs"
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if filename.lower().endswith('.png'):
        os.remove(file_path)

# GUI setup. Uses the tkinter package which is not built into Homebrew Installs for Mac M4
root = tk.Tk()
root.title('Plate Viewer')

plate_numbers = []
plate_images = []
current_index = [-1]
showing_front = [True]

label = tk.Label(root)
label.pack()

# internal logic to creating images of plates
def generate_plate():

    plate_options = {
        'Slovakia': Slovakia,
        'Sweden': Sweden,
        'Ukraine': Ukraine,
        'Estonia': Estonia,
        'Romania': Romania,
        'Bosnia': Bosnia,
        'Malta': Malta,
        'Belgium': Belgium,
        'Spain': Spain,
        'Slovakia': Slovakia,
        'Cyprus': Cyprus,
        'Bulgaria': Bulgaria
    }

    countries = list(plate_options.keys())
    country = random.choice(countries)

    plate = plate_options[country]()
    plate.image_plate()
    dictsw = plate.dictsw
    plate_number = plate.plate_number
    back_matter(plate_number,dictsw)
    plate_numbers.append(plate_number)

    front_img = Image.open(f'plate-outputs/{plate_number}-front.png')
    back_img = Image.open(f'plate-outputs/{plate_number}-back.png')

    front_tk = ImageTk.PhotoImage(front_img)
    back_tk = ImageTk.PhotoImage(back_img)
    plate_images.append((front_tk,back_tk))

    current_index[0] += 1
    showing_front[0] = True
    label.config(image=front_tk)

def show_current_image():
    idx = current_index[0]
    front, back = plate_images[idx]
    label.config(image=front if showing_front[0] else back)

def on_click(event):
    showing_front[0] = not showing_front[0]
    show_current_image()

def next_plate():
    if current_index[0] < len(plate_images) - 1:
        current_index[0] +=1
    else:
        generate_plate()

    showing_front[0] = True
    show_current_image()

def prev_plate():
    if current_index[0] > 0:
        current_index[0] -= 1
        showing_front[0] = True
        show_current_image()

# buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

back_btn = tk.Button(button_frame, text='← Back', command=prev_plate)
back_btn.pack(side='left',padx=10)

next_btn = tk.Button(button_frame, text = 'Next →', command=next_plate)
next_btn.pack(side='right',padx=10)

label.bind('<Button-1>',on_click)
generate_plate()
root.mainloop()



