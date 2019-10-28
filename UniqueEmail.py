class Solution:

    def strip(self, email):

        parts = email.split("@")
        rtr = parts[0].replace(".", "")

        if(not "+" in rtr):
            return rtr + "@" + parts[1]
        else:
            return rtr[:rtr.index("+")] + "@" + parts[1]

    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        
        emails = [self.strip(i) for i in emails]
        Mset = set(emails)
        
        return len(Mset)


if __name__ == "__main__":
    
    test = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    sol = Solution().numUniqueEmails(test)

    print(sol)