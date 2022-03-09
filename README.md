# Refreshable Braille Display

In this project we make a Refreshable Braille Display (RBD) that provides a cost-effective alternative to bulky Braille textbooks and current expensive Braille texts, making it more readily accessible to a larger population of visually impaired individuals. It consists of a microcomputer, a 3D-printed chassis and commodity and low-power motors that together form an 8-grid Braille display. Existing displays provide a similar functionality, but cost between $3000 and $15000 dollars making them inaccessible to those who require them. Our project is a proof of concept showing that we can provide this functionality for a fraction of the cost. This project can be easily augmented to provide more functionality.

Link to our submission video for Make OHI/O 2022: [Youtube](https://www.youtube.com/watch?v=me4idjuad2g)

The software implementation for the RBD is written in Python and it consists of the following systems:
 1. An image-to-text conversion system powered by Google's [Tesseract](https://tesseract-ocr.github.io/) project.
 2. Text-to-Braille conversion and interfacing with GPIO pins on an NVIDIA Jetsen Nano board.

The hardware comprises mostly of custom 3D-printed parts for the 8-dot universal Braille pattern.  In addition, we use:
 1. Pager motors for the up-down motion of the dots on the RBD.
 2. A synchronized LED grid to view the displayed Braille pattern, which is mostly for aiding Braille tutors.

We also plan to include a microphone input with speech-to-text processing and a functionality to perform Google search for documents. 
