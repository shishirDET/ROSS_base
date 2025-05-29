import ross as rs

# uncomment the lines below if you are having problems with plots not showing
import plotly.io as pio

pio.renderers.default = "browser"

# ======================================================================================
# OPTION No.1:
# Using zip() method
L = [28.25, 10, 4, 4, 25, 4, 4, 15, 10, 5]
i_d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
o_d = [10, 10, 12, 12, 16, 12, 12, 12, 10, 10]
shaft_elements = [
    rs.ShaftElement(
        L=length * 1e-3,  # Convert to meters
        idl=idl * 1e-3,
        odl=odl * 1e-3,
        material=steel,
        shear_effects=True,
        rotary_inertia=True,
        gyroscopic=True,
    )
    for length, idl, odl in zip(L, i_d, o_d)
]
shaft_elements

# Option2: From excel file
# shaft_file = Path("shaft_si.xls")
# shaft = rs.ShaftElement.from_table(
#     file=shaft_file, sheet_type="Model", sheet_name="Model"
# )

# ======================================================================================
# from E and G_s
steel = rs.Material(name="Steel", rho=7810, E=211e9, G_s=81.2e9)
# from E and Poisson
steel2 = rs.Material(name="Steel", rho=7810, E=211e9, Poisson=0.3)
# from G_s and Poisson
steel3 = rs.Material(name="Steel", rho=7810, G_s=81.2e9, Poisson=0.3)

print(steel)
# returning attributes
print("=" * 36)
# print(f"Young's Modulus: {steel.E}")
# print(f"Shear Modulus:   {steel.G_s}")

# ======================================================================================
# OPTION No.1:
# Using zip() method
n_list = [1, 9]
m_list = [0.45, 0.45]
Id_list = [0.0, 0.0]
Ip_list = [0.0, 0.0]
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

stfx = 100e6
stfy = 100e6
# bearing0 = rs.BearingElement(0, kxx=stfx, kyy=stfy, cxx=0, n_link=7)
bearing1 = rs.BearingElement(3, kxx=stfx, kyy=stfy, cxx=0)
bearing2 = rs.BearingElement(6, kxx=stfx, kyy=stfy, cxx=0)
bearings = [bearing1, bearing2]

# ======================================================================================
# pm0 = rs.PointMass(n=7, m=30)
# pointmass = [pm0]

# ======================================================================================
rotor1 = rs.Rotor(shaft_elements, disk_elements, bearings)
# rotor1= rotor1.add_nodes([20e-3])

path = "rotorModels/testRotor3.toml"
# Save the rotor to a file
test_rotor = rotor1.save(path)
# test_rotor= rotor1.save("testRotor1.toml")
print(f"Rotor saved to: {path}")
