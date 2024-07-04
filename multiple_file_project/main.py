import support      # Importing the support module
# from support import *     # Importing all the functions and variables from the support module
# from support import var, add_2_numbers     # Importing the var and add_2_numbers from the support module

test = support.Test()
print(test.a)
test.some_method()
print(support.var)
print(support.add_2_numbers(10, 20))


# we also can work with external modules, such as PyGames for games, Matplotlib for data visualization, BeautifulSoup for web scraping, etc.
# to install these we have to use pip in the powershell or cmd