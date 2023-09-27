import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# Create a 3D volume (you can replace this with your own data)
shape = (30, 30, 30)
volume = np.random.rand(*shape)

# Create an empty mask volume
mask_volume = np.zeros(shape, dtype=bool)

# Create a figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Initial slice index
initial_slice = shape[0] // 2
current_slice = initial_slice

# Display the initial slice
current_image = ax.imshow(volume[current_slice], cmap='gray')

# Create a slider for selecting the slice
ax_slider = plt.axes([0.2, 0.02, 0.65, 0.03])
slice_slider = Slider(ax_slider, 'Slice', 0, shape[0] - 1, valinit=initial_slice, valstep=1)

# Create buttons for mask actions
ax_button_clear = plt.axes([0.02, 0.1, 0.1, 0.06])
ax_button_save = plt.axes([0.02, 0.02, 0.1, 0.06])

button_clear = Button(ax_button_clear, 'Clear')
button_save = Button(ax_button_save, 'Save Mask')

# Function to update the displayed slice
def update(val):
    global current_slice
    current_slice = int(slice_slider.val)
    current_image.set_data(volume[current_slice])
    fig.canvas.draw_idle()

# Function to handle mask creation and clearing
def clear_mask(event):
    mask_volume[current_slice] = False
    current_image.set_data(volume[current_slice])
    fig.canvas.draw_idle()

def save_mask(event):
    mask_filename = f'mask_slice_{current_slice}.npy'
    np.save(mask_filename, mask_volume[current_slice])

# Attach the update function to the slider
slice_slider.on_changed(update)

# Attach the mask functions to the buttons
button_clear.on_clicked(clear_mask)
button_save.on_clicked(save_mask)

plt.show()
