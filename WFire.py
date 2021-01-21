# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np


# %%
cd E:\PYTHON PROJECTS\\FIRST_AUST_WFIRE

# %%
table = pd.read_csv("CleanedDataV4.csv")


# %%

table


# %%
print('Latitude and longitude show the coordinates of the fire.')


# %%
lat = table['latitude'].values
lon = table['longitude'].values
temp = table['fire_temperature'].values

date = table['acq_date'].values

# %%

fig = plt.figure(figsize=(12,5))
m = Basemap(
            llcrnrlon=103.784763, llcrnrlat=-44.590467,
            urcrnrlon=164.90369, urcrnrlat=-6.105602) 
m.shadedrelief()
m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.drawstates(color='black')
m.drawrivers(color='blue')

m.scatter( x = lon, y = lat,
    c=(temp),
          cmap='Reds_r', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire...intensity}$')
plt.clim(25, 325)

value_of_intensity = 25 
for i in ['mistyrose','coral','darkred']:
    plt.scatter([],[], c = i , alpha=1,
                s = 150, label = 'Fire intensity: '+str(value_of_intensity)+ ' Celsius')
    value_of_intensity = value_of_intensity + 50
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left')

x,y = m(115.857048,-31.953512)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(111.24316514,-31.98198667, "Perth" )

x,y = m(130.82958978,-12.47305101)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(126.14062607,-11.69527273, "Darwin" )

x,y = m(144.946457,-37.840935)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(142.41796821,-39.63953756, "Melbourne" )

x,y = m(151.209900,-33.865143)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(151.84863254,-33.60730141, "Sydney" )

x,y =(151.750000,-32.916668)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(151.342224,-33.425018)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(143.850006,-37.549999)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	150.893143,-34.425072)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	153.399994,	-28.016666)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	146.816956,	-19.258965)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	149.186813,-21.144337)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	152.350006,		-24.850000)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y = m(153.021072,-27.470125)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(153.86132866,-27.19210716, "Brisbane" )

x,y = m(149.128998,-35.282001)
plt.plot(x,y,'ok', markersize=10, marker='*')
plt.text(150.73242188,-35.51792029, "Canberra" )

