def theme_alberta():
    """ 
    Applies a University of Alberta theme to all subsequential altair plot objects so they are displayed with the U of A visual identity.
    See the visual identity at https://www.ualberta.ca/toolkit/visual-identity/our-colours. 
    Four palettes based on the U of A visual identity guidelines can be selected: 'alpha', 'beta', 'gamma' and 'delta'.
	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the U of A visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_alberta', theme_alberta)
    >>> alt.themes.enable('theme_alberta')

    """

    # Code attribution: Sergio Sanchez
    # https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    # University font
    font = "Arial"
    labelFont = "Arial"

    # Specify colour palette for Alberta
    alberta_palette = ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"]

    return {
        "config": {
            # Title font and size
            "title": {
                "fontSize" : 18,
                "font": font,
                "anchor": "start",
                "fontColor": "#000000"
            } ,
            # Axes font and sizes
            "axisX": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "X Axis Title (units)"
            },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "Y Axis Title (units)"
            },
            # Add colour palette
            "range": {
                "category": alberta_palette
            }
        }
    }
