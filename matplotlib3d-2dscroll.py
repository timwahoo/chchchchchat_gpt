import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# Create a 3D volume (you can replace this with your own data)
shape = (30, 30, 30)
volume = np.random.rand(*shape)

# Create a binary mask with the same shape for segmentation
mask = np.zeros(shape, dtype=bool)

# Create a figure and initial 2D slice
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)

# Initial slice index
initial_slice = shape[0] // 2
current_slice = initial_slice

# Display the initial slice
current_image = ax.imshow(volume[current_slice], cmap='gray')

# Create a slider for selecting the slice
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slice_slider = Slider(ax_slider, 'Slice', 0, shape[0] - 1, valinit=initial_slice, valstep=1)

# Create buttons for segmentation
ax_button_add = plt.axes([0.1, 0.02, 0.1, 0.06])
ax_button_clear = plt.axes([0.23, 0.02, 0.1, 0.06])

button_add = Button(ax_button_add, 'Add')
button_clear = Button(ax_button_clear, 'Clear')

# Create radio buttons for brush size
ax_radio = plt.axes([0.45, 0.02, 0.15, 0.15])
radio = RadioButtons(ax_radio, ('Small', 'Medium', 'Large'), active=0)

# Define brush sizes
brush_sizes = {'Small': 1, 'Medium': 3, 'Large': 5}
current_brush_size = brush_sizes['Small']

# Function to update the displayed slice
def update(val):
    global current_slice
    current_slice = int(slice_slider.val)
    current_image.set_data(volume[current_slice])
    fig.canvas.draw_idle()

# Function to handle adding and clearing masks
def add_mask(event):
    x, y = int(event.xdata), int(event.ydata)
    mask_slice = mask[current_slice]
    brush_half = current_brush_size // 2
    for i in range(x - brush_half, x + brush_half + 1):
        for j in range(y - brush_half, y + brush_half + 1):
            if 0 <= i < shape[1] and 0 <= j < shape[2]:
                mask_slice[i, j] = True
    ax.imshow(mask_slice, cmap='Blues', alpha=0.5)
    fig.canvas.draw_idle()

def clear_mask(event):
    mask_slice = mask[current_slice]
    mask_slice.fill(False)
    ax.imshow(mask_slice, cmap='Blues', alpha=0.5)
    fig.canvas.draw_idle()

def change_brush_size(label):
    global current_brush_size
    current_brush_size = brush_sizes[label]

# Attach the update function to the slider
slice_slider.on_changed(update)

# Attach the mask functions to the buttons
button_add.on_clicked(add_mask)
button_clear.on_clicked(clear_mask)

# Attach the brush size function to the radio buttons
radio.on_clicked(change_brush_size)

plt.show()
