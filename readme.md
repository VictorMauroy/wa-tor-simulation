## ***Wa-tor simulator***

Concept link : https://en.wikipedia.org/wiki/Wa-Tor

### **Objective :** 
Create a simple simulation with fishs and sharks that can interact together. 

### **Details** :
The planet is supposed to be a 3D donut and borders will deplace entity to the opposite side.

There is only two species in this simulation.
- **Fishs** : Can move, and reproduce after a few turns
- **Sharks** : Can move, reproduce after a few turns and eat fishs

Movement can only be done to adjacent cells (include borders). </br>
Fishs are immortals but die if eaten.
Sharks die after a few turns if they do not eat a fish (regen energy) and need to live a minimum amount of turns to reproduce. Sharks can only eat fishs at adjacent cells.

### **Expected result** :
Both species living together and not reaching extinction. </br>
If sharks kill all the fishs, they will die a few turns after (cannot get energy) </br>
If the number of fish decrease near extinction and the sharks cannot eat, sharks will die but fishs will then reproduce without any dying from shark attacks.