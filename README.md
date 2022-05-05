# A Sudoku Solver in Python

I wrote this sudoku solver after learning about Python generator expressions and the magical `eval()` function in [Peter Norvig](www.norvig.com)'s wonderful Udacity [course](https://www.udacity.com/course/design-of-computer-programs--cs212). That said, I haven't been able to bring myself to look at [his sudoku solver](http://www.norvig.com/sudoku.html) yet, since it will likely be a thing of great elegance that will make my version look terrible :-( 


**Usage**

`python sudoku.py input_filename.txt`


input_filename.txt has the puzzle that needs to be solved. 
- one line for each row of the puzzle
- zeros for blank cells
- cells separated by spaces
 
 (It may be easier to just copy the file 'puzzle.txt' from the repo and modify it)
 
 
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


 

 
