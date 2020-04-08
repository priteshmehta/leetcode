def countElements(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        uniq_element = set(arr)
        counter = 0 
        for n in arr:
            if n+1 in uniq_element:
                counter+=1

        print(counter)


countElements([1,3,2,3,5,0])

