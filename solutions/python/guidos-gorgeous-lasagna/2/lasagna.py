"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
"""int: The expected bake time in minutes for the lansagna."""
def bake_time_remaining(elapsed_bake_time):
    """ Calculate the bake time remaining. 
    :param elapsed_bake_time: int - the number of minutes the lasagna has already         baked. 
    :return int - how many minutes are left to bake the lasagna. """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    bake_time_remaining(30)
    
def preparation_time_in_minutes(number_of_layers):
    """ calculate the preparations time based on the number of layers. 
    :param number of layers: int - the number of layers added to the lasagna.
    :return: int - total preparation time (2 minutes per layer)."""
    return number_of_layers * 2
    preparation_time_in_minutes()

def elapsed_time_in_minutes (number_of_layers, elapsed_bake_time):
           
    """Calculate the total elapsed cooking time (prep + baking).
    
    :param number of layers: int - how many layers were added.
    :param elapsed_bake_time: int - how many minutes the lasagna has already baked. 
    :return : int - total time spent cooking (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO: define the 'elapsed_time_in_minutes()' function below.



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
