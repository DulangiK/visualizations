plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.rc('xtick', labelsize=14) 
plt.rc('ytick', labelsize=14) 

plotdata = pd.DataFrame(
    {"disabled": [70, 900]}, 
    index=['disabled', 'normal'])
# Plot a bar chart
plotdata.plot(kind="bar", color='tan', width=0.4)

plt.xticks(rotation=0, horizontalalignment="center")
plt.title("The disbaled population distribution at workplace",fontsize=14)
plt.xlabel("disabled or not",fontsize=14)
plt.ylabel("No.of people",fontsize=14)


#plt.savefig('disabled.png', dpi=1200)

plt.savefig('disabled.eps',format='eps')
