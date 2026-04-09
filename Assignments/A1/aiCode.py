import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

# 1. Planetary Data [cite: 7, 9, 15]
# Distance R in AU, Orbital Period T in Years
planets = {
    'Mercury': {'R': 0.39,  'T': 0.24,  'color': 'gray'},
    'Venus':   {'R': 0.72,  'T': 0.62,  'color': 'orange'},
    'Earth':   {'R': 1.00,  'T': 1.00,  'color': 'blue'},
    'Mars':    {'R': 1.52,  'T': 1.88,  'color': 'red'},
    'Jupiter': {'R': 5.20,  'T': 11.86, 'color': 'brown'},
    'Sun':     {'R': 0.00,  'T': 1.00,  'color': 'gold'} # Sun in Copernicus is (0,0)
}

# 2. Setup Figure and Axes [cite: 8]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
plt.subplots_adjust(bottom=0.25, left=0.15)

# 3. Time variables [cite: 10, 11]
t_start = 0.0
t_orbit = np.linspace(0, 10, 1000)

# 4. Storage for plot objects
cop_plots = {}
pto_plots = {}

# 5. Initialization function to draw everything
def init_plots():
    for name, data in planets.items():
        R = data['R']
        T = data['T']
        omega = (2 * np.pi) / T
        color = data['color']

        # Copernicus Calculations [cite: 3, 11]
        xc_orb = R * np.cos(omega * t_orbit)
        yc_orb = R * np.sin(omega * t_orbit)
        
        # Earth data for Ptolemy 
        xe_orb = 1.0 * np.cos((2 * np.pi / 1.0) * t_orbit)
        ye_orb = 1.0 * np.sin((2 * np.pi / 1.0) * t_orbit)

        # Ptolemy Calculations (Relative to Earth) [cite: 2, 12]
        xp_orb = xc_orb - xe_orb
        yp_orb = yc_orb - ye_orb

        # Draw on Copernicus Graph (ax1)
        # We don't draw an orbit for the Sun at (0,0)
        line_c, = ax1.plot(xc_orb, yc_orb, color=color, alpha=0.3, visible=False)
        dot_c,  = ax1.plot([], [], color=color, marker='o', markersize=8, visible=False, label=name)
        cop_plots[name] = {'line': line_c, 'dot': dot_c, 'R': R, 'omega': omega}

        # Draw on Ptolemy Graph (ax2)
        # We don't draw an orbit for Earth at (0,0)
        line_p, = ax2.plot(xp_orb, yp_orb, color=color, alpha=0.3, visible=False)
        dot_p,  = ax2.plot([], [], color=color, marker='o', markersize=8, visible=False)
        pto_plots[name] = {'line': line_p, 'dot': dot_p}

    # Formatting [cite: 9]
    for ax, title in zip([ax1, ax2], ["Copernicus Model (Heliocentric)", "Ptolemy Model (Geocentric)"]):
        ax.set_title(title)
        ax.set_xlabel("Distance (AU)")
        ax.set_ylabel("Distance (AU)")
        ax.axis('equal')
        ax.grid(True, linestyle=':')
        # Set limit for Jupiter visibility
        ax.set_xlim(-7, 7)
        ax.set_ylim(-7, 7)

init_plots()

# 6. Update function for Slider and Checkboxes 
def update(val=None):
    t = slider_t.val
    
    # Calculate Earth's position for relative shift 
    xe = 1.0 * np.cos(2 * np.pi * t)
    ye = 1.0 * np.sin(2 * np.pi * t)

    for name in planets:
        # Get visibility from checkboxes
        is_visible = check.get_status()[list(planets.keys()).index(name)]
        
        # Copernicus update
        p_data = cop_plots[name]
        x_c = p_data['R'] * np.cos(p_data['omega'] * t)
        y_c = p_data['R'] * np.sin(p_data['omega'] * t)
        
        p_data['dot'].set_data([x_c], [y_c])
        p_data['dot'].set_visible(is_visible)
        # Sun orbit line is irrelevant, others visible if checked
        if name != 'Sun': p_data['line'].set_visible(is_visible)

        # Ptolemy update 
        p_pto = pto_plots[name]
        p_pto['dot'].set_data([x_c - xe], [y_c - ye])
        p_pto['dot'].set_visible(is_visible)
        if name != 'Earth': p_pto['line'].set_visible(is_visible)

    fig.canvas.draw_idle()

# 7. GUI Widgets 
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_t = Slider(ax_slider, 'Time (Years)', 0.0, 10.0, valinit=t_start)
slider_t.on_changed(update)

ax_check = plt.axes([0.02, 0.4, 0.1, 0.2])
check = CheckButtons(ax_check, list(planets.keys()), [False]*len(planets))
# Set Earth and Sun and Mars as default active for base view [cite: 15]
for i, name in enumerate(planets.keys()):
    if name in ['Sun', 'Earth', 'Mars']:
        check.set_active(i)

check.on_clicked(update)

# Initial call to set positions
update()
plt.show()