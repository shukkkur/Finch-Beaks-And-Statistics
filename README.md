<h2 align='center'>Darwinian Evolution in Action <br>Finch Beaks and Statistics</h2>
<p align='center'>
  <img src='datasets/finches.gif'>
</p>

<p><a href='https://github.com/shukkkur/Finch-Beaks-And-Statistics/tree/main/datasets' target="_blank">Data</a> from Peter and Rosemary Grant research of Darwin's finches on Galápagos island of Daphne Major. 
</p>

<br>

<h3>1. EDA of beak depths of Darwin's finches</h3>
<p>First let's see how the beak depth (the distance, top to bottom, of a closed beak) of the finch species <i>Geospiza scandens</i> has changed over time. </p>

```python
_ = sns.swarmplot(x='year', y='beak_depth', data=df)
```
<img src='datasets/swarm.jpg'>

<p>It's hard to see if there is a clear difference between the <b>1975</b> and <b>2012</b> data set. But, it appears as the mean of the 2012 dataset might be slightly higher, and it might have a bigger variance.</p>


<h4>ECDFs of beak depths</h4>

```python
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012,y_2012, marker='.', linestyle='none')
```

<img src='datasets/ecdfs.jpg'>
<p>The differences are much clearer in the ECDF. The mean is larger in the 2012 data, and the variance does appear larger as well.</p>
