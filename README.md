# simple-games
Few simple games.

#bullsNcows.py
* Simple paper game about guessing numbers.
* Default is 4 figure number afaik, change bull_population in the script to increase/lower difficulty.
* Score evalution is based only on default cases with 4 figures. It does not make sense for other difficulties.

*I experienced some strange bugs when the guess in count_bulls_and_cows definition was sometimes NoneType. No idea how to reproduce that error, converting the guess to str seemed to fix the issue.*
