class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        cnt=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    cnt+=1
                    side=1      #dimension-->starts with 1
                    #expand the square
                    while i+side<n and j+side<m:
                        flag=True
                        for k in range(side+1): #first check aju baju then go for diagonal one
                            if mat[i+side][j+k]==0 or mat[i+k][j+side]==0:
                                flag=False
                                break       #do not check for diagonal then
                        if flag==False:
                            break
                        else:
                            cnt+=1
                            side+=1
        return cnt
                        


                 