import json
import matplotlib.pyplot as plt

"""
Simple plotting for visualizing and debugging.
"""

def plot_geojson(json_data, color='k'):
    """
    Plot the features in a GeoJSON dict.
    """
    fig = plt.figure()
    ax = fig.gca()
    
    for feature in json_data['features']:

        coords = feature['geometry']['coordinates']
        xy = zip(*coords)
        
        ax.plot(xy[0], xy[1], color)
        
    ax.axis('equal')
    plt.show()
