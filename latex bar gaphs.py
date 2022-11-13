plotdata = pd.DataFrame(
    {"No. of students": [40, 30, 10, 4]}, 
    index=['A', 'B', 'C','D'])
# Plot a bar chart
plotdata.plot(kind="bar", color='gray')

plt.xticks(rotation=0, horizontalalignment="center")
#plt.title("S")
plt.xlabel("student marks")
plt.ylabel("No.of students")

#plt.show()
plt.savefig('fig1.png', dpi=1200)
