class Solution(object):
    def reorderLogFiles(self, logs):
        
        res1, res2 = [],[]

        for log in logs:
            if (log.split()[1].isdigit()):
                res2.append(log)
            else:
                res1.append(log)

        res1.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        for i in range(len(res1)):
            res1[i] = ("".join(res1[i]))

        res1.extend(res2)

        return res1


        