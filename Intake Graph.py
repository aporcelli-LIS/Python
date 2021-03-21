import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['Return', 'Surrender', 'Stray', 'Confiscate', 'Foster']
Dogs = [2, 8, 29, 3, 2]
Cats = [0, 3, 2, 1, 0]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Dogs, width, label='Dogs', color='green')
rects2 = ax.bar(x + width/2, Cats, width, label='Cats', color='purple')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Intakes')
ax.set_title('Intakes March 5th - 19th 2021', color='red')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()