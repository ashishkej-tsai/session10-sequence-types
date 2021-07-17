
# EPAi3.0 Session10 Sequence Types Assignment
Assignment to check our knowledge of Sequence Types.

1. A regular strictly convex polygon is a polygon that has the following characteristics:
    1. all interior angles are less than 180
    2. all sides have equal length
![Polygons](./ywVyfMa1Zt.png "Polygons")

2. For a regular strictly convex polygon with:
- n edges (=n vertices)
- R circumradius
- interiorAngle=(n−2)⋅180n
- edgeLength,s=2⋅R⋅sin(πn)
- apothem,a=R⋅cos(πn)
- area=12⋅n⋅s⋅a
- perimeter=n⋅s

3. Objective 1 [pts:400]:
    1.Create a Polygon Class:
        where initializer takes in:number of edges/vertices, circumradius
        that can provide these properties:
        - edges
        - vertices
        - interior angle
        - edge length
        - apothem
        - area
        - perimeter
        that has these functionalities:
        - a proper __repr__ function
        - implements equality (==) based on # vertices and circumradius (__eq__)
        - implements > based on number of vertices only (__gt__)

4. Objective 2 [pts:600]:
    1. Implement a Custom Polygon sequence type:
        where initializer takes in:
        - number of vertices for largest polygon in the sequence
        - common circumradius for all polygons
        that can provide these properties:
        - max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
        that has these functionalities:
        - functions as a sequence type (__getitem__)
        - supports the len() function (__len__)
        - has a proper representation (__repr__)

5. Results:
- Implement these 2 classes as a separate module. Access these modules in Google Colab or Deep Note or local Notebook (later you'd need to upload to GitHub)
- Run Objective 1 module to show that the functionalities are implemented properly
- Run Objective 2 module and show which polygon is efficient for n = 25
- You are submitting a link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them on GitHub Actions.
- All your code must be publicly accessible (make sure to open all links in an incognito window before submitting)


## test 
