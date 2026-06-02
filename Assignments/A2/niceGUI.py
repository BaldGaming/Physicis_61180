from nicegui import ui
import numpy as np
import matplotlib
matplotlib.use('Agg') # This forces the non-interactive backend
import matplotlib.pyplot as plt

def run_simulation():
    # 1. Fetch values from sliders
    m = mass_slider.value
    b = b_slider.value
    c = c_slider.value
    h = h_slider.value
    v0 = v0_slider.value
    alpha_deg = alpha_slider.value
    
    alpha = alpha_deg * (np.pi / 180)
    g = 9.8
    dt = 0.001

    # 2. Starting conditions
    x = 0
    y = h
    vx = v0 * np.cos(alpha)
    vy = v0 * np.sin(alpha)
    t = 0

    xList = [x]
    yList = [y]
    tList = [t]

    # 3. Euler calculation
    while y >= 0:
        v = np.sqrt(vx**2 + vy**2)

        ax = -(1 / m) * (b + c * v) * vx
        ay = -g - (1 / m) * (b + c * v) * vy

        vx = vx + ax * dt
        vy = vy + ay * dt

        x = x + vx * dt
        y = y + vy * dt
        t = t + dt

        xList.append(x)
        yList.append(y)
        tList.append(t)

    # 4. Calculate Stats
    maxHeightTime = tList[yList.index(max(yList))]
    
    returnHeightTime = 0
    for i in range(1, len(yList)):
        if yList[i-1] > h and yList[i] <= h:
            returnHeightTime = tList[i]
            break
    if returnHeightTime == 0:
        returnHeightTime = tList[-1] # Fallback if it never goes above h

    totalTime = tList[-1]
    horizontalRange = xList[-1]

    # 5. Parabola fit & RMS
    coefficients = np.polyfit(xList, yList, 2)
    yPara = np.polyval(coefficients, xList)

    yArr = np.array(yList)
    yParaArr = np.array(yPara)
    
    # Avoid division by zero if max and min are exactly the same
    y_range = (np.max(yArr) - np.min(yArr))
    if y_range == 0:
        rms = 0
    else:
        rms = np.sqrt(np.mean((yArr - yParaArr) ** 2)) / y_range

    # 6. Update UI Plot
    with plot:
        plot.fig.clear() 
        ax = plot.fig.add_subplot(111) 
        
        ax.plot(xList, yList, label="Euler calculation", color="red")
        ax.plot(xList, yPara, label="Parabola", color="blue", linestyle="--")
        ax.set_title("Ball Trajectory with Air Resistance")
        ax.set_xlabel("Horizontal Distance x (m)")
        ax.set_ylabel("Height y (m)")
        ax.legend()
        ax.grid(True)
        
        # This line is absolutely mandatory to push the new graph to the browser
        plot.update()

    # 7. Update UI Text Outputs
    results_text.set_text(
        f"Time to max height: {maxHeightTime:.3f} s\n"
        f"Return to starting height: {returnHeightTime:.3f} s\n"
        f"Total flight time: {totalTime:.3f} s\n"
        f"Horizontal Range: {horizontalRange:.3f} m\n"
        f"RMS: {rms:.5f}"
    )

    # 8. Traffic Light Logic
    # Thresholds are assumed based on visual deviation
    if rms < 0.05:
        color = 'green' # Good fit
        eval_text = "Good Fit (Green)"
    elif rms < 0.15:
        color = 'yellow' # Medium fit
    else:
        color = 'red' # Weak fit
        eval_text = "Weak Fit (Red)"
        
    traffic_light.classes(replace=f'w-8 h-8 rounded-full bg-{color}-500 shadow-md')

def generate_prompt():
    prompt = (
        f"A ball with mass {mass_slider.value} kg is thrown from height {h_slider.value} m "
        f"at a velocity of {v0_slider.value} m/s and an angle of {alpha_slider.value} degrees. "
        f"The air resistance constants are b={b_slider.value} and c={c_slider.value}. "
        f"Based on these parameters, is it important to consider air resistance in this specific case? Explain why."
    )
    prompt_output.set_value(prompt)

# --- UI LAYOUT ---
ui.page_title('Air Resistance Simulation')

with ui.row().classes('w-full items-stretch'):
    
    # Left Column: Controls
    with ui.column().classes('w-1/3 p-4 bg-gray-100 rounded-lg shadow-inner'):
        ui.label('Simulation Parameters').classes('text-xl font-bold mb-4')
        
        ui.label('Initial Height (h) [m]')
        h_slider = ui.slider(min=0, max=10, step=0.1, value=0.5, on_change=run_simulation)
        
        ui.label('Initial Velocity (v0) [m/s]')
        v0_slider = ui.slider(min=1, max=50, step=0.5, value=10, on_change=run_simulation)
        
        ui.label('Launch Angle (alpha) [degrees]')
        alpha_slider = ui.slider(min=0, max=90, step=1, value=30, on_change=run_simulation)
        
        ui.label('Mass (m) [kg]')
        mass_slider = ui.slider(min=0.01, max=2.0, step=0.01, value=0.1, on_change=run_simulation)
        
        ui.label('Linear Resistance (b)')
        b_slider = ui.slider(min=0, max=1.0, step=0.01, value=0.2, on_change=run_simulation)
        
        ui.label('Quadratic Resistance (c)')
        c_slider = ui.slider(min=0, max=1.0, step=0.01, value=0.3, on_change=run_simulation)

    # Right Column: Display
    with ui.column().classes('w-2/3 p-4'):
        # Plot
        plot = ui.pyplot(figsize=(8, 5))
        
        # Results & Traffic Light Row
        with ui.row().classes('w-full items-center justify-between mt-4 p-4 bg-white rounded shadow'):
            with ui.column():
                ui.label('Simulation Results:').classes('font-bold text-lg')
                results_text = ui.label().classes('whitespace-pre-line text-gray-700 font-mono')
            
            with ui.column().classes('items-center mr-8'):
                ui.label('Fit Quality').classes('font-bold mb-2')
                traffic_light = ui.element('div').classes('w-8 h-8 rounded-full bg-gray-300 shadow-md')

        # Bonus: Explain Button
        ui.separator().classes('mt-4')
        ui.button('Explain (Generate AI Prompt)', on_click=generate_prompt).classes('mt-4')
        prompt_output = ui.textarea('Prompt for Local/External AI').classes('w-full mt-2')

# Run initial simulation to populate data on startup
run_simulation()

ui.run()