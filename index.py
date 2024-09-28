from graphics import *
import numpy

# mandlebrot equation: z(n) = z(n - 1) ** 2 + c
# where c is a complex constant(in this case, points on the 2d window complex plan). 
#   If z(n) diverges, its not in the mandlebrot set(colored white)
#   If z(n) converges, its in the mandlebrot set(colored black)

zLimit = 2
iterations = 1000

def main():
    cols = 400
    rows = 400
    # centerX = rows / 2
    # centerY = cols / 2
    window = GraphWin("Mandlebrot", rows, cols, autoflush=False)
    c = complex(1, 1)
    xShift = rows / 2
    yShift = cols / 2
    # since the coordinates of this window are (0,0j) in the top left, 
    # we want the center to be at (200, 200j) where each pixel interval is 0.1
    for x in range(rows):
        for y in range(cols):
            c = complex((x - xShift) * 0.01, (yShift - y) * 0.01)
            if isInMandlebrotSet(c):
                window.plotPixel(x, y, "blue")


    isInMandlebrotSet(c)
    window.getMouse()
    window.close()

def isInMandlebrotSet(c):
    i = 1
    z = [complex(0)]
    while i <= iterations:
        next = z[i - 1] ** 2 + c
        nextMagnitude = numpy.sqrt((next.real)**2 + (next.imag)**2)
        if nextMagnitude > zLimit:
            return False
        z.append(next)
        i += 1
    
    return True
main()