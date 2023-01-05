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

        def func(pct) : 
            return "{:1.1f}%".format(pct)

        fig = plt.figure(figsize =(20, 14))
        plt.pie(x=value, labels=label,  autopct=lambda pct: func(pct))
        
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

        def func(pct) : 
            return "{:1.1f}%".format(pct)

        fig = plt.figure(figsize =(20, 14))
        plt.pie(x=value, labels=label, autopct=lambda pct: func(pct))
        
        plt.savefig('static/location.jpg') 

    def drawSalary(self, data):
        cnt = []
        for x in data :
            y = x['monthly_salary']
            if y > 10000 : 
                y = 10000
            cnt.append(y)
         
        
        fig = plt.figure(figsize =(20, 14))

        bins_list = [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
        plt.hist(x=cnt, bins=bins_list ,color='cyan', linewidth=1)
        plt.xticks(bins_list)
        plt.xlabel('monthly_salary (>10000 set as 10000) ')
        
        plt.savefig('static/monthly_salary.jpg') 