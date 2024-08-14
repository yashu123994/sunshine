import pandas as p
from functools import reduce
data={'Numbers':[1,2,3,4,5],'Letters':['A','B','C','D','E']}
df=p.DataFrame(data)
sq=df['Numbers'].map(lambda x:x**2)
fi=list(filter(lambda x:x%2==0,df['Numbers']))
po=reduce(lambda x,y:x*y,df['Numbers'])
print("DataFrame:\n",df)
print("/nmap for squaring:/n",sq)
print("/nreduce for product:/n",sq)
