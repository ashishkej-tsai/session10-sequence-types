import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have 3 edges/vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def no_vertices(self):
        return self._n
    
    @property
    def no_edges(self):
        return self._n
    
    @property
    def circum_radius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180.0 / self._n

    @property
    def edge_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2.0 * self.edge_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.edge_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.no_edges == other.no_edges 
                    and self.circum_radius == other.circum_radius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.no_vertices > other.no_vertices
        else:
            return NotImplemented

class Polygon_Sequence:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('number of vertices for largest polygon in the sequence must be greater than 3')
        self._n = n
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, n+1)]
        
    def __len__(self):
        return self._n - 2
    
    def __repr__(self):
        return f'Polygons(n={self._n}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, key=lambda p: p.area/p.perimeter,reverse=True)
        return sorted_polygons[0]