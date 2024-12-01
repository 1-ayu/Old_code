class Solution:
    def spiralOrder(self, matrix: List[List[int]])-> List[int]:
        result=list()

        left,right=0, len(matrix[0])
        top,bottom=0, len(matrix)
        
        # Continue until the boundaries overlap
        while left<right and top<bottom:
            # Step1: Traverse the top row from left to right
            for i in range(left,right):
                result.append(matrix[top][i])
            top+=1  #Move the top boundary down

            # Step2: Traverse the right column from top to bottom
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right -=1  #Move the right boundary left

            #  Check if there are still elements to process
            if not (left<right and top<bottom):
                break 

            #  Step 3: Traverse the bottom row from right to left
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1[i]])
            bottom -=1  #Move the bottom boundary up

            # Step 4: Traverse the left column from bottom to top
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left -=1  # Move the left boundary right

        # Return the spiral ordered result list
        return result