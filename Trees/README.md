# Outline:

- The build is a very basic recursive fractal tree that has been created using the inbuilt turtle module that comes with python. A detailed description lies below.

# Purpose:

- Ever since I saw the thumbnail of [Coding Train's fractal tree video](https://www.youtube.com/watch?v=0jjeOYMjmDU&t=500s), I was instantly enamoured by the symmetric, chaotic and yet purposeful design - I wanted to recreate it and therefore after trial and error and a few tutorials, I was able to generate my recursive fractal tree using turtle thereby solidifying my understanding of recursion.

# Description:

- The main function of the program initialises the turtle screen and deals with repositioning, colours etc and calls upon the draw_tree function which accepts the branch length and the turtle (t).
- The draw_tree draws the inital forward branch and then works from right to left recursively, drawing the left branches after finishing up with the ones on the right - at each stage the branch length reduces by 12 to avoid an infinite tree as the main if condition acts as a base case.
- After finishing up with that level, it simply proceeds backwards and then continues on its path!
- Its extremely enjoyable to mess around with this code and visualise how the fractal evolves over time!
