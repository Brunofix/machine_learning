import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#prvo pitanje: Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.
mtcars = pd.read_csv('mtcars.csv')

mpg_4_cilindra=(mtcars[mtcars["cyl"] == 4]['mpg'].mean())
mpg_6_cilindara=(mtcars[mtcars["cyl"]==6]["mpg"].mean())
mpg_8_cilindara=(mtcars[mtcars["cyl"]==8]["mpg"].mean())

plt.figure()
sns.barplot(x=['4 cyl', '6 cyl', '8 cyl'], y=[mpg_4_cilindra, mpg_6_cilindara, mpg_8_cilindara])
plt.ylabel('Mean MPG')
plt.xlabel('(Higher is better)')
plt.title("MPG compared to number of cylinders")

