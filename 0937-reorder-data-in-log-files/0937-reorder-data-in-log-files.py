class Solution(object):
    def reorderLogFiles(self, logs):
        
        res1, res2 = [],[]

        for log in logs:
            if (log.split()[1].isdigit()):
                res2.append(log)
            else:
                res1.append(log)

        res1.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        res1.extend(res2)

        return res1


        