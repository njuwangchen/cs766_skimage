import numpy as np

'''
s = np.linspace(0, 5, 5)
print s
x = 100*np.cos(s)
print x
y = 100*np.sin(s)
print y
init = np.array([x, y]).T
print init
print init[:, 0]
print init[:, 1]
'''

left_most = 10
right_most = 30
up_most = 20
down_most = 40

num_of_points = 10

up_line_x = np.linspace(left_most, right_most, num_of_points)
up_line_y = np.ones(num_of_points)*up_most
print up_line_x
print up_line_y
right_line_x = np.ones(num_of_points)*right_most
right_line_y = np.linspace(up_most, down_most, num_of_points)
print right_line_x
print right_line_y
down_line_x = np.linspace(right_most, left_most, num_of_points)
down_line_y = np.ones(num_of_points)*down_most
print down_line_x
print down_line_y
left_line_x = np.ones(num_of_points)*left_most
left_line_y = np.linspace(down_most, up_most, num_of_points)
print left_line_x
print left_line_y

X = np.concatenate((up_line_x, right_line_x, down_line_x, left_line_x), axis=0)
print X
Y = np.concatenate((up_line_y, right_line_y, down_line_y, left_line_y), axis=0)
print Y

init = np.array([X, Y]).T
print init
