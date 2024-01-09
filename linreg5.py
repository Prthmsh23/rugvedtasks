import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rugvedlin.csv')


def gradient_descent(m, b, points, L):
  m_gradient = 1
  b_gradient = 1

  n = len(points)
  for i in range(n):
      x = points.iloc[i].carat
      y = points.iloc[i].price

      m_gradient += -(2/n)*x*(y - (m*x + b))
      b_gradient += -(2/n)*(y - (m*x + b))

  m = m - L*m_gradient
  b = b - L*b_gradient

  return m, b

m = 0
b = 0
L = 0.0001
iterations = 500
for i in range(iterations):
  m, b = gradient_descent(m, b, data, L)
  print(f"Iteration {i+1}: m={m}, b={b}") # Debugging print statement

print("Final values:", m, b)

plt.scatter(data.price, data.carat, color="#000000")
line_x= [x for x in range(1, len(data.price)+1)]
line_y = [m*x+b for x in range(1, len(data.price)+1)]
print("Line y-values:", line_y) # Debugging print statement
print("Line x-values:", line_x) # Debugging print statement

plt.plot(line_x , line_y, color="red")
plt.show()
