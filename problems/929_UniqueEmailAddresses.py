# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:42:54 2020

@author: wyue
"""

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        domains = {}
        result = 0
        for e in emails:
            """
            at_index = e.find('@')
            dom_name = e[at_index+1:]
            loc_name = e[0:at_index]
            """
            loc_name,dom_name = e.split('@')
            ## Clean the local name
            ## Clean local name: 
            ## Ignore string after '+'
            plus_index = loc_name.find('+')
            if plus_index!=-1:
                loc_name = loc_name[:plus_index]
            ## Remove '.'
            loc_name = loc_name.replace('.','')
            
            if domains.get(dom_name)==None:
                domains[dom_name] = {loc_name:1}
                result += 1
            elif domains[dom_name].get(loc_name) == None:
                domains[dom_name] = {loc_name: 1}
                result += 1
                    
                
        return result
    
    


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(Solution().numUniqueEmails(emails))