x,y = m(118.95117134,-25.73657274)
plt.text(x,y,"Western\n Australia",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m(131.23828232,-19.64258753)
plt.text(x,y,"Northern\n Territory",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')  

x,y = m(141.328125,-21.66559708)
plt.text(x,y,"Queensland",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m(131.60742134,-29.25956498)
plt.text(x,y,"South\n Australia",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m(142.55859375,-32.5171737)
plt.text(x,y,"New South\n Wales",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m(142.68164277,-37.03413685)
plt.text(x,y,"Victoria",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

plt.title('Wildfire\n in Australia', fontsize= 20, color = 'black')
plt.savefig("WFAUST.png")

# %%
data = table['acq_date']
data_array = data.values


# %%

i = 0
mounth_8 = [0]*32
mounth_9 = [0]*31
day = 1
mounth = 8
for i in data_array :
    if i == '8/'+ str(day) + '/2019':
        mounth_8[day] = mounth_8[day] + 1
    else:
        day = day + 1 
        if day == 32:
            break
        mounth_8[day] = mounth_8[day] + 1

data_m9 = data.tail(len(data) - sum(mounth_8)).values

day = 1
for i in data_m9 :
    if i == '9/' + str(day) +'/2019':
        mounth_9[day] = mounth_9[day] + 1
    else:
        day = day + 1
        if day == 31:
            break
        mounth_9[day] = mounth_9[day] + 1
sum(mounth_8)+sum(mounth_9)

nr = 1
for i in mounth_8:
    if(i > 0):
        new_table = table.head(i)
        table = table.tail(len(table)-i)
        lat = new_table['latitude'].values
        lon = new_table['longitude'].values
        temp = new_table['fire_temperature'].values
        date = new_table['acq_date'].values
        fig = plt.figure(figsize=(12,5))
        m = Basemap(
                    llcrnrlon=103.784763, llcrnrlat=-44.590467,
                    urcrnrlon=164.90369, urcrnrlat=-6.105602) 
        m.shadedrelief()
        m.drawcoastlines(color='black')
        m.drawcountries(color='black')
        m.drawstates(color='black')
        m.drawrivers(color='blue')

        m.scatter( x = lon, y = lat,
            c=(temp),
                cmap='Reds_r', alpha=1, marker = 'o')
        plt.colorbar(label=r'${\rm Fire...intensity}$')
        plt.clim(25, 325)

        value_of_brightness = 25
        for i in ['darkred','coral','mistyrose']:
            plt.scatter([],[], c = i , alpha=1,
                        s = 150, label = 'Intensity: '+str(value_of_brightness) + ' C')
            value_of_brightness = value_of_brightness + 150
        plt.legend(scatterpoints=1, frameon=False,
                labelspacing=1, loc='lower left')

        x,y = m(115.857048,-31.953512)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(111.24316514,-31.98198667, "Perth" )

        x,y = m(130.82958978,-12.47305101)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(126.14062607,-11.69527273, "Darwin" )

        x,y = m(144.946457,-37.840935)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(142.41796821,-39.63953756, "Melbourne" )

        x,y = m(151.209900,-33.865143)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(151.84863254,-33.60730141, "Sydney" )

        x,y = m(153.021072,-27.470125)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(153.86132866,-27.19210716, "Brisbane" )

        x,y = m(149.128998,-35.282001)
        plt.plot(x,y,'ok', markersize=10, marker='*')
        plt.text(150.73242188,-35.51792029, "Canberra" )

        x,y = m(118.95117134,-25.73657274)
        plt.text(x,y,"Western\n Australia",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(131.23828232,-19.64258753)
        plt.text(x,y,"Northern\n Territory",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')  

        x,y = m(141.328125,-21.66559708)
        plt.text(x,y,"Queensland",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(131.60742134,-29.25956498)
        plt.text(x,y,"South\n Australia",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(142.55859375,-32.5171737)
        plt.text(x,y,"New South\n Wales",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(142.68164277,-37.03413685)
        plt.text(x,y,"Victoria",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')
                
        plt.title('Fire intensity\n on '+ str(nr) + ' august 2019', fontsize= 20, color = 'black')
        plt.savefig('august'+str(nr)+'.png')
        nr = nr + 1

# %%
nr = 1
for i in mounth_9:
    if(i > 0):
        new_table = table.head(i)
        table = table.tail(len(table)-i)
        lat = new_table['latitude'].values
        lon = new_table['longitude'].values
        temp = new_table['fire_temperature'].values
        date = new_table['acq_date'].values
        fig = plt.figure(figsize=(12,5))
        m = Basemap(
                    llcrnrlon=103.784763, llcrnrlat=-44.590467,
                    urcrnrlon=164.90369, urcrnrlat=-6.105602) 
        m.shadedrelief()
        m.drawcoastlines(color='black')
        m.drawcountries(color='black')
        m.drawstates(color='black')
        m.drawrivers(color='blue')

        m.scatter( x = lon, y = lat,
            c=(temp),
                cmap='Reds_r', alpha=1, marker = 'o')
        plt.colorbar(label=r'${\rm Fire...intensity}$')
        plt.clim(25, 325)

        value_of_brightness = 25
        for i in ['darkred','coral','mistyrose']:
            plt.scatter([],[], c = i , alpha=1,
                        s = 150, label = 'Intensity: '+str(value_of_brightness) +' C')
            value_of_brightness = value_of_brightness +150
        plt.legend(scatterpoints=1, frameon=False,
                labelspacing=1, loc='lower left')

        x,y = m(115.857048,-31.953512)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(111.24316514,-31.98198667, "Perth" )

        x,y = m(130.82958978,-12.47305101)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(126.14062607,-11.69527273, "Darwin" )

        x,y = m(144.946457,-37.840935)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(142.41796821,-39.63953756, "Melbourne" )

        x,y = m(151.209900,-33.865143)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(151.84863254,-33.60730141, "Sydney" )

        x,y = m(153.021072,-27.470125)
        plt.plot(x,y,'ok', markersize=5, marker='o')
        plt.text(153.86132866,-27.19210716, "Brisbane" )

        x,y = m(149.128998,-35.282001)
        plt.plot(x,y,'ok', markersize=10, marker='*')
        plt.text(150.73242188,-35.51792029, "Canberra" )

        x,y = m(118.95117134,-25.73657274)
        plt.text(x,y,"Western\n Australia",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(131.23828232,-19.64258753)
        plt.text(x,y,"Northern\n Territory",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')  

        x,y = m(141.328125,-21.66559708)
        plt.text(x,y,"Queensland",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(131.60742134,-29.25956498)
        plt.text(x,y,"South\n Australia",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(142.55859375,-32.5171737)
        plt.text(x,y,"New South\n Wales",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')

        x,y = m(142.68164277,-37.03413685)
        plt.text(x,y,"Victoria",c = "black",
                fontstyle='italic',fontsize="small", va = 'baseline')
                
        plt.title('Fire intensity\n on '+ str(nr) + ' september 2019', fontsize= 20, color = 'black')
        plt.savefig('september'+str(nr)+'.png')
        nr = nr + 1



# %%
table

# %%
frp = table['frp'].head(304).values
lat = table['latitude'].head(304).values
lon = table['longitude'].head(304).values
data = table['acq_date'].head(304).values
# %%
#print("Frp = Fire Radiative Power")
frp.max()
frp.min()
# %%
figure = plt.figure(figsize=(12,5))
m1 = Basemap(
            llcrnrlon=103.784763, llcrnrlat=-44.590467,
            urcrnrlon=164.90369, urcrnrlat=-6.105602) 
m1.shadedrelief()
m1.drawcoastlines(color='black')
m1.drawcountries(color='black')
m1.drawstates(color='black')
m1.drawrivers(color='blue')

m1.scatter( x = lon, y = lat,  c=(frp), cmap='YlGnBu', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire Radiative Power}$')
plt.clim(0, 100)

"""value_of_brightness = 300        
for i in ['mistyrose','coral','darkred']:
        plt.scatter([],[], c = i , alpha=1,
                        s = 150, label = 'brightness: '+str(value_of_brightness))
            value_of_brightness = value_of_brightness +10
        plt.legend(scatterpoints=1, frameon=False,
                labelspacing=1, loc='lower left')"""


x,y = m1(115.857048,-31.953512)
plt.plot(x,y,'ok', markersize=5, marker='o')
plt.text(111.24316514,-31.98198667, "Perth" )

x,y = m1(130.82958978,-12.47305101)
plt.plot(x,y,'ok', markersize=5, marker='o')
plt.text(126.14062607,-11.69527273, "Darwin" )

x,y = m1(144.946457,-37.840935)
plt.plot(x,y,'ok', markersize=5, marker='o')
plt.text(142.41796821,-39.63953756, "Melbourne" )

x,y = m1(151.209900,-33.865143)
plt.plot(x,y,'ok', markersize=5, marker='o')
plt.text(151.84863254,-33.60730141, "Sydney" )

x,y = m1(153.021072,-27.470125)
plt.plot(x,y,'ok', markersize=5, marker='o')
plt.text(153.86132866,-27.19210716, "Brisbane" )

x,y = m1(149.128998,-35.282001)
plt.plot(x,y,'ok', markersize=10, marker='*')
plt.text(150.73242188,-35.51792029, "Canberra" )

x,y = m1(118.95117134,-25.73657274)
plt.text(x,y,"Western\n Australia",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m1(131.23828232,-19.64258753)
plt.text(x,y,"Northern\n Territory",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')  

x,y = m1(141.328125,-21.66559708)
plt.text(x,y,"Queensland",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m1(131.60742134,-29.25956498)
plt.text(x,y,"South\n Australia",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m1(142.55859375,-32.5171737)
plt.text(x,y,"New South\n Wales",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')

x,y = m1(142.68164277,-37.03413685)
plt.text(x,y,"Victoria",c = "black",
        fontstyle='italic',fontsize="small", va = 'baseline')
                

# %%
df = pd.read_csv("CleanedDataV4.csv")

# %%

        
"""WESTERN AUSTRALIA"""

figure = plt.figure(figsize=(12,5))
wa = Basemap(llcrnrlon=109.86328125, llcrnrlat=-36.23009502,
            urcrnrlon=130.51757813, urcrnrlat=-12.74322911)
lat = table['latitude'].values
lon = table['longitude'].values
temp = table['fire_temperature'].values
#area = table['track'].values
date = table['acq_date'].values

wa.shadedrelief()
wa.drawcoastlines(color='black',linewidth=2)
wa.drawcountries(color='black')
wa.drawstates(color='black',linewidth=2)
wa.drawrivers(color='blue')  

wa.scatter( x = lon, y = lat,
    c=(temp),
          cmap='Reds_r', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire...intensity}$')
plt.clim(25, 325)

x,y = wa(118.95117134,-25.73657274)
plt.text(x,y,"Western\n Australia",c = "black",
        fontstyle='italic',fontsize="large", va = 'baseline')

x,y = wa(115.857048,-31.953512)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(111.24316514,-31.98198667, "Perth" )



# %%


"""NORTHERN TERRITORY"""

figure = plt.figure(figsize=(12,5))
nt = Basemap(llcrnrlon=127.12499678, llcrnrlat=-27.26243891,
            urcrnrlon=139.88671929, urcrnrlat=-10.67788193)

nt.shadedrelief()
nt.drawcoastlines(color='black')
nt.drawcountries(color='black')
nt.drawstates(color='black')
nt.drawrivers(color='blue') 



x,y = nt(131.23828232,-19.64258753)
plt.text(x,y,"Northern\n Territory",c = "black",
        fontstyle='italic',fontsize="large", va = 'baseline')


x,y = nt(130.82958978,-12.47305101)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(131.14062607,-12.69527273, "Darwin" )
# %%

"""QUEENSLAND"""

figure = plt.figure(figsize=(12,5))

ql = Basemap(llcrnrlon=136.97753873, llcrnrlat=-29.81776778,
            urcrnrlon=156.12890705, urcrnrlat=-9.3796961)

ql.shadedrelief()
ql.drawcoastlines(color='black')
ql.drawcountries(color='black')
ql.drawstates(color='black')
ql.drawrivers(color='blue') 

x,y = ql(141.328125,-21.66559708)
plt.text(x,y,"Queensland",c = "black",
        fontstyle='italic',fontsize="large", va = 'baseline')

x,y = ql(153.021072,-27.470125)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(153.86132866,-27.19210716, "Brisbane" )

# %%

table = pd.read_csv("CleanedDataV4.csv")
sa_table = table
sa_table = sa_table.loc[sa_table['longitude'] >129.03222576]
sa_table = sa_table.loc[sa_table['longitude'] <140.9765625]
sa_table = sa_table.loc[sa_table['latitude'] > -38.07922811]
sa_table = sa_table.loc[sa_table['latitude'] < -26.02914407]
"""SOUTH AUSTRALIA """

figure = plt.figure(figsize=(12,5))

sa = Basemap(llcrnrlon=127.66992107, llcrnrlat=-38.71294664,
            urcrnrlon=142.40039036, urcrnrlat=-25.32416168)

lat = sa_table['latitude'].values
lon = sa_table['longitude'].values
temp = sa_table['fire_temperature'].values


sa.shadedrelief()
sa.drawcoastlines(color='black',linewidth=2)
sa.drawcountries(color='black')
sa.drawstates(color='black',linewidth=2)
sa.drawrivers(color='blue')  

sa.scatter( x = lon, y = lat,
    c=(temp),
          cmap='Reds_r', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire...intensity}$')
plt.clim(25, 325)         

x,y = sa(132.60742134,-29.25956498)
plt.text(x,y,"South\n Australia",c = "black",
        fontstyle='italic',fontsize="xx-large", va = 'baseline')

x,y = sa(138.58593643,-34.94358992)
plt.plot(x,y,'ok', marker = 'o', markersize = 5)
plt.text(137.54882813,-36.04635127,'Adelaide')

plt.savefig("SouthAustralia.png")
# %%

sa_table
# %%

"""NEW SOUTH WALES"""
nsw_table = table
nsw_table = nsw_table.loc[nsw_table['longitude'] >140.95898397]
nsw_table = nsw_table.loc[nsw_table['longitude'] <153.59765545]
nsw_table = nsw_table.loc[nsw_table['latitude'] > -38.07922811]
nsw_table = nsw_table.loc[nsw_table['latitude'] < -28.22697004]

figure = plt.figure(figsize=(12,5))

nsw = Basemap(llcrnrlat=-37.49577984, llcrnrlon=140.08007906,
                urcrnrlat=-27.0904292,urcrnrlon=156.31347656)

lat = nsw_table['latitude'].values
lon = nsw_table['longitude'].values
temp = nsw_table['fire_temperature'].values


nsw.shadedrelief()
nsw.drawcoastlines(color='black',linewidth=2)
nsw.drawcountries(color='black')
nsw.drawstates(color='black',linewidth=2)
nsw.drawrivers(color='blue')  

nsw.scatter( x = lon, y = lat,
    c=(temp),
          cmap='Reds_r', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire...intensity}$')
plt.clim(25, 325)          

x,y = nsw(142.55859375,-31.5171737)
plt.text(x,y,"New South\n Wales",c = "black",
        fontstyle='italic',fontsize="xx-large", va = 'baseline')

x,y = nsw(151.209900,-33.865143)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(151.44863254,-33.60730141, "Sydney" )

x,y = nsw(149.128998,-35.282001)
plt.plot(x,y,'ok', markersize=10, marker='*')
plt.text(149.23242188,-35.01792029, "Canberra", fontsize="large")

x,y =(151.750000,-32.916668)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(151.342224,-33.425018)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(143.850006,-37.549999)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	150.893143,-34.425072)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	153.399994,	-28.016666)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	146.816956,	-19.258965)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	149.186813,-21.144337)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

x,y =(	152.350006,		-24.850000)
plt.plot(x,y,'ok',markersize = 7 , marker ='^')

plt.savefig("NewSouthWales.png")
# %%


"""Victoria"""

vc_table = table
vc_table = vc_table.loc[vc_table['longitude'] >139.62304473]
vc_table = vc_table.loc[vc_table['longitude'] <153.59765545]
vc_table = vc_table.loc[vc_table['latitude'] > -44.84029065]
vc_table = vc_table.loc[vc_table['latitude'] < -33.84121631]

figure = plt.figure(figsize=(12,5))

vc = Basemap(llcrnrlat=-44.84029065,llcrnrlon=139.62304473,
                urcrnrlat=-33.84121631, urcrnrlon=153.36914063)

lat = vc_table['latitude'].values
lon = vc_table['longitude'].values
temp = vc_table['fire_temperature'].values

vc.shadedrelief()
vc.drawcoastlines(color='black',linewidth = 2)
vc.drawcountries(color='black')
vc.drawstates(color='black', linewidth = 2)
vc.drawrivers(color='blue')  

vc.scatter( x = lon, y = lat,
    c=(temp),
          cmap='Reds_r', alpha=1, marker = 'o')
plt.colorbar(label=r'${\rm Fire...intensity}$')
plt.clim(25, 325)

x,y = vc(144.68164277,-40.03413685)
plt.text(x,y,"Victoria",c = "black",
        fontstyle='italic',fontsize="xx-large", va = 'baseline')

x,y = vc(144.946457,-37.840935)
plt.plot(x,y,'ok', markersize=7, marker='o')
plt.text(144.41796821,-38.63953756, "Melbourne", fontsize="medium" )

plt.savefig("Victoria.png")