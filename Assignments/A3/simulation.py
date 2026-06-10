import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# variables
m = 1200
rho = 1.3
Cd = 0.3
A = 2.1
eta = 0.25
energy_per_liter = 35e6
min_fuel_lh = 0.5
distance = 3000

# Finding optimal speed
v_kmh = np.arange(1, 151, 1)
v_ms = v_kmh / 3.6
Fd_opt = 0.5 * rho * Cd * A * (v_ms**2)
P_opt = Fd_opt * v_ms

fuel_lh_opt = (P_opt / (eta * energy_per_liter)) * 3600
fuel_lh_opt = np.maximum(fuel_lh_opt, min_fuel_lh) # min 0.5 L/h constraint
fuel_l_per_km = fuel_lh_opt / v_kmh

# find the minimum
min_idx = np.argmin(fuel_l_per_km)
best_v = v_kmh[min_idx]
min_consumption = fuel_l_per_km[min_idx]

print(f"Optimal speed: {best_v} km/h")
print(f"Min fuel per km: {min_consumption:.4f} L/km\n")

# plot optimal speed graph using plotly
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=v_kmh, y=fuel_l_per_km, mode='lines', line=dict(color='green')))
fig1.update_layout(
    title="Fuel Consumption vs Speed",
    xaxis_title="Speed (km/h)",
    yaxis_title="Fuel Consumption (L/km)",
    template="plotly_white"
)
fig1.show()

# Synthetic trips simulation
# (a, v_target) combinations
scenarios = [(1.3, 80), (4, 80), (7, 140)]

for a, v_target_kmh in scenarios:
    v_target = v_target_kmh / 3.6
    dt = 0.1
    
    # kinematics
    t_accel = v_target / a
    x_accel = 0.5 * a * (t_accel**2)
    x_cruise = distance - 2 * x_accel
    t_cruise = x_cruise / v_target
    t_total = 2 * t_accel + t_cruise
    t = np.arange(0, t_total, dt)
    
    # empty lists/arrays to update
    v = np.zeros_like(t)
    acc = np.zeros_like(t)
    x = np.zeros_like(t)
    
    # simulation loop
    for i in range(len(t)):
        if t[i] < t_accel:
            acc[i] = a
            v[i] = a * t[i]
            x[i] = 0.5 * a * (t[i]**2)
        elif t[i] < t_accel + t_cruise:
            acc[i] = 0
            v[i] = v_target
            x[i] = x_accel + v_target * (t[i] - t_accel)
        else: # decelerate
            t_dec = t[i] - (t_accel + t_cruise)
            acc[i] = -a
            v[i] = v_target - a * t_dec
            x[i] = x_accel + x_cruise + (v_target * t_dec - 0.5 * a * (t_dec**2))
            
    # physics calculations
    Fd = 0.5 * rho * Cd * A * (v**2)
    F_engine = m * acc + Fd
    P_mech = F_engine * v
    P_mech[P_mech < 0] = 0 # braking uses minimum fuel (0 mechanical power needed)
    
    fuel_lh = (P_mech / (eta * energy_per_liter)) * 3600
    fuel_lh = np.maximum(fuel_lh, min_fuel_lh) # min 0.5 L/h constraint
    
    # sum up total fuel in Liters
    total_fuel = np.sum((fuel_lh / 3600) * dt)
    
    # eco score calculation
    eco_score = total_fuel / (min_consumption * (distance / 1000))
    
    # display the stats
    print(f"--- Results for a={a}, v={v_target_kmh} ---")
    print(f"Max Speed: {np.max(v)*3.6:.2f} km/h")
    print(f"Max Power: {np.max(P_mech):.2f} W")
    print(f"Max Accel: {np.max(acc):.2f} m/s^2")
    print(f"Trip Time: {t_total:.2f} s")
    print(f"Trip Distance: {distance} m")
    print(f"Total Fuel: {total_fuel:.3f} L")
    print(f"ECO Score: {eco_score:.2f}\n")
    
    # graphs using plotly subplots
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                        subplot_titles=('Position (m)', 'Speed (km/h)', 'Accel (m/s^2)', 'Fuel (L/h)'))
    
    fig.add_trace(go.Scatter(x=t, y=x, mode='lines', line=dict(color='blue'), name='Position'), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=v*3.6, mode='lines', line=dict(color='red'), name='Speed'), row=2, col=1)
    fig.add_trace(go.Scatter(x=t, y=acc, mode='lines', line=dict(color='green'), name='Accel'), row=3, col=1)
    fig.add_trace(go.Scatter(x=t, y=fuel_lh, mode='lines', line=dict(color='orange'), name='Fuel'), row=4, col=1)
    
    fig.update_layout(
        title=f'Synthetic Trip: a={a}, v={v_target_kmh}',
        height=800,
        showlegend=False,
        template="plotly_white"
    )
    fig.update_xaxes(title_text='Time (s)', row=4, col=1)
    
    fig.show()