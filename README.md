# simple-games
Few simple games

#bullsNcows.py
simple paper game about guessing numbers
default is 4 figure number afaik, change bull_population in the script to increase/lower difficulty

I experienced some strange bugs when the guess in count_bulls_and_cows definition was sometimes NoneType. No idea how to reproduce that error, converting the guess to str seemed to fix the issue.
