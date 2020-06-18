# Outline:

- Koch curve and by extension a Koch snowflake built using recursion and the turtle module. A more detailed description lies below.

# Purpose:

- After I had programmed a fractal tree, I was intrigued about what else I could build with recursion and fractals and so I went scouring for projects - the Mandelbrot and Julia sets seemed more intermediate and I was looking for a project to ease myself in with, and therefore when I found the Koch curve and by extension snowflake, I was very excited!
- The build was extremely engaging and I find these sort of recursive fractals are more enjoyable as I can visualise the recursion and see the progress of my code in real time, thereby better understanding recursion.

# Description:

- A Koch curve is drawn by first constructing an equilateral triangle and then splitting each side into 3 parts.
- Then on each middle part, an equilateral triangle is to be drawn and this process is to repeated.
- See also: [Khan Academy's excellent description](https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area/koch-snowflake/v/koch-snowflake-fractal).
- In programming terms, the creation of a Koch Curve can be depicted using the L-system depiction:
    - F=F+F--F+F
    - Here F indicates go forward, + means turn left by 60 degrees and - is turn right by 60 degrees.
- To complete the snowflake, repeat the construction of this partial Koch curve thrice, each time turning right by 120 degrees!
- More interestingly, the depth controls how much detail the snowflake is drawn using, I'd recommend playing with it to fully understand how this shape with finite area yet infinite perimeter is created!
