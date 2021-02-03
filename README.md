# The prime decomposition

You hopefully worked out that there are numbers missing from the set of products you extract whenever `N` is greater than 2.  For example, if `N=3` the set of all possible products includes the numbers 0, 1, 2 and 4 but the number 3 is missing.  The numbers that are missing are the __prime numbers__.  Furthermore, as you no doubt know, there are an infinite number of primes.  In answer to our question: an infinite number of different symbols would be required for any number system that was based purely on multiplication, which is obviously not ideal.

Representations of natural numbers as a product of primes appear in many of the mathematical proofs you will encounter in MTH1002.  Even though this clunky representation is not going to replace the Arabic system of number any time soon it is thus still worth considering how it works as we will do in this exercise.

The code in `main.py` contains a function called `primeDecomposition` that takes an integer `N` as input.  The function then returns the largest divisor of that number.  If you run it you will see how this works in practice.  To write this code I have had to use a feature of python that you have not seen before - a while loop.  This command:

````
while i*i <= N
````

tells python to continue to repeat the indented code within the loop until the condition is no longer satisfied.  In other words, python stops repeating the code in the loop once `i*i` is greater than `N`.  It is necessary to use a while loop here because, if you look at the code in the loop, you will notice that changes are made both to the value of `i` and the value of `N`.

In order to understand the code remember the basic idea of the prime decomposition system of number is to represent a natural number N as follows:

![](https://render.githubusercontent.com/render/math?math=N=p_1p_2p_3\dots\p_m)

where ![](https://render.githubusercontent.com/render/math?math=p_1), ![](https://render.githubusercontent.com/render/math?math=p_2) etc are all prime numbers and ![](https://render.githubusercontent.com/render/math?math=p_1<p_2<p_3<\dots).  The algorithm in the code on the left tests whether the natural numbers are factors of `N` one by one.  If a factor is found the following calculation is performed:

![](https://render.githubusercontent.com/render/math?math=\frac{N}{p_1}=p_2p_3\dots\p_m)

and the one-by-one search for factors continues to find ![](https://render.githubusercontent.com/render/math?math=p_2), ![](https://render.githubusercontent.com/render/math?math=p_3) and so on.  Each time one of these factors is found the left-hand side of the above equation is divided by this number.  Once the code has finished running the right-hand side is equal to ![](https://render.githubusercontent.com/render/math?math=p_m) - the largest prime divisor.

__To complete this task I would like you to demonstrate that you understand the code in `main.py` by modifying the function `primeDecomposition` so that it returns a python set containing all the prime factors of `N` rather than the largest prime divisor only.__



