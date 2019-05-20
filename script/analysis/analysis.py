import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../outputs/results.csv')

fig = plt.figure()

ax1 = fig.add_subplot(5, 1, 1)
ax1.set_title('amount')
ax1.plot(df['amount'], marker='o')

ax2 = fig.add_subplot(5, 1, 2)
ax2.set_title('profit')
ax2.plot(df['profit'], marker='o')

ax3 = fig.add_subplot(5, 1, 3)
ax3.set_title('correct')
ax3.plot(df['correct'], marker='o')

ax4 = fig.add_subplot(5, 1, 4)
ax4.set_title('average')
ax4.plot(df['average'], marker='o')

ax5 = fig.add_subplot(5, 1, 5)
ax5.set_title('mis')
ax5.plot(df['mis'],  marker='o')

plt.show()
