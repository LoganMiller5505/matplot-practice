# matplot-practice
 A repository containing simple programs to practice matplotlib functionalities and gain proficiency

## Included Programs

### Math 1627 11 Problem Plus 18

This came from as an assigned practice problem in my Calculus II class that I used in order to enhance my program graphing skills.

The images shown here are generated automatically by the program for a user-input **n** value.

For n = 10, the following graphs are output:

#### N=10 Problem Graph
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n10graph.png?raw=true)
#### N=10 X & Y Graphs
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n10xy.png?raw=true)

*Notice how the points do not converge at this low n value*

This, of course, means that the values of these points are NOT equal to the true value of the function as it approaches infinity, as displayed by the following console output:
#### N=10 Console Output
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n10console.png?raw=true)


For n = 5000, the following graphs are output:

#### N=5000 Problem Graph
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n5000graph.png?raw=true)
#### N=5000 X & Y Graphs
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n5000xy.png?raw=true)

*Notice how the points DO clearly converge now that n is a much higher value*

This, of course, means that the value of these points ARE equal to the true value of the function as it approaches infinity, as displayed by the following console output:
#### N=5000 Console Output
![alt text](https://github.com/LoganMiller5505/matplot-practice/blob/main/blob/n5000console.png?raw=true)

**The results of this program SUPPORT the answer I found by completing the problem mathematically using infinite limits.**

#### Takeaways

This was a good introduction into how to use matplotlib and introduced me to the basics of plots as well as subplots.
This project also provided an additional check to ensure I got the correct answer on my assigned math problem. Programming this kind of logic, and checking it with graphs and outputs, is likely a procedure I will use in future math classes on large problems like these that can sometimes be simpler to program rather than break down solely mathematically.

In the future, I would like to add functionality by adding interactive elements, or "widgets", directly into the plot, rather than relying solely on terminal input. Introducing animation could be another way to make these graphs more dynamic as well.