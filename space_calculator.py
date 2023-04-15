import numpy as np

class IndexSpaceConverter:
    def __init__(self,N,L,d):
        if N%2 == 1: 
            print("N deve ser par, o atual valor de N:", N)
        self.N = N
        self.L = L
        self.d = d
        
        self.M = int(3*(N**2)//2)
        self.delta = L/N
        
        
    def get_is_above(self,m):
        """Returns whether the given index m is from an element of the upper plane"""
        return  m >= self.M//2

    def get_spatial_indices(self,m):
        """Returns the spatial indices of the given matrix index m"""
        if self.get_is_above(m):
            k = 1
            m -= self.M//2 # reduz ao caso da placa de baixo
        else:
            k = 0

        #o elemento está na parte inferior do L:
        if m < (self.N**2)//2: 
            i = m%self.N
            j = m//self.N
        
        # o elemento está na parte superior do L:
        else:
            # reduz ao caso da parte inferior do L:
            m -= (self.N**2//2)

            i = m %(self.N//2) #+ (self.N**2//2)
            j = m//(self.N//2) + (self.N//2) # esta em cima
            
        return i, j, k
    


    def get_spatial_positions(self,m):
        i, j, k = self.get_spatial_indices(m)

        x = (i+0.5)*self.delta
        y = (j+0.5)*self.delta
        z = k*self.d

        return x, y, z

    def generate_spatial_matrix(self):
        matrix_espacial = -np.ones(shape = (self.N, self.N, 2))
        for m in range(self.M):
            i, j, k = self.get_spatial_indices(m)
            #print(f"m = {m}, i = {i}, j = {j}, k = {k}")
            matrix_espacial[self.N-1-j][i][k] = m
        
        return matrix_espacial

    def distancia(self,m,n):

        xm, ym, zm = self.get_spatial_positions(m)        
        xn, yn, zn = self.get_spatial_positions(n)

        rm = np.array([xm, ym, zm])
        rn = np.array([xn, yn, zn])

        distancia_quadrado = ((rm - rn)**2).sum()
        return np.sqrt(distancia_quadrado)


# testando
if __name__ == "__main__":
    N = 4
    conversor = IndexSpaceConverter(N = N, L = 16, d = 1)

    print("M:",conversor.M)
    print("N:",conversor.N)
    print("L:",conversor.L)
    print("delta:",conversor.delta)
    print()
    
    print(conversor.distancia(10,3))# deve ser sqrt(2)*(L-delta) ~ 16.97
    print()
    
    matrix_espacial = conversor.generate_spatial_matrix()
    print( matrix_espacial[:,:,0] )
    print( matrix_espacial[:,:,1] )

    # [[10. 11. -1. -1.]
    # [ 8.  9.  -1. -1.]
    # [ 4.  5.   6.  7.]
    # [ 0.  1.   2.  3.]]

    # [[22. 23. -1. -1.]
    # [ 20. 21. -1. -1.]
    # [ 16. 17.  18. 19.]
    # [ 12. 13.  14. 15.]]