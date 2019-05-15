# sudoku-solver
Sudoku Solver in Python


**Example**  

Let's say the puzzle you want to solve is in puzzle.txt

`cat puzzle.txt`


 0  0  0  5  0  0  0  0  2   
 0  1  0  8  0  0  9  0  0   
 0  8  9  0  0  2  0  0  5   
 0  0  3  0  0  0  0  0  0   
 4  7  5  0  0  0  1  2  8  
 0  0  0  0  0  0  7  0  0  
 3  0  0  4  0  0  5  7  0  
 0  0  8  0  0  6  0  3  0  
 9  0  0  0  0  3  0  0  0  

To solve it:
 
 `python sudoku.py puzzle.txt`
 
 *Output*
 
(6, 3, 4, 5, 9, 7, 8, 1, 2)  
(5, 1, 2, 8, 3, 4, 9, 6, 7)  
(7, 8, 9, 6, 1, 2, 3, 4, 5)  
(1, 2, 3, 7, 8, 5, 6, 9, 4)  
(4, 7, 5, 3, 6, 9, 1, 2, 8)  
(8, 9, 6, 2, 4, 1, 7, 5, 3)  
(3, 6, 1, 4, 2, 8, 5, 7, 9)  
(2, 5, 8, 9, 7, 6, 4, 3, 1)  
(9, 4, 7, 1, 5, 3, 2, 8, 6)  



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
 
