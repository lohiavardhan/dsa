class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, n1):
        res = n1
        while self.parents[res] != res:
            self.parents[res] = self.parents[self.parents[res]]
            res = self.parents[res]
        return res
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += p2
        else:
            self.parents[p1] = p2
            self.rank[p2] += p1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UF(len(accounts))

        emailToAcc = {}
        for index, emails in enumerate(accounts):
            for e in emails[1:]:
                if e in emailToAcc:
                    uf.union(index, emailToAcc[e])
                emailToAcc[e] = index

        for emails in emailToAcc:
            emailToAcc[emails] = uf.find(emailToAcc[emails]) 


        res_dict = defaultdict(list)
        for email, account in emailToAcc.items():
            res_dict[account].append(email)
        
        answer = []

        for account, emails in res_dict.items():
            emails.sort()
            answer.append([accounts[account][0]] + emails)

        return answer