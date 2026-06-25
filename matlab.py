import pandas as pd
import matplotlib.pyplot as plt

df =df = pd.read_csv(r"C:\Users\HP USER\Downloads\company_sales_data.csv")
profitlist = df["total_profit"].tolist()
monthslist = df["month_number"].tolist()
# Draw the line
plt.plot(monthslist, profitlist,
         label='Monthly Profit',  # text shown in legend
         color='red',             # line color
         marker='o',              # circle at each data point
         markerfacecolor='black', # fill the circle black
         linestyle='--',          # dashed line
         linewidth=3)             # thickness

plt.xlabel('Month Number')        # x-axis label
plt.ylabel('Profit in USD')       # y-axis label
plt.title('Company Sales Data')   # chart title
plt.legend(loc='lower right')     # show the legend

plt.xticks(monthslist)             # force x-axis to show each month
plt.yticks([10000,20000,30000,40000,50000,60000])  # custom y ticks

plt.show()   

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
# Top chart — Bathing Soap
bathingsoap = df['bathingsoap'].tolist()
ax1.plot(monthslist, bathingsoap, color='blue', marker='s')
ax1.set_title('Bathing Soap Sales')
ax1.set_ylabel('Units Sold')

# Bottom chart — Facewash
facewash = df['facewash'].tolist()
ax2.plot(monthslist, facewash, color='green', marker='^')
ax2.set_title('Facewash Sales')
ax2.set_xlabel('Month')
ax2.set_ylabel('Units Sold')

plt.tight_layout()   # auto-fix spacing between subplots
plt.show()