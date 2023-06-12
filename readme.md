## <span style="color:red">***Wa-tor simulator***</span>

Concept link : https://en.wikipedia.org/wiki/Wa-Tor

### <u>**Objective</u> :** 
Create a simple simulation with fishs and sharks that can interact together. 

### <u>**Details**</u> :
The planet is supposed to be a 3D donut and borders will deplace entity to the opposite side.

There is only two species in this simulation.
- **Fishs** : Can move, and reproduce after a few turns
- **Sharks** : Can move, reproduce after a few turns and eat fishs

Movement can only be done to adjacent cells (include borders). </br>
Fishs are immortals but die if eaten.
Sharks die after a few turns if they do not eat a fish (regen energy) and need to live a minimum amount of turns to reproduce. Sharks can only eat fishs at adjacent cells.

### <u>**Expected result**</u> :
Both species living together and not reaching extinction. </br>
If sharks kill all the fishs, they will die a few turns after (cannot get energy) </br>
If the number of fish decrease near extinction and the sharks cannot eat, sharks will die but fishs will then reproduce without any dying from shark attacks.</br> 
</br>


## <span style="color:red">***How I dit it***</span>

### <u>**Creation of the planet**</u> :
For the planet, the objective was to obtain an array of cells. I created a dictionary where the key are tuples (coordonates x and y) and the values are the content of the cell. (I could've also used a bi-dimensional list or array but I wanted to practice dictionary) </br></br>
That allowed me to easily change the content of the cells from a character (space or dot for empty cells) to class objects (Fishs, Sharks).
If I found a fish or a shark, I return its appearance (a character defined in their classes)

### <u>**Define entities**</u> :
First, I created a class **Fish()**. I made the functions to move at each turn and reproduce when a counter reach 0, then I reset it. </br>
To move, I check each cells at a distance of 1 and return a list of available positions, if there is one or more empty position, fish can move, otherwise not. </br>
</br>
Then I added a class **Shark()** that inherit the class Fish(). That allows me to reuse and to not write again my methods to move and reproduce. </br>
Finally, I did a method to eat fishs by checking adjacent cells, if not empty : move and eat fishs. </br>
</br>
To reach a balance, we then need to tweak values of reproduction (counter for both species), sharks lifetime and also the amount of population generated when we start.

### <u>**Generate entities**</u> :
Fishs must spawn for 1/3 of the planet size and sharks must spawn for 1/3 of the fish population size. </br>
I saved those numbers and then started a while loop to add entities at random coordonates until the number of entities for each species reachs the corresponding count. (Obviously, I checked if the cells were empty)