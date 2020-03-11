import pandas as pd
import altair as alt

# import theme_toronto.py file with functions. 
from hueniversitypy.theme_toronto import *

data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                 'B':[2, 3, 7, 4, 8, 4, 9], 
                 'C':[3, 6, 3, 5, 8, 2, 8] }))

# creating data to plot for tests

def test_chart_object():
    ''' A function that tests if an altair chart object is created  '''

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')

    assert str(type(test_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"
    
def test_colours():
    ''' A function that tests the correct colours an imported into the 
    altair chart based on the theme'''

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')

    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ['#002A5C', '#FFE498', '#E31837', '#008BB0', '#DAE5CD']
    
def test_font_type():
    ''' A function that tests the correct fonts are imported into the 
    altair chart based on the theme'''

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')

    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['font'] == 'Tahoma'
    assert plot_dict['config']['axisX']['labelFont'] == 'Tahoma'
    assert plot_dict['config']['axisX']['titleFont'] == 'Tahoma'
    assert plot_dict['config']['axisY']['labelFont'] == 'Tahoma'
    assert plot_dict['config']['axisY']['titleFont'] == 'Tahoma'
    
def test_font_size():
    ''' A function that tests the correct fonts sizes are used in the 
    altair chart based on the theme'''

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')

    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    
# defensive tests, expect failure

def wrong_colour():
    ''' A function that checks if the correct colours are used,
    shoud fail'''
    
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')
    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['range']['category'] != ['#002A5C', '#FFE498', '#E31837', '#008BB0', '#DAE5CD'], 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
    
def wrong_font():
    ''' A function that tests the if correct fonts are used,
    shoud fail'''
    
    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')

    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['font'] != 'Tahoma', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
    assert plot_dict['config']['axisX']['labelFont'] != 'Tahoma', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
    assert plot_dict['config']['axisX']['titleFont'] != 'Tahoma', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
    assert plot_dict['config']['axisY']['labelFont'] != 'Tahoma', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
    assert plot_dict['config']['axisY']['titleFont'] != 'Tahoma', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_toronto", theme_toronto) \n>>> alt.themes.enable("theme_toronto")'
