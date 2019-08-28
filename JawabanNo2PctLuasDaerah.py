import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



conn = mysql.connector.connect(
    host =  '127.0.0.1',
    port = 3306,
    user = 'kinanweda',
    passwd = 'Jimbamamba22',
    database = 'world' 
)

q = ''' select t.Name as Negara_ASEAN, t.SurfaceArea as LuasDaratan
from city c inner join  country t
on c.ID = t.Capital
where t.Name in ('Brunei','Cambodia','East Timor','Indonesia','Laos','Malaysia','Myanmar','Philippines','Singapore','Thailand','Vietnam') 
order by Negara_ASEAN asc '''
x = conn.cursor()
x.execute(q)
listsdc = x.fetchall()

sns.set()
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
df = pd.read_sql(q,con=conn)
Negara = list(df['Negara_ASEAN'])
Populasi = list(df['LuasDaratan'])
warna=['red','orange','aqua','yellow','lightgreen','green','lightblue','blue','violet','purple','black']

def func(pct, populasi):
    absolute = int(pct/100.*np.sum(populasi))
    return "{:.1f}%".format(pct)
wedges, texts, autotexts = ax.pie(Populasi, labels=Negara ,autopct=lambda pct: func(pct, Populasi),
                                  textprops=dict(color="k"))
plt.title('Persentasi Luas Daratan Negara ASEAN')
plt.setp(autotexts, size=10, weight='bold')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
