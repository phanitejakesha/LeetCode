"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employeeImpMap = {}
        employeeSubMap = {}
        for i in range(0,len(employees)):
            employeeImpMap[employees[i].id] = employees[i].importance
            for j in range(0,len(employees[i].subordinates)):
                if employees[i].id in employeeSubMap:
                    employeeSubMap[employees[i].id].append(employees[i].subordinates[j])
 
                else:
                    employeeSubMap[employees[i].id]= [employees[i].subordinates[j]]
        
        importanceVal =  employeeImpMap[id]
        
        if id in employeeSubMap:
            subQue = employeeSubMap[id]
        else:
            subQue = []
        ans = []
        while len(subQue)!=0:
            ans = ans + subQue
            q = []
            for i in range(0,len(subQue)):
                if subQue[i] in employeeSubMap:
                    q = q + employeeSubMap[subQue[i]]
            subQue = q
        
        for i in range(0,len(ans)):
            importanceVal+=employeeImpMap[ans[i]]
        return importanceVal
        
        
        
        
