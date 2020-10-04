#Biased coin probablility of occurncae of a head is 0.2 and that of a trial is 0.8
 # case 1:- Tossing of such a coin 5 time. what is the probality of getting 3 head
 #case 2: - Find the variance and standdard deviation

# The no. of success(x) = 3, Number of Trials(n) = 5 , probability of success(p) = 0.2
from math import comb
import matplotlib.pyplot as plt
import seaborn as sns

p = 0.2
x = 3
n = 5

fact_n = 1
fact_x = 1
fact_num_minus_x = n - x
for counter in range (1,n+1):
   fact_n = fact_n * counter

for counter in range (1,x+1):
    fact_x = fact_x * counter

for counter in range (1,fact_num_minus_x):
    fact_num_minus_x = fact_num_minus_x * counter

print("fact_n=", fact_n)
print("fact_x=", fact_x)
print("fact_num_minus_x=", fact_num_minus_x)

result = fact_n/(fact_x * fact_num_minus_x)
print("result=", result)
final_result = result * (p)**x * (1-p)**(n-x)
print("Pro_of_heads=", final_result)
n1 = [0,1,2,3]
#proba_group = [0.2, 0.3, 0.3, 0.2]
range = (0,3)
bins = 4
plt.hist(n1, bins ,  rwidth = 0.8 , color= 'green', histtype= 'bar')
plt.xlabel("Number of trial", fontsize=12)


plt.ylabel("probability of frequency", fontsize=12)
plt.show()

'''
P(X=x) = Pro_of_heads
Pro_of_heads = comb(5,3) * (0.2)**3 * (0.8)**2
print("Pro_of_heads=", Pro_of_heads)'''

