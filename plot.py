from matplotlib import pyplot as plt
from collections import Counter
 
class Plot() :     
    def drawJobTitle(self, data):
        cnt = {}
        for x in data :
            y = x['job_title']
            if y in cnt: 
                cnt[y] += 1
            else : 
                cnt[y] = 1
        
        df = sorted(cnt.items(), key=lambda cnt:cnt[1])
        df.reverse()
        
        label = []
        value = []

        if len(df) <= 10 : 
            for x, y in df :
                label.append(x)
                value.append(y)
        else : 
            for x, y in df[0:8]:
                label.append(x)
                value.append(y)
            label.append('other')
            sum_other = 0
            for x, y in df[9:len(df) - 1] :
                sum_other += y
            value.append(sum_other)

        fig = plt.figure(figsize =(20, 14))
        plt.pie(x=value, labels=label)
        
        plt.savefig('static/jobTitle.jpg')
    
    def drawLocation(self, data):
        cnt = {}
        for x in data :
            y = x['location']
            if y in cnt :
                cnt[y] += 1
            else : 
                cnt[y] = 1
        label = list(cnt.keys())
        value = list(cnt.values())

        fig = plt.figure(figsize =(20, 14))
        plt.pie(x=value, labels=label)
        
        plt.savefig('static/location.jpg') 
