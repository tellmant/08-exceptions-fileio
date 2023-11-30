import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('college.csv')
college = data.groupby('Private')
college[['Apps', 'Accept', 'Enroll']].mean().plot(kind='bar', title=r'Student Applications',
                                                  tick_label=['Private Schools', 'Public Schools'])
plt.ylabel('Amount of Applications')
plt.xlabel('Private or Public School')
plt.legend(['Applications', 'Accepted Students', 'Enrolled Students'])
plt.grid(True)

data.plot(kind='box', vert=False, title='Distributions of graduation rates.', y=['Grad.Rate'])

data.plot(kind='hexbin', x='S.F.Ratio', y='Grad.Rate', gridsize=20,
          title='Correlation between Graduation Rate and S.F. Ratio')
plt.xlabel('S.F. Ratio')

plt.tight_layout()
plt.show()
