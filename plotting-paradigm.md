# Plotting Paradigm

This is a proposal to introduce a different paradigm for the way specialised control analyses and plots are created in Python-Control.

It is based on the way plotting is done in [Pandas](https://pandas.pydata.org/docs/).

For example:

```python
s = pandas.Series(my_data, index=my_index, name="my series")  # instantiate object
print(s.dtype)  # get an attribute
s.plot(style="o-")  # make a plot
plt.show()
avg = s.mean()  # do something else
```

## Functions this proposal could affect

- `root_locus`
- `pzmap`
- `bode_plot`
- `nyquist_plot`
- `gangof4_plot`
- `nichols_plot`
- `sisotool`?


## Rationale

The current paradigm for these plot functions is based on the way they are done in MATLAB using the functions `pzmap`, `bode`, `nyquist`, etc. These functions can produce a plot and/or the data itself, depending on how you use them. This style is typical of a functional programming language that does not have support for object-oriented programming.

*Problem*:
- Doing the calculations and making the plot are two separate tasks.  Doing both with one function is arguably 'overloading' it. This leads to a larger set of arguments and return values and somewhat restricts the amount of variables that can be returned or accessed after the function is called.

*Solution*:
- Split the process into two steps:
    - Step 1, do the calculations and generate the data
    - Step 2, make the plot
- Use a Python object (class) to access the data and plot method.

The benefits of this approach are:
- The inputs, outputs and arguments of each step are separated
- A greater variety of variables and attributes can be accessed
- Easier to get a handle to the plot axis for customizing plots
- Easily extensible — more functionality could be added as methods
- It is familiar to many Python users (e.g. data scientists using Pandas).

To illustrate how this might work, I have outlined some examples below.

### Example 1 – Root locus plot

Current method:

```python
from control import rlocus
rlocus(my_sys, **kwargs)
plt.show()
```

Proposed method:

```python
from control import RootLocus
rl = RootLocus(my_sys, **kwargs)  # calculation arguments go here
rl.plot(**kwargs)  # plotting arguments here
plt.show()
```

or:

```python
from control import RootLocus
RootLocus(my_sys).plot(**kwargs)
plt.show()
```

### Calculate the root locus without making the plot

Current method:

```python
rlist, klist = rlocus(my_sys, Plot=False)
```

Proposed method:

```python
rl = RootLocus(my_sys)  # does not make a plot by default
rl.rlist, rl.klist  # access the data
```

### Calculate and plot the root locus

Current method:

```python
rlist, klist = rlocus(my_sys)
plt.show()
```

Proposed method:

```python
rl = RootLocus(my_sys)
rl.rlist, rl.klist  # access the data
rl.plot()
plt.show()
```

### Customizing the root locus plot

Current method:

```python
rlocus(my_sys)
ax = plt.gca()
#ax.lines[??].set_linewidth(2)  # not easy to do
ax.annotate("label", (-1, 0))
plt.show()
```

Proposed method:

```python
rl = RootLocus(my_sys)
ax = rl.plot(linewidth=2)  # plotting arguments here
ax.annotate("label", (-1, 0))
plt.show()
```

### Adding root locus to a custom plot

Current method:

```python
fig, axes = plt.subplots(2, 1)
ax = axes[0]
rlocus(sys1, ax=axes[0])
ax.set_title("System 1")
ax = axes[1]
rlocus(sys2, ax=axes[1])
ax.set_title("System 2")
plt.tight_layout()
plt.show()
```

Proposed method:

```python
rl1 = RootLocus(sys1)
rl2 = RootLocus(sys2)
fig, axes = plt.subplots(2, 1)
ax = axes[0]
rl1.plot(ax=ax)
ax.set_title("System 1")
ax = axes[1]
rl2.plot(ax=ax)
ax.set_title("System 2")
plt.show()
```

## Other comments

Introducing this would not require the replacement of the MATLAB-like functions `rlocus`, `nyquist`, `pzmap`, etc. although keeping the current `root_locus`, `bode_plot`, and `nyquist_plot` functions seems a bit redundant.

Functions such as `freqresp` would be unaffected and would probably be called by `FreqResp` to do the calculations.
