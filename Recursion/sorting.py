class sorting():


    def sort(self,arr):
        if(len(arr)==0):
            return 
        value = arr[-1]
        arr.pop()
        self.sort(arr)
        self.place_element(arr,value)
        return(arr)

    def place_element(self,arr,n):
        if(len(arr)==0 or arr[-1]<=n):
            arr.append(n)
            return
        
        value = arr[-1]
        arr.pop()
        self.place_element(arr,n)
        arr.append(value)
        

s = sorting()
# s.sort([5,7,2,1,3,9,6])
print(s.sort([5,7,2,1,3,9,6]))

# print(place_element([4],6))
