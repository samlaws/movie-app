# movie-app
Python app comprised of a few short scripts to scrape an online movie database.

## cli.py
  
  CLICK based cli, currently very barebones
  
## functions.py

  The file containing the functions
  
  __Search:__ Navigates to the chosen films imdb page and exits the program if there are no films or if the top result is not the film the user wants.

  __Recomender:__ Gets a list of the recommended movies from the searched film
 
  __Details:__ Gets some basic information from the page of the searched film

# TODO
  
  * Improve CLI by making it loop after a function is called and adding options such as verbose
  * Allow the user to try again if the functions fail rather than exiting the program
