# <img src="https://github.com/phuongtrieu97coder/Readme_Content_Structure/assets/82598726/174e2883-2d0b-4d01-8992-32f709b72373" alt="Python" width="100px" height="100px">


<img src="https://github.com/phuongtrieu97coder/Python_projects/assets/82598726/19e383e6-169d-428b-8879-766b22b50211" alt="python_poster" width="400px" height="300px"> <a type="button" title="Codecademy_Learn_Python3_Course_button" href="https://www.codecademy.com/courses/learn-python-3/projects/python-carlys-clippers" target="_blank" data-CodecademyLearnPython3CourseButt="CodecademyLearnPython3CourseButt_data"><img src="https://user-images.githubusercontent.com/82598726/175697552-f960b057-9e97-4c3e-a3e2-f2b5f7876de9.png" alt="Codecademy_Learn_Python3_Course_button" width="400px" height="300px"></a>


<br><br>


# Carly's Clippers

# 1. Introduction:
> You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.<br><br>
You have been provided with three lists:<br><br>
> - <b>hairstyles</b>: the names of the cuts offered at Carly’s Clippers.<br><br>
> - <b>prices</b>: the price of each hairstyle in the hairstyles list.<br><br>
> - <b>last_week</b>: the number of purchases for each hairstyle type in the last week.
Each index in <b>hairstyles</b> corresponds to an associated index in <b>prices</b> and <b>last_week</b>.<br><br>
For example, The hairstyle <b>"bouffant"</b> has an associated price of <b>30</b> from the <b>prices</b> list, and was purchased <b>2</b> times in the last week as shown in the <b>last_week</b> list. Each of these elements are in the first index of their respective lists.


# 2. Output:
Average Haircut Price: 31.875

[25, 20, 35, 15, 15, 30, 45, 30]

Total Revenue: 1085

['bouffant', 'pixie', 'crew', 'bowl']

# 3. Prompts:
> 1. Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.<br><br>
First, let’s sum up all the prices of haircuts. Create a variable <b>total_price</b>, and set it to <b>0</b>.
```python
total_price = 0
```

<br>

> 2. Loop through the <b>prices</b> list and add each price to the variable <b>total_price</b>.
```python
for num in prices:
  total_price+=num
```

<br>

> 3. After your loop, create a variable called <b>average_price</b> that is the <b>total_price</b> divided by the number of prices.<br><br>
You can get the number of prices by using the <b>len()</b> function.
```python
average_price = total_price / len(prices)
```

<br>

> 4. Print the value of average_price so the output looks like:<br><br>
Average Haircut Price: <average_price>
```python
print("Average Haircut Price:",average_price)
```

<br>

> 5. That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.<br><br>
Use a list comprehension to make a list called <b>new_prices</b>, which has each element in <b>prices</b> minus <b>5</b>.
```python
new_prices = [num-5 for num in prices]
```

<br>

> 6. Print <b>new_prices</b>.

<br>

> 7. Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.<br><br>
Create a variable called <b>total_revenue</b> and set it to <b>0</b>.
```python
total_revenue = 0
```
<br>

> 8. Use a for loop to create a variable <b>i</b> that goes from <b>0</b> to <b>len(hairstyles)</b><br><br>
Hint: You can use <b>range()</b> to do this!
```python
for i range(len(hairstyles)):
```

<br>

> 9. Add the product of <b>prices[i]</b> (the price of the haircut at position <b>i</b>) and <b>last_week[i]</b> (the number of people who got the haircut at position <b>i</b>) to <b>total_revenue</b> at each step.
```python
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
```

<br>

> 10. After your loop, print the value of total_revenue, so the output looks like:<br><br>
Total Revenue: <total_revenue>
```python
print("Total Revenue:",total_revenue)
```

<br>

> 11. Find the average daily revenue by dividing <b>total_revenue</b> by 7. Call this number <b>average_daily_revenue</b> and print it out.
```python
average_daily_revenue = total_revenue/7
```

<br>

> 12. Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under <b>30</b> dollars.<br><br>
Use a list comprehension to create a list called <b>cuts_under_30</b> that has the entry <b>hairstyles[i]</b> for each i for which <b>new_prices[i]</b> is less than <b>30</b>.<br><br>
You can use range() in your list comprehension to make i go from <b>0</b> to <b>len(new_prices) - 1</b>.
```python
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
```

<br>

> 13. Print <b>cuts_under_30</b>.