import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print ("This game will help you faster. You will have to type the word 'programming' as fast you can for five times")

input ("Press enter to continue...")

while len (times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if (word.lower() != "programming"):
        mistakes += 1

print ("You made ", mistakes, " mistakes")
print ("Let's see your evolution")

t.sleep(3)

x = [1,2,3,4,5]
y = times
legends = ["1", "2", "3", "4","5"]
plt.plot(x,y)
plt.xticks(x,legends)
plt.xlabel("Attempts")
plt.ylabel("Time in seconds")
plt.show()
