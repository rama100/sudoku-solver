# sudoku-solver
Sudoku Solver in Python


**Example**  

Let's say the puzzle you want to solve is in puzzle.txt

`cat puzzle.txt`


 5  0  0  2  0  0  0  8  0  
 8  0  0  1  0  5  0  0  0   
 0  0  0  0  0  0  0  0  3   
 4  2  6  9  0  0  0  5  0   
 0  9  0  0  0  0  0  0  6   
 7  0  0  0  4  0  0  0  0   
 0  0  0  0  3  0  8  2  0   
 0  0  0  4  2  0  0  0  1   
 0  1  0  0  0  0  0  7  0   

To solve it:
 
 `python sudoku.py puzzle.txt`
 
 *Output*
 
5  6  4  2  7  3  1  8  9  
8  3  9  1  6  5  7  4  2  
1  7  2  8  9  4  5  6  3  
4  2  6  9  1  8  3  5  7  
3  9  8  7  5  2  4  1  6  
7  5  1  3  4  6  2  9  8  
9  4  7  6  3  1  8  2  5  
6  8  5  4  2  7  9  3  1  
2  1  3  5  8  9  6  7  4  



**Usage**

In general:

`python sudoku.py input_filename.txt`


input_filename.txt has the puzzle that needs to be solved. 
- one line for each row of the puzzle
- zeros for blank cells
- cells separated by spaces
 
 (It may be easier to just edit 'puzzle.txt' in the repo)
 
 
 **Approach**
 
The approach was inspired by something I saw in [Peter Norvig](www.norvig.com)'s Udacity lectures. That said, I haven't been able to bring myself to look at [his sudoku solver](http://www.norvig.com/sudoku.html) yet, since it will likely be a thing of elegance, cleverness and great beauty that will make my version look pedestrian and make me weep :-) 
 
