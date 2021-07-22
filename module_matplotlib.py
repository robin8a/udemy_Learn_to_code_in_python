import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1000, 2000, 2500, 3500]
legends = ["January", "February", "March", "April"]

# plt.plot(x,y)
# plt.xticks(x,legends)

plt.bar(x,y)
plt.ylabel("Sales in US")
plt.title("Montly Sales")
plt.show()


