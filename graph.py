import matplotlib.pyplot as plt
x = ['Math','English','Hindhi']
y = [56,78,90]
plt.bar(x,y,width=0.1,color=['green','red','orange'])
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks Graph')
plt.show()