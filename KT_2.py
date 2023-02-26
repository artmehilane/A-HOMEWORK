def smallerNumbersThanCurrent(nums):
        
        vastus = []
        for i in range(len(nums)):
            lugeja = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    lugeja += 1
            vastus.append(lugeja)
        return vastus


##
programm, mis loeb kokku palju on väiksemaid numbreid arvust

võrdleme elemente
loenduri lähtestame nulliks ja suurendame iga kord kui leiame vaste

Testitud leetcode poolt kasutades automaatteste

Python 3


        
