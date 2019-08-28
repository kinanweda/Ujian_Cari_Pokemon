import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



conn = mysql.connector.connect(
    host =  '127.0.0.1',
    port = 3306,
    user = 'kinanweda',
    passwd = '12345',
    database = 'world' 
)

q = ''' select t.Name as Negara_ASEAN, t.Population as Populasi_Negara, t.GNP, c.Name as Ibukota, c.Population as Populasi_Ibukota 
from city c inner join  country t
on c.ID = t.Capital
where t.Name in ('Brunei','Cambodia','East Timor','Indonesia','Laos','Malaysia','Myanmar','Philippines','Singapore','Thailand','Vietnam') 
order by Negara_ASEAN asc '''
x = conn.cursor()
x.execute(q)
listsdc = x.fetchall()

sns.set()

df = pd.read_sql(q,con=conn)
Negara = list(df['Negara_ASEAN'])
Populasi = list(df['Populasi_Negara'])
plt.bar(Negara,Populasi, color=['red','orange','aqua','yellow','lightgreen','green','lightblue','blue','violet','purple','black'],zorder=1)
for i in range(len(Negara)):
    plt.text(i-.5,Populasi[i],str(Populasi[i]), size=7)

plt.subplots_adjust(left=.12,bottom=.24,right=.9,top=.88, wspace=.4, hspace=.4)

plt.title('Diagram Batang')
plt.grid(True)
plt.xlabel('Negara ASEAN')
plt.ylabel('Populasi x 100jt Jiwa')
plt.xticks(rotation=65)
plt.show()
