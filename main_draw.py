import cv2
import numpy as np
import imutils


def change_brightness(inp_img, value=30):
	img = inp_img.copy()
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h, s, v = cv2.split(hsv)
	v = cv2.add(v,value)
	v[v > 255] = 255
	v[v < 0] = 0
	final_hsv = cv2.merge((h, s, v))
	img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
	return img


inp_img = "forest_land335.jpg"
# inp_img = "hanumanji.jpg"
# inp_img = "lion.jpg"
inp_img = "nezuko.jpg"

img = cv2.imread(inp_img)

side = 1000 
squeeze = 100
skip = 10
font_size = 0.7
offset = 10
font = 5


"""
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
"""

essay = """Now that you've learned what a system of linear equations is and when they are singular or non-singular, it is time for some visualizations.
It turns out that linear equations can easily be visualized as lines in the coordinate plane. This is because you have two variables. If you have three variables,
they are planes in space. If you have more variables, they look like high-dimensional space. But let's not worry about that yet. Since linear equations can be
represented as lines, then systems of linear equations can be represented as arrangements of lines in the plane. This way, you can visualize their solutions and
their singularity or non-singularity in a much clear way. How can you visualize, for example, the equation a plus b equals 10 as a line? First, let us get a grid 
in which the horizontal axis represents a, which is the price of an apple, and the vertical axis represents b, which is the price of a banana. Now let's look at solutions to
this equation a plus b equals 10. In other words, pairs of numbers that add to 10. What you'll do is put them in this plot. Two obvious solutions are the point 10, 0. The a coordinate,
the price of an apple, is 10 and the b coordinate, the price of a banana, is zero because 10 plus 0 is 10. Another obvious solution is the point 0, 10 where a is zero and b equals 10. Other 
solutions are the point 4, 6 because 4 plus 6 equals 10. This is a equals 4 and b equals 6 or the point 8, 2 where a equals and b equals 2. Notice that you can also have negative solutions, 
for example minus 4,14. Now, this makes no sense in the world problem because an apple cannot cost minus 4. But these are two numbers that add to 10, minus 4 plus 14 equals 10. This is a 
legitimate solution to the equation. You can also have negative solutions like 12, minus 2. Now notice that all these points form a line. In fact, every single point in this line is solution 
to the equation. You can then associate the equation a plus b equals 10 with this line. Now let's do another equation. Say the equation a plus 2b equals 12. That means points for which the 
horizontal coordinate plus two times the vertical coordinate add to 12. Some solutions for this equation are the point 0,6 since 0 plus 2 times 6 equals 12. The point 12,0 because 12 plus 2 
times 0 is 12. The point 8,2 because 8 plus 2 times 2 is 12. Again, negative solutions like minus 4,8 for example, because minus 4 plus 2"""

essay = 'Jai Shri Ram | '

essay = """The lion (Panthera leo) is a large cat of the genus Panthera native to Africa and India. It has a muscular, broad-chested body; short, rounded head; round ears; and a hairy tuft
at the end of its tail. It is sexually dimorphic; adult male lions are larger than females and have a prominent mane. It is a social species, forming groups called prides. 
A lion's pride consists of a few adult males, related females, and cubs. Groups of female lions usually hunt together, preying mostly on large ungulates. The lion is an apex and keystone predator;
although some lions scavenge when opportunities occur and have been known to hunt humans, lions typically do not actively seek out and prey on humans.
The lion inhabits grasslands, savannas and shrublands. It is usually more diurnal than other wild cats, but when persecuted, it adapts to being active at night and at twilight.
During the Neolithic period, the lion ranged throughout Africa and Eurasia from Southeast Europe to India, but it has been reduced to fragmented populations in sub-Saharan Africa
and one population in western India. It has been listed as Vulnerable on the IUCN Red List since 1996 because populations in African countries have declined by about 43% since the early 1990s.
Lion populations are untenable outside designated protected areas. Although the cause of the decline is not fully understood, habitat loss and conflicts with humans
are the greatest causes for concern"""



img = imutils.resize(img, height=squeeze) # to reduce number of colors in image
img = imutils.resize(img, height=side)
op = change_brightness(img, value=-180) # to put image as background with reduced brightness
# op = np.ones((side,side, 3), dtype='uint8')*100 # to have blank white or gray image as background 


index = 0
for i in range(0,len(img),skip):
	for j in range(0,len(img[0]),skip):

		# to get the color of that pixel
		color = list(img[i][j]) # (0, 255, 0)
		color = ( int (color [0]), int (color [1]), int (color [2])) 

		char = essay[index]
		index+=1
		if index>=len(essay):
			index = 0 # restart the text writer

		# print(color, char)
		cv2.putText(op, char, (j+offset,i*2+offset), font, font_size, color, 1, cv2.LINE_AA) # x, y , size, thick

cv2.imshow('test',op)
cv2.imwrite(f'{inp_img}_{font}_output.jpg',op)
cv2.waitKey(0)
cv2.destroyAllWindows()
