class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image)==0:
            return 
        prevColor = image[sr][sc]
        if prevColor == newColor:
            return image
        helper(image,sr,sc,newColor,prevColor)
        return image
        

def helper(image,sr,sc,newColor,prevColor):
    if image[sr][sc]==prevColor:
        image[sr][sc]=newColor
        helper(image,sr-1,sc,newColor,prevColor) if sr>0 else None
        helper(image,sr,sc-1,newColor,prevColor) if sc>0 else None
        helper(image,sr+1,sc,newColor,prevColor) if sr<len(image)-1 else None
        helper(image,sr,sc+1,newColor,prevColor) if sc<len(image[0])-1 else None
    else:
        return None
    
    


