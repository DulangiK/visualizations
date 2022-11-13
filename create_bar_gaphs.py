plotdata = pd.DataFrame(
    {"# students": [35, 60, 12, 5]}, 
    index=['A', 'B', 'C','D'])
# Plot a bar chart
plotdata.plot(kind="bar", color='gray')

plt.xticks(rotation=8, horizontalalignment="center")
plt.title("Studets mark distribution for English subject")
plt.xlabel("student class")
plt.ylabel("No.of students")
