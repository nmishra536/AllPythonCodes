"""*******************************************
	python code for project 1 in
	CSE 107 in 2022 winter, UC Santa Cruz,
			for Prof. Chen Qian.
**********************************************
	Student name: Navya Mishra
	UCSC email: nmishra3@ucsc.edu
"""
import numpy as np
import matplotlib.pyplot as plt
import simplerandom.iterators as sri

"""
Make a scatter plot of the distribution for these three RNG.
You'll generate num = 10,000 random number in range [0, num).
Make a single scatter plot using matplotlib with the x-axis being 
index of number and the y-axis being the number.

Hint(s):
    1. You'll call plt.scatter(...) for each rng. 
    Make sure your calls are of the form:
    'plt.scatter(x_vals, y_vals, c = 'b', s=2)' where c = 'b' indicates
    blue and s = 2 is to set the size of points. You may want to use
    "r", "g", and "b", a different color for each rng.
    2. Use plt.savefig(...).
"""


def distribution_random():
    x_vals = []
    y_vals = []
    np.random.seed(0)
    num = 10000
    for i in range(num):
        y_vals.append(np.random.randint(num))
        x_vals.append(i)
    plt.scatter(x_vals, y_vals, c="b", s=2)
    plt.xlabel("index")
    plt.ylabel("random number")
    plt.title("distribution_random")
    plt.savefig("distribution_random")
    plt.clf()


def distribution_KISS():
    x_vals = []
    y_vals = []
    rng_kiss = sri.KISS(123958, 34987243, 3495825239, 2398172431)
    num = 10000
    for i in range(num):
        y_vals.append(next(rng_kiss))
        x_vals.append(i)
    plt.scatter(x_vals, y_vals, c="g", s=2)
    plt.xlabel("index")
    plt.ylabel("random number")
    plt.title("distribution_KISS")
    plt.savefig("distribution_KISS")
    plt.clf()


def distribution_SHR3():
    x_vals = []
    y_vals = []
    rng_shr3 = sri.SHR3(3360276411)
    num = 10000
    for i in range(num):
        y_vals.append(next(rng_shr3))
        x_vals.append(i)
    plt.scatter(x_vals, y_vals, c="r", s=2)
    plt.xlabel("index")
    plt.ylabel("random number")
    plt.title("distribution_SHR3")
    plt.savefig("distribution_SHR3")
    plt.clf()


def pingpong(n: int = 21, p: float = 0.3, ntrials: int = 5000, seed: int = 0):
    win = 0
    you = 0
    friend = 0
    np.random.seed(seed)
    def sim_one_game():
        #     """
        #     This is a nested function only accessible by parent sim_prob,
        #     which we're in now. You may want to implement this function!
        #     """
        nonlocal you
        nonlocal friend
        number = np.random.random()
        if you <= n and friend <= n:
            if number < p:
                you += 1 #you isn't updating
                sim_one_game()
            else:
                friend += 1 # friend isn't updating either
                sim_one_game()
        if (you - friend) >= 2:
            return True
        else:
            if (friend - you) >= 2:
                return False
            elif abs( you - friend) < 2:
                if number < p:
                    you += 1  # you isn't updating
                    sim_one_game()
                else:
                    friend += 1  # friend isn't updating either
                    sim_one_game() #thank god this thing works now GREAAAAAT




    for i in range(ntrials):
        you = 0
        friend = 0
        if sim_one_game() ==  True:
            win += 1
    return win / ntrials
    # TODO: Your code here (10-20 lines)


def plot_output():
    plt.clf()
    p = 0.0
    x_vals = []
    y_vals = []
    while p <= 1.0:
        x_vals.append(p)
        p += 0.04
    for g in x_vals:
        y_vals.append(pingpong(3, g, 5000, 5))
    plt.plot(x_vals, y_vals, "-b", label="n=3")
    y_vals.clear()
    for g in x_vals:
        y_vals.append(pingpong(11, g, 5000, 5))
    plt.plot(x_vals, y_vals, "-r", label="n=11")
    y_vals.clear()
    for g in x_vals:
        y_vals.append(pingpong(21, g, 5000, 5))
    plt.plot(x_vals, y_vals, "-g", label="n=21")

    plt.legend(loc="upper left")
    plt.xlabel("P(win point)")
    plt.ylabel("P(win game)")
    plt.title("Relating P(win point) to P(win game)")
    plt.savefig("part_B")

    """
    Make a single plot using matplotlib with the x-axis being p
    for different values of p in {0, 0.04, 0.08,...,0.96, 1.0}
    and the y-axis being the probability of winning the overall game
    (use your previous function). Plot 3 "curves" in different colors,
    one for each n in {3,11,21}.
    You can code up your solution here. Make sure to label your axes
    and title your plot appropriately, as well as include a
    legend!
    Hint(s):
    1. You'll call plt.plot(...) 3 times total, one for each
    n. Make sure your calls are of the form:
    'plt.plot(x_vals, y_vals, "-b", label="n=11")' where "-b" indicates
    blue and "n=11" is to say these set of points is for n=11. You may
    want to use "-r", "-g", and "-b", a different color for each n.
    2. Use plt.legend(loc="upper left").
    3. Use plt.savefig(...).
    :return: Nothing. Just save the plot you made!
    """


# TODO: Your code here (10-20 lines)


if __name__ == '__main__':
    distribution_random()
    distribution_KISS()
    distribution_SHR3()
    plot_output()
    # You can test out things here. Feel free to write anything below
