# Jaxon

9/9 4 hours (roughly, I wasn't paying attention because I didn't realize we needed to track it at the time.)

```
- Got the base of the game set up. I created the Game and Player class as well as the GameObject parent class. I have the skeleton ready for the actual game to be created. Almost finished the setup phase where players hide their ships, but there was a weird bug, so I went to bed.
```

9/10 2 hours

```
- Mostly work on the Github repo, but a little more coding. Added documentation folder, organized project requirements into a Github issue.
```

Probably about 3 more hours

```
- I did tid bits between the last chunk of time and this chunk
- Peter resolved a bug that was holding me back and I begain implementing the ability to orient your ships when you place down 1xN ships where N > 1.
```

<details>
  <img width="718" alt="Screenshot 2024-09-10 at 10 21 23 PM" src="https://github.com/user-attachments/assets/fab53248-c921-43d3-9ea7-9b3edc05bae9">
</details>

9/11 4 Hours

```
- Met with Pete and helped do some work on his part. I then refactored the whole repo for several hours. The main work that was done was changing the board to be more dynamic by including the new Tile and Ship class on the board, instead of just regular strings. I also refactored the hiding mechanics to be transactional and only accept transactions where all the coords the ship is attempting to be placed on are valid. This prevents a ship from being overlapped or going off the board. I actually just realized there's a bug where the initial placement can overlap a ship. Oops. I'll have to fix that tomorrow.
```

9/13 2 hours

```
- Team meeting and refactored a bunch of stuff
```

9/14 7.5 hours

```
- Had to refactor a bunch of the game. Resolved a major bug where if one part of the ship was hit then the whole thing would say it was hit. Peter helped.
```

# Achraf

9/11 3 hours

```
-I implemented the logic for taking turns between the players, and then, I also implemented the attack logic where players can fire at each other's boards and receive feedback on whether the shot was a hit or miss. This changes introduced a bug where every shot that was fired was counted as a miss shot.
```

9/12 4 hours

```
-Met with Jaxon, and he explained more of the logic game to me and that was a big step for me to resolve the issue
-Integrated the opponent board logic so that each player corectly tracks their opponent's board, reflecting hits and misses accurately.
-Tried to implement some destroy the ships logic. The way the logic is right now, everytime a ship is hit, then the player who shot, wins which should't be the case. the player's should only win if the opp board is empty. (This is going to be part of Timi implementation)
```

9/15 1h

```
Added comments and documentations
```

# Timi

# Peter
- 9/10 2 hours
```
Had a team meeting where we went over the setup code that Jaxon made and talked about who was going to implement which features moving forward. We also talked about a bug Jaxon found where you weren't able to hide the correct amount of ships

Later that evening, I fixed the bug and pushed it to the repo
```
- 9/12 15 minutes, GTA meeting
- 9/13 1 hour
```
Met with the team to talk about what was left to be done. The main problems left were a bug where the player's board would not appear correctly when a hit occurred and adding logic for the game to end when all ships were sunk.
```
- 9/14 5 hours 
```
Implemented end game logic so that the right person wins when all the opponent's ships are sunk. Met up with Jaxon to work together and make sure we could resolve conflicts since we were both working at the same time. We also worked on the previous bug where the player's board wouldn't appear correctly, but Jaxon was able to fix it.
```

# Pete

- 9/11 spent about 2 hours familarizing myself with the repo then beggining to add to my section of work. Then met with jaxon to get his help with navigating the repo and refractoring the board bulid.