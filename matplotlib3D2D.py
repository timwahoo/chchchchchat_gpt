import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Create a 3D volume (you can replace this with your own data)
shape = (30, 30, 30)
volume = np.random.rand(*shape)

# Create a figure and initial 2D slice
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Initial slice index
initial_slice = shape[0] // 2
current_slice = initial_slice

# Display the initial slice
current_image = ax.imshow(volume[current_slice], cmap='gray')

# Create a slider for selecting the slice
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slice_slider = Slider(ax_slider, 'Slice', 0, shape[0] - 1, valinit=initial_slice, valstep=1)

# Function to update the displayed slice
def update(val):
    global current_slice
    current_slice = int(slice_slider.val)
    current_image.set_data(volume[current_slice])
    fig.canvas.draw_idle()

# Attach the update function to the slider
slice_slider.on_changed(update)

plt.show()
