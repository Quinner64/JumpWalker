import h5py
import pandas as pd
import matplotlib.pyplot as plt

with h5py.File('./project_data.h5', 'r') as hdf:
    walking_data = hdf['Lucas/Walking'][:]
    jumping_data = hdf['Lucas/Jumping'][:]

# simple acceleration vs time for walking and jumping

fig, ax = plt.subplots()

# walking

ax.plot(walking_data[:, 0], walking_data[:, 4], color = 'green', label = 'Walking')

# jumping

ax.plot(jumping_data[:, 0], jumping_data[:, 4], color = 'orange', label = 'Jumping')
ax.set_title('Acceleration Magnitude vs Time')
ax.set_ylabel('Acceleration Magnitude')
ax.set_xlabel('Time')
ax.legend()

plt.show()

# comparison of the three accelerations in a 3D graph

# walking 3D graph

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(walking_data[:, 1], walking_data[:, 2], walking_data[:, 3], color='green', label='Walking')

ax.set_title('3D Scatter Plot of Acceleration for Walking')
ax.set_xlabel('Acceleration X')
ax.set_ylabel('Acceleration Y')
ax.set_zlabel('Acceleration Z')
ax.legend()

plt.show()

# jumping 3D graph

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(jumping_data[:, 1], jumping_data[:, 2], jumping_data[:, 3], color='orange', label='Jumping')

ax.set_title('3D Scatter Plot of Acceleration for Jumping')
ax.set_xlabel('Acceleration X')
ax.set_ylabel('Acceleration Y')
ax.set_zlabel('Acceleration Z')
ax.legend()

plt.show()

# plotting the acceleration magnitude for a single segment

# walking window

walking_window = walking_data[0:0+500, :]
fig, ax = plt.subplots()

ax.plot(walking_window[:, 0], walking_window[:, 4], color = 'green', label = 'Walking')
ax.set_title('Walking Acceleration Magnitude vs Time For 1 Segment')
ax.set_ylabel('Walking Acceleration Magnitude')
ax.set_xlabel('Time')
ax.legend()

plt.show()

# jumping window

jumping_window = jumping_data[0:0+500, :]
fig, ax = plt.subplots()

ax.plot(jumping_window[:, 0], jumping_window[:, 4], color = 'orange', label = 'Walking')
ax.set_title('Jumping Acceleration Magnitude vs Time For 1 Segment')
ax.set_ylabel('Jumping Acceleration Magnitude')
ax.set_xlabel('Time')
ax.legend()

plt.show()

# comparing individual axis of acceleration

# X vs Y axis

fig, ax = plt.subplots()
ax.scatter(walking_data[:, 1], walking_data[:, 2], color='green', label='Walking')
ax.scatter(jumping_data[:, 1], jumping_data[:, 2], color='orange', label='Jumping', alpha=0.1)
ax.set_title('Acceleration in x vs Acceleration in y')
ax.set_xlabel('x Acceleration')
ax.set_ylabel('y Acceleration')
ax.legend()

plt.show()

# Y vs Z axis

fig, ax = plt.subplots()
ax.scatter(walking_data[:, 2], walking_data[:, 3], color='green', label='Walking')
ax.scatter(jumping_data[:, 2], jumping_data[:, 3], color='orange', label='Jumping', alpha=0.1)
ax.set_title('Acceleration in y vs Acceleration in z')
ax.set_xlabel('y Acceleration')
ax.set_ylabel('z Acceleration')
ax.legend()

plt.show()

# X vs Z axis

fig, ax = plt.subplots()
ax.scatter(walking_data[:, 1], walking_data[:, 3], color='green', label='Walking')
ax.scatter(jumping_data[:, 1], jumping_data[:, 3], color='orange', label='Jumping', alpha=0.1)
ax.set_title('Acceleration in x vs Acceleration in z')
ax.set_xlabel('x Acceleration')
ax.set_ylabel('z Acceleration')
ax.legend()

plt.show()

data = {
    'Jacob': {
        'version': '1.1.11',
        'build': '10011',
        'fileFormat': '1.15',
        'deviceModel': 'iPhone11,8',
        'deviceBrand': 'Apple',
        'deviceBoard': '',
        'deviceManufacturer': '',
        'deviceBaseOS': '',
        'deviceCodename': '',
        'deviceRelease': '15.6',
        'depthFrontSensor': '1',
        'depthFrontResolution': '',
        'depthFrontRate': '',
        'depthBackSensor': '0',
        'depthBackResolution': '',
        'depthBackRate': ''
    },
    'Lucas': {
        'version': '1.1.11',
        'build': '10011',
        'fileFormat': '1.15',
        'deviceModel': 'iPhone10,8',
        'deviceBrand': 'Apple',
        'deviceBoard': '',
        'deviceManufacturer': '',
        'deviceBaseOS': '',
        'deviceCodename': '',
        'deviceRelease': '16.0',
        'depthFrontSensor': '1',
        'depthFrontResolution': '',
        'depthFrontRate': '',
        'depthBackSensor': '0',
        'depthBackResolution': '',
        'depthBackRate': ''
    },
    'Hayden': {
        'version': '1.1.11',
        'build': '10011',
        'fileFormat': '1.15',
        'deviceModel': 'iPhone12,8',
        'deviceBrand': 'Apple',
        'deviceBoard': '',
        'deviceManufacturer': '',
        'deviceBaseOS': '',
        'deviceCodename': '',
        'deviceRelease': '15.7.3',
        'depthFrontSensor': '1',
        'depthFrontResolution': '',
        'depthFrontRate': '',
        'depthBackSensor': '1',
        'depthBackResolution': '',
        'depthBackRate': ''
    }
}

meta_data = pd.DataFrame(data).T

meta_data = meta_data.reset_index()
meta_data = meta_data.melt(id_vars=['index'], var_name='Property', value_name='Value')
meta_data = meta_data.pivot(index='Property', columns='index', values='Value').reset_index()

meta_data.columns.name = None
meta_data = meta_data[['Property', 'Jacob', 'Lucas', 'Hayden']]

meta_data.to_excel('metadata.xlsx', index=False)


