# HexProver

Interactive prover of [Hex](https://en.wikipedia.org/wiki/Hex_(board_game)) diagrams.

![Internal connection example](images/internal_connection.png) ![Strategy Viewer example](images/view_strategy.png) 

## Dependencies
+ Python3
+ [pyGtk3](https://pygobject.readthedocs.io/en/latest/getting_started.html)
+ [numpy](https://pypi.org/project/numpy/) (on Windows: "pacman -S mingw-w64-x86_64-python3-numpy")

## Running

To check it out, run
```
./hex_gui.py custom.hdg
```

and you should see an example of [Tom's move](https://www.hexwiki.net/index.php/Tom%27s_move), where you can play red hexes.

![Internal connection example](images/internal_connection.png) ![Strategy Viewer example](images/view_strategy.png) 

## Concept

The program is intended to lead the user prove a validity of a hex template. Except a very simple automation (described below), it is not using any extensive search / AI -- it is all up to the user.

Hex template is a partial Hex board with some red hexes, some blue hexes (these are in fact equivalent to empty hexes for the purpose of the template). Red plays second, and the template is valid red has a strategy which guarantees that there will be a connection between the upper edge ur any hex marked with up-arrow to the lower edge or any hex marked with down-arrow.

Red plays second. So why it seems as if red played first? Similarly as in proving validity on HexWiki, it needs to first see a move that red would like to play, and after red connects, blue starts automatically systematically interfering in all the positions that red needed.

After all the possible red's moves are examined, the windows torns light green, and the user can now plays blue, and can see what strategy was built.

## Goal splitting

In Hex, it is often useful to describe a strategy as an independent combination of local strategies. This can be done in two very similar (but slightly different) ways. If you click on a red node, there will be two subtasks to prove: that the template with this node marked down is valid, and that the same template with this node marked up is valid. By immediate clicking on the same hex, you can choose if you prove first up or down.

However, these two strategies are not allowed to share any nodes, so after proving one connection, all the nodes used for this proof are removed from the diagram.

If you want to prove a two red nodes disconnected from both border edges are connected, drag from one hex to the other.

For a technical reason, the program mainly operates on templates where red plays second, so if you are in a position where the last move is blue, you will nod be able to do this split, and you have to make a red move first. I know this can be a bit confusing / annoying, perhaps it will get better in some further version...

## Automation

HexProver closes some subgoals automatically. In particular:
* A simple fork -- when there are two different direct connections.
* A lemma -- HexProver remembers all the subgoals that were proven in a particular problem (until the problem gets restarted). If it sees a subgoal that has been already proven, it closes it automatically. Again, because of the design of operating on templates where red plays second, this only works on such subgoals.

Automation can be turned On / Off by the appropriate button in the top bar. It can be useful to turn it off for two reasons:
* to get to understand better the underlying logic (and not be confused by too many closed subgoals)
* sometimes, automation uses other hexes than the user intended, which breaks e.g. the intended goal split.

## Controls

* Escape -- exit the program. Note that the program remembers which problems were solved (in `./proof` directory) but not partial 
* PgUp / PgDown -- select problem. Warning: when a problem is changed, all the proving progress is lost. (except when the problem has been fully solved)
* 'a' / 's' -- toggle automation / run once
* Left click -- in proving mode either split on red node, or play red node, in viewing strategy play blue node
* Mouse drag from a red not to another -- make internal connection
* Right click -- Select current opponent's (blue) move

## Data format

HexProver uses its custom text-like `.hdg` format for Hex templates, as can be seen in
[custom.hdg](custom.hdg) or [templates-drking.hdg](templates-drking.hdg), the latter is the list of templates by [David King](https://www.drking.org.uk/hexagons/hex/templates.html). Its use should be fairly intuitive -- only note that there must not be any hole (written by space) in a line. If there should be, write `X` instead.

HexProver is also capable of parsing some problems by [http://www.mseymour.ca/hex_puzzle/](Matthew Seymour's Hex puzzles) -- in particular those puzzles where the objective is to connect, and the first player is supposed to pass. To load them, download [Puzzle Data](http://www.mseymour.ca/hex_puzzle/puzzle_data.js), extract the inside of `puzzle_data = '...'` into a file `puzzle_data.json` (the `json` extension is important), and run HexProver on that file.
