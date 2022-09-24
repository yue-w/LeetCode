
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        #return self.method1(arriveAlice, leaveAlice, arriveBob, leaveBob)
        return self.method2(arriveAlice, leaveAlice, arriveBob, leaveBob) # preferred method
    
    def method1(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Call built-in functions
        """
        y = 2022
        aam = int(arriveAlice[:2])
        aad = int(arriveAlice[3:5])
        alm = int(leaveAlice[:2])
        ald = int(leaveAlice[3:5])
        
        aadate = date(y, aam, aad)
        aldate = date(y, alm, ald)
        
        bam = int(arriveBob[:2])
        bad = int(arriveBob[3:5])
        blm = int(leaveBob[:2])
        bld = int(leaveBob[3:5])
        badate = date(y, bam, bad)
        bldate = date(y, blm, bld)
        
        if aadate > bldate or aldate < badate:
            return 0
        
        arr = max(aadate, badate)
        lea = min(aldate, bldate)
        d = (arr - lea).days
        return abs(d) + 1
                            

    def method2(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Preferred method.
        Use a base date to compare the differences between two dates
        """
        def get_days(date):
            month = int(date[0:2])
            day = int(date[3:5])
            days = 0
            for i in range(month):
                days += days_month[i]
            days += day
            return days
            
        days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        L1 = get_days(arriveAlice)
        R1 = get_days(leaveAlice)
        L2 = get_days(arriveBob)
        R2 = get_days(leaveBob)
        
        L = max(L1, L2)
        R = min(R1, R2)
        return max(0, R - L + 1)
    
        

