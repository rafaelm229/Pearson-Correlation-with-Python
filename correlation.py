import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")

movies["Rotten Tomatoes"] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace = True, axis=1)
correlations = movies.corr(method="pearson")

#correlation Between all the features
print(correlations)

#Correlation Betweek a particular column "Year"
print(correlations["Year"])

sns.heatmap(correlations)
plt.show()

