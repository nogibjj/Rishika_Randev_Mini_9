from lib import load, summarise, scatter, anx_boxplot, dep_boxplot
import numpy as np

def test_load_summarise():
    pivoted, regions = load()
    means = summarise(pivoted)
    assert np.isclose(means['Symptoms of Anxiety Disorder'], 28.996078)
    assert np.isclose(means['Symptoms of Depressive Disorder'], 23.468627)
    
def test_plots():
    pivoted, regions = load()
    assert scatter(pivoted) is not None
    assert anx_boxplot(pivoted, regions) is not None
    assert dep_boxplot(pivoted, regions) is not None
