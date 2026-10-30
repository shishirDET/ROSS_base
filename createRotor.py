import ross as rs

# uncomment the lines below if you are having problems with plots not showing
import plotly.io as pio

pio.renderers.default = "browser"

# ======================================================================================
# from E and G_s
steel = rs.Material(name="Steel", rho=7810, E=211e9, G_s=81.2e9)
# from E and Poisson
steel2 = rs.Material(name="EN24", rho=7810, E=211e9, Poisson=0.3)
# from G_s and Poisson
steel3 = rs.Material(name="Steel", rho=7810, G_s=81.2e9, Poisson=0.3)

print(steel2)
# returning attributes
print("=" * 36)
# print(f"Young's Modulus: {steel.E}")
# print(f"Shear Modulus:   {steel.G_s}")

# ======================================================================================
# OPTION No.1:
# Using zip() method
n_list = [2, 11]
m_list = [0.080, 0.099]
Id_list = [18.6e-6, 18.7e-6]
Ip_list = [28e-6, 36.2e-6]
disk_elements = [
    rs.DiskElement(
        n=n,
        m=m,
        Id=Id,
        Ip=Ip,
    )
    for n, m, Id, Ip in zip(n_list, m_list, Id_list, Ip_list)
]
disk_elements

# ======================================================================================
# bearing2 = rs.BearingElement(
#     n=0,
#     kxx=np.array([0.5e6, 1.0e6, 2.5e6]),
#     kyy=np.array([1.5e6, 2.0e6, 3.5e6]),
#     cxx=np.array([0.5e3, 1.0e3, 1.5e3]),
#     frequency=np.array([0, 1000, 2000]),
# )

# print(bearing2)
# print("="*79)
# print(f"Kxx coefficient: {bearing2.kxx}")
# bearing2.plot(['kxx', 'kyy'])

# Bearing1
bearing_1_node = 4
stfx1 = 0.1e6
stfy1 = 0.1e6
# bearing 2
bearing_2_node = 9
stfx2 = .4e6
stfy2= .4e6

# bearing0 = rs.BearingElement(0, kxx=stfx, kyy=stfy, cxx=0, n_link=7)
bearing1 = rs.BearingElement(bearing_1_node, kxx=stfx1, kyy=stfy1, cxx=0)
bearing2 = rs.BearingElement(bearing_2_node, kxx=stfx2, kyy=stfy2, cxx=0)
bearings = [bearing1, bearing2]

# ======================================================================================
# pm0 = rs.PointMass(n=7, m=30)
# pointmass = [pm0]

# ======================================================================================
# OPTION No.1:
# Using zip() method

# DET200
L = [8.5, 28.524, 9.776, 6.9, 3.5, 14, 59.25, 14, 3, 3.5, 6.95, 5.05, 10]
i_d = [0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
o_dl = [6, 6.4, 6.4, 8, 8, 11, 16, 16, 8, 8, 7.9, 7.9, 7.9]
o_dr = [6, 6.4, 6.4, 8, 8, 16, 16, 11, 8, 8, 7.9, 7.9, 7.9]
shaft_elements = [
    rs.ShaftElement(
        L=length * 1e-3,  # Convert to meters
        idl=idl * 1e-3,
        idr=idr * 1e-3,
        odl=odl * 1e-3,
        odr=odr * 1e-3,
        material=steel,
        shear_effects=True,
        rotary_inertia=True,
        gyroscopic=True,
    )
    for length, idl, idr, odl, odr in zip(L, i_d, i_d, o_dl, o_dr)
]
shaft_elements

# Option2: From excel file
# shaft_file = Path("shaft_si.xls")
# shaft = rs.ShaftElement.from_table(
#     file=shaft_file, sheet_type="Model", sheet_name="Model"
# )

# ======================================================================================
rotor1 = rs.Rotor(shaft_elements, disk_elements, bearings)
# rotor1= rotor1.add_nodes([20e-3])

path = "rotorModels/DET200.toml"
# Save the rotor to a file
test_rotor = rotor1.save(path)
# test_rotor= rotor1.save("testRotor1.toml")
print(f"Rotor saved to: {path}")

# plotting the rotor model
rotor1.plot_rotor(check_sld=True).show()  # Plot the rotor model