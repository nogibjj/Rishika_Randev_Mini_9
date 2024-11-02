"""Main function making use of the math module."""

from lib import load, summarise, scatter, anx_boxplot, dep_boxplot

if __name__ == "__main__":
    pivoted, regions = load()
    print(summarise(pivoted))
    scatter(pivoted)
    anx_boxplot(pivoted, regions)
    dep_boxplot(pivoted, regions)
    
    
    
    
