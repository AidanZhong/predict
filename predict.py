from GradientDescent import train
from utils.CsvReader import *

print('start')
read_csv_to_fill_data()
train()
print('output is h(x,y)=' + '{:.4f}'.format(THETA[0]) +
      '+' + '{:.4f}'.format(THETA[1]) + 'x' +
      '+' + '{:.4f}'.format(THETA[2]) + 'x^2' +
      '+' + '{:.4f}'.format(THETA[3]) + 'y' +
      '+' + '{:.4f}'.format(THETA[4]) + 'y^2'
      )
