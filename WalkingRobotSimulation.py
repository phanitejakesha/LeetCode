class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        leftMap = {'N':'W','W':'S','S':'E','E':'N'}
        rightMap = {'N':'E','W':'N','S':'W','E':'S'}
        direction  = 'N'
        pos = [0,0]
        
        obstacleMap = {}
        for i in range(0,len(obstacles)):
            obstacleMap[str(obstacles[i][0])+":"+str(obstacles[i][1])] = [obstacles[i][0],obstacles[i][1]]
            
            
        maxVal = 0
        for i in range(0,len(commands)):
            if commands[i] == -1:
                direction = rightMap[direction]
            elif commands[i] == -2:
                direction = leftMap[direction]
            else:
                if direction == 'N':
                    
                    for i in range(0,commands[i]):
                        # print(i,commands[i],pos)
                        intermedPosition = [pos[0],pos[1]+1]
                        interString = str(intermedPosition[0]) +":" + str(intermedPosition[1])
                        # print(interString)
                        if interString in obstacleMap:
                            # print(interString)
                            break
                        else:
                            pos = [pos[0],pos[1]+1]
                         
                elif direction == 'E':
                     for i in range(0,commands[i]):
                        intermedPosition = [pos[0]+1,pos[1]]
                        interString = str(intermedPosition[0]) +":" + str(intermedPosition[1])
                        # print(interString)
                        if interString in obstacleMap:
                            
                            break
                        else:
                            pos = [pos[0]+1,pos[1]]
                            

                elif direction == 'S':
                    
                    for i in range(0,commands[i]):
                        intermedPosition = [pos[0],pos[1]-1]
                        interString = str(intermedPosition[0]) +":" + str(intermedPosition[1])
                        # print(interString)
                        if interString in obstacleMap:
                            # print(interString)
                            break
                        else:
                            pos = [pos[0],pos[1]-1]
                    
                elif direction == 'W':
                    for i in range(0,commands[i]):
                        intermedPosition = [pos[0]-1,pos[1]]
                        interString = str(intermedPosition[0]) +":" + str(intermedPosition[1])
                        # print(interString)
                        if interString in obstacleMap:
                            break
                        else:
                            pos = [pos[0]-1,pos[1]]
                if maxVal < pos[0]**2 + pos[1]**2:
                    maxVal = pos[0]**2 + pos[1]**2
        return maxVal
            
            
        
