# Notes

## Game State
All state is public unless explicitly marked "(private)"
- phase and turn information
  - current game phase (i.e. game start, main phase, finished)
  - special game phase (i.e. asking players to drop loads)
  - current turn number
  - current player state
    - turn phase (i.e., move, build)
    - how much money spent
    - how far moved
  - list of all effectful commands made so far, in order
  - player that has won, if any
- effect states (for each of these, is it enabled and what turn does it end?)
  - rainbow bridge enabled/disabled
  - magical link enabled/disabled
  - can't build track state (all players)
  - halted train state (all players)
  - half rate areas (all players, specific areas)
  - no pick up or deliveries at cities (all players, specific cities)
  - no upgrading trains
  - no changing ships
  - no changing foremen
- deck information
  - for all resources, how many left?
  - foremen deck
    - discard pile
    - (private) deck
  - ships deck
    - discard pile
    - (private) deck
  - demand/event deck
    - discard pile
    - (private) deck
  - train deck (i.e., which trains are available to upgrade)
- per-player state
  - identifier
  - demand cards
  - train
  - ship
  - foreman
  - resources carried
  - gp (technically private according to the rules, but we'll leave it public)
  - color
  - effects (including turn when the effect is disabled)
    - skip turn?
    - can build track?
- static geography state
  - Notes on representation: I'd expect to use the 'odd-r' horizontal layout from [Red Blob](http://www.redblobgames.com/grids/hexagons/). A milepost (point) on the board is uniquely specified by the 3-tuple (map # (e.g. 0 for aboveground, 1 for undergroudn), q, r). A link is a tuple of mileposts.
  - 3d array of mileposts
  - milepost info
    - terrain (i.e., mountain, alpine, plain, ...)
    - traversable by ship? (We're making a special hack here where some LAND points will be traversable by ship to keep the board to a proper grid of hexagons, instead of the slightly ad-hoc nature of the real board. The implication is that if laying track between two mileposts and at least one of them is 'traversable by ship' you must be crossing an ocean inlet.)
    - name if named (i.e., nothing, 'Uloggh', 'Nordkassel', etc.)
    - region name (i.e., ocean, northern wastes, glyth gamel, etc.)
  - special links: collection of tuples of name and collection links (i.e. [('underground entrances', links), ('magical connection', links), ('rainbow bridge', links)])
  - rivers: tuples of river names and collections of links (i.e. all the links that river crosses)
  - map of city name to available resources (i.e., bluefeld -> hops, bremmner -> steel)
- dynamic geography state
  - track
    - per player list of links


## Progression:
1. Start of Game
  1. Determine turn order
  2. Players start with 60 gold, teapot, some color
  3. Get 3 demand cards
  4. Deal out all foremen so everyone has the same number, each player picks a foreman in turn order (there is a procedure for redealing foremen specified in the rules)
  5. Each player picks a starting city
2. Normal turn
  1. Decide to turn in all demand cards?
  2. Move Phase
    - can switch foreman
    - can move (and possibly pay toll) (a move can be invalid if underground and you can't pay the bribe)
    - pick up or drop off resources
      - Dropping off resources:
        1. Get gp, leave resource
        2. Pick a card
        3. If event card, do the event card, go back to #2 (NOTE: This could end the game and make another player win, for example if Rainbow Bridge comes up. It could also interrupt the turn and require the input of other players, for instance if Vampires Attack and a player must choose which load to lose.)
  3. Ship Phase (decide to get ship or not, decide to move ship, disembark, etc.)
  4. Build Phase (switch foreman, upgrade train, build track)

The game is over when a player has connected 7 cities via uninterrupted track and has 250 gp.

Event card effects:
  - Can't build track (in an area, certain players)
  - Track destroyed
  - Trains halted (in an area)
  - Trains move half rate (in an area)
  - Players lose a turn
  - Players lose a load
  - No pickups or deliveries at cities
  - Rainbow bridge enabled
  - Wizard strike (magical connections are disabled)
  - Trains can't be upgraded
  - All ships go to the nearest port
  - No boarding or disembarking from ships
  - No exchanging foremen
  - War tax (pay some money based on how much you have)

Foremen effects:
  - Catman: jungle -> 1gp
  - Dwarf: mountains -> 1gp
  - Elf/Half-elf: forest -> 1gp
  - Human: lowered cost for bridges
  - Orc: obtains bribes, doesn't pay a bribe
  - Troll: Build underground only at a cost of 2gp, doesn't pay a bribe
  - Wee folk: can pick from 3 ships at no cost

## Command/Response structure:

All interactions are JSON posts to the server at "/api", like

```
{
  "cmd": "build-track",
  "player_id": 1,
  "start": [0, 20, 30],
  "end": [0, 20, 31]
}
```

And a response would look like

```
{
  "response": "build-track-response",
  "status": "ok"
}
```

For now, let's ignore authentication. We can very easily bolt it on later, requiring a token with each request.

We'll probably need some general purpose commands like "get-state", which just returns all the public state.