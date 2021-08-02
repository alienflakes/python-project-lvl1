***
This is a little handbook guide for this Brain Games project (:

I hope this makes peeking around this project
a little easier and things I use here and there
would be somewhat more understandable.


So now, behold... here is my Project 01 for Hexlet Python Course (:<

The Brain Games project is expected to be a Terminal trinket
with three math games, each one having three rounds.
Failing a question will finish the game and you'll have to
start over.

First up there's Is Even Game, where you answer whether
the prompted number is even or not.

Second one is the Calc Game, the answer is the result of a
math expression (could be addition, subtraction or division).

Third game - GCD Game - puts the greatest common divisor
of the pair of suggested numbers as an answer.

Fourth one is the Progression Game. Find the missing
number in an arithmetic progression and that would be
the answer.

The fifth, final game is Prime Game, in which you have
to find out whether the number is prime or not.

All of primarely used numbers (and Calc operations) are randomly generated.
number_01 has a range of 0 to 100.
number_02 has a range of 0 to 20
number_03 has a range of 0 to 20

02 and 03 have a shorter range for the sake of 
the Games being a little easier with smaller numbers,
but ranges can be changed anytime in the game_flow.py's cycle,
where they are originally generated.

Also, in GCD Game, where I use number_01 as a base to create 
the nums for finding their GCD, it's cut down by dividing (//)
it by 10, bc using (0, 100) as a base makes these tasks
just a liiitle too difficult. This can be fixed too if
any wandering mathematician stumbles across this project.

And in the Progression Game number_01 and number_03 are
also modified to fit into the game rules and avoid
using numbers that are too big.


The Games have a similar logic that goes like this:
-welcome the player and get their name,
-start the first game:
    1. explain the rules, 
    2. show the question, 
    3. get an answer,
    4. answer is right: repeat steps 2-3 three times,
    4.1 answer is wrong: failure message, finish the games;
-start the second game:
    -repeat 1-4.1;
-start the third game:
    -repeat 1-4.1;
-etc etc ...
-congratulate on the win.

So it was convinient to make a separate game-flow module (game_flow.py)
that wraps any game into it's useful state (dependent on it's rules)
that can be later used from the scripts that would build the whole Project.

Each games' logic is fit into custom classes and then given to the
game-flow module to build them - the flow and game modules
lay in the brain_games/games dir.

Numbers are generated in the game_flow.py cycle, bc generating them inside
the classes would make them repeat on each game round.
There was another solution to this, but for now it's easier
to bring up the randomizer directly in the game flow cycle.

I'll probably add things up later, this is the base for now! (:
