from pathlib import Path
import ross as rs
import numpy as np

# uncomment the lines below if you are having problems with plots not showing
import plotly.io as pio

pio.renderers.default = "browser"

# ======================================================================================
path = "rotorModels/kj450.toml"

if not Path(path).exists():
    print(f"File {path} does not exist. Please create the rotor model first.")
    exit()
else:
    rotor = rs.Rotor.load(path)
    print(f"Rotor model loaded from {path}")
print("Rotor total mass = ", np.round(rotor.m, 2))
print("Rotor center of gravity =", np.round(rotor.CG, 2))

# plotting the rotor model
rotor.plot_rotor(check_sld=True).show()  # Plot the rotor model

# ***********STATIC ANALYSIS****************
# static = rotor.run_static()
# static.plot_free_body_diagram().show()  # Plot the free body diagram of the rotor

# ***********Modal ANALYSIS****************
rotor_speed = 110000/60 * 2 * np.pi # rad/s
modal = rotor.run_modal(rotor_speed, num_modes=15)
# print(f"Undamped natural frequencies:\n {modal.wn}")

#enter the mode number you want to plot
mode = 6
for i in range(mode):
    # modal.plot_mode_2d(mode, frequency_units="Hz").show()  # Plot the 2D mode shape of the rotor
    modal.plot_mode_3d(i, frequency_units="RPM").show()  # Plot the 3D mode shape of the rotor

# *****************Campbell****************
samples = 31
speed_range = np.linspace(1, rotor_speed, samples)

campbell = rotor.run_campbell(speed_range)
campbell.plot([1, 2],frequency_units="Hz").show()

# ************************* UCS Map*************************
stiff_range = (4, 9)
ucs_results = rotor.run_ucs(stiffness_range=stiff_range, num=20, num_modes=25,)
ucs_results.plot(frequency_units="Hz").show()  # Plot the UCS map
