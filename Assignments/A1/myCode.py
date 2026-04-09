import numpy as np
import matplotlib.pyplot as plt

# Constants and time
t = 4.3
Re, Te = 1, 1  # Earth: 1 AU, 1 Year
Rm, Tm = 1.52, 1.88  # Mars: 1.52 AU, 1.88 Years

# Omegas
omega_e = (2 * np.pi) / Te
omega_m = (2 * np.pi) / Tm

# Time array for orbits
t_orbit = np.linspace(0, 10, 1000)

# Copernicus
Xe = Re * np.cos(omega_e * t)
Ye = Re * np.sin(omega_e * t)
Xm = Rm * np.cos(omega_m * t)
Ym = Rm * np.sin(omega_m * t)

# Full Orbit paths
Xe_orbit = Re * np.cos(omega_e * t_orbit)
Ye_orbit = Re * np.sin(omega_e * t_orbit)
Xm_orbit = Rm * np.cos(omega_m * t_orbit)
Ym_orbit = Rm * np.sin(omega_m * t_orbit)

# Ptolemy
# Sun
Xp_sun = -Xe
Yp_sun = -Ye
Xp_sun_orbit = -Xe_orbit
Yp_sun_orbit = -Ye_orbit

# Mars
Xm_P = Xm - Xe
Ym_P = Ym - Ye
Xm_P_orbit = Xm_orbit - Xe_orbit
Ym_P_orbit = Ym_orbit - Ye_orbit

plt.figure(figsize=(14, 6))

# Graph 1: Copernicus Model
plt.subplot(1, 2, 1)
plt.plot(Xe_orbit, Ye_orbit, "b", alpha=0.3, label="Earth Orbit")
plt.plot(Xm_orbit, Ym_orbit, "r", alpha=0.3, label="Mars Orbit")
plt.plot(0, 0, "yo", markersize=12, label="Sun (Center)")
plt.plot(Xe, Ye, "bo", label=f"Earth at t={t}")
plt.plot(Xm, Ym, "ro", label=f"Mars at t={t}")
plt.title("Copernicus Model")
plt.xlabel("Distance (AU)")
plt.ylabel("Distance (AU)")
plt.legend(loc="upper right", fontsize="small")
plt.axis("equal")
plt.grid(True, linestyle=":")

# Graph 2: Ptolemy Model
plt.subplot(1, 2, 2)
plt.plot(Xp_sun_orbit, Yp_sun_orbit, "y", alpha=0.3, label="Sun Path")
plt.plot(Xm_P_orbit, Ym_P_orbit, "r", alpha=0.3, label="Mars Path")
plt.plot(0, 0, "bo", markersize=10, label="Earth (Center)")
plt.plot(Xp_sun, Yp_sun, "yo", label=f"Sun at t={t}")
plt.plot(Xm_P, Ym_P, "ro", label=f"Mars at t={t}")
plt.title("Ptolemy Model")
plt.xlabel("Distance (AU)")
plt.ylabel("Distance (AU)")
plt.legend(loc="upper right", fontsize="small")
plt.axis("equal")
plt.grid(True, linestyle=":")

plt.tight_layout()
plt.show()