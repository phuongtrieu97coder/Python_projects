# <img src="https://github.com/phuongtrieu97coder/Readme_Content_Structure/assets/82598726/174e2883-2d0b-4d01-8992-32f709b72373" alt="Python" width="100px" height="100px">


<img src="https://github.com/phuongtrieu97coder/Python_projects/assets/82598726/19e383e6-169d-428b-8879-766b22b50211" alt="python_poster" width="400px" height="300px"> <a type="button" title="Codecademy_Learn_Python3_Course_button" href="https://www.codecademy.com/courses/learn-python-3/projects/python-magic-8-ball" target="_blank" data-CodecademyLearnPython3CourseButt="CodecademyLearnPython3CourseButt_data"><img src="https://user-images.githubusercontent.com/82598726/175697552-f960b057-9e97-4c3e-a3e2-f2b5f7876de9.png" alt="Codecademy_Learn_Python3_Course_button" width="400px" height="300px"></a>


<br><br>


# Magic 8-Ball

# 1. Introduction:
The [Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8_Ball) is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a <b>magic8.py</b> Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

![Alt text](image.png)

We’ll be using the following 9 possible answers for our Magic 8-Ball:

- <b>Yes - definitely</b> <br><br>
- <b>It is decidedly so</b> <br><br>
- <b>Without a doubt</b> <br><br>
- <b>Reply hazy, try again</b> <br><br>
- <b>Ask again later</b> <br><br>
- <b>Better not tell you now</b> <br><br>
- <b>My sources say no</b> <br><br>
- <b>Outlook not so good</b> <br><br>
- <b>Very doubtful</b> <br><br>

The output of the program will have the following format:

> [Name] asks: [Question] <br>
Magic 8-Ball’s answer: [Answer]

For example:

> Joe asks: Is this real life?<br>
Magic 8-Ball's answer: Better not tell you now

# 2. Output:
> Joe  asks:  Will I win the lottery?<br>
Magic 8-Ball's answer:  Ask again later<br><br>

> Joe  asks:  Will I win the lottery?<br>
Magic 8-Ball's answer:  My sources say so

> Then answer comes after "Magic 8-Ball's answer:" will be changed randomly each time a user runs this program.

# 3. Prompts:

> 1. In <b>magic8.py</b>, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.<br>

Assign the variable name to a string value. In Python, a string must be wrapped in a pair of quotes.
```python
name = "Joe"
```

<br>

> 2. Next, declare a variable <b>question</b>, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
```python
question = "Will I win the lottery?"
```

<br>

> 3. We want to store the answer of the Magic 8-Ball in another variable, which we’ll call <b>answer</b>. For now, assign this variable to an empty string.

<br>

### Generating a random number

<br>

> 4. In order for the answer to be different each time we run the program, we will utilize randomly generated values.<br><br>
<b>Note:</b> This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code.<br><br>
In Python, we can use the <b>.randint()</b> function from the <b>random</b> module to generate a random number from a range.<br><br>
But first, let’s import this module so we can use its functions. Add this line of code to the top of <b>magic8.py</b>:
```python
import random
```

<br>

> 5. Next, we’ll create a variable to store the randomly generated value. Declare a variable called <b>random_number</b>, and assign it to the function call:
```python
random.randint(1, 9)
```
> which will generate a random number between <b>1</b> (inclusive) and <b>9</b> (inclusive).<br><br>
Next, add a <b>print()</b> statement that outputs the value of <b>random_number</b>, and run the program several times to ensure random values are being generated as expected.<br><br>
Once you’re sure this is working as we expected, feel free to comment out this <b>print()</b> statement.
```python
random_number = random.randint(1,9)
# print(random_number)
```

<br>

> 6. Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!<br><br>
For this section, we’ll be utilizing control flow using an <b>if/elif/else</b> statement to assign different answers for each randomly generated value.<br><br>
First, write an <b>if</b> statement where if the <b>random_number</b> is equal to <b>1</b>, <b>answer</b> is assigned to the phrase “Yes - definitely”
```python
if random_number == 1:
  answer = "Yes - definitely"
```
<br>

> 7. Next, write an <b>elif</b> statement after the <b>if</b> statement where if the <b>random_number</b> is equal to <b>2</b>, <b>answer</b> is assigned to the phrase “It is decidedly so”.<br><br>
Then, continue writing <b>elif</b> statements for each of the remaining phrases for the values <b>3</b> to <b>9</b>.<br><br>
Recall that the 9 possible answers of the Magic 8-Ball are:<br><br>
>> - <b>Yes - definitely</b> <br><br>
>> - <b>It is decidedly so</b> <br><br>
>> - <b>Without a doubt</b> <br><br>
>> - <b>Reply hazy, try again</b> <br><br>
>> - <b>Ask again later</b> <br><br>
>> - <b>Better not tell you now</b> <br><br>
>> - <b>My sources say no</b> <br><br>
>> - <b>Outlook not so good</b> <br><br>
>> - <b>Very doubtful</b> <br><br>

<br>

> 8. Following the <b>if/elif</b> statements, add an <b>else</b> statement that will set <b>answer</b> to the string “Error”, if the number was accidentally assigned a value outside of our range.
```python
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say so"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
```

<br>

### Seeing the result

> 9. Now, let’s see our program in action! Write a <b>print()</b> statement to output the asker’s <b>name</b> and their <b>question</b>, which should be in the following format:<br><br>
[Name] asks: [Question] <br><br>
For example, when we run the program, the output should look something like:<br><br>
Joe asks: Will I win the lottery?
```python
print(name," asks: ",question)
```

<br>

> 10. Add a second <b>print()</b> statement that will output the Magic 8-Ball’s <b>answer</b> in the following format:<br><br>
Magic 8-Ball's answer: [answer]<br><br>
For example, when running the program it should look something like:<br><br>
Magic 8-Ball's answer: My sources say no
```python
print("Magic 8-Ball's answer: ",answer)
```

<br>

> 11. Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.<br><br>
Run your program several times to see that it’s working as expected.

<br>

### Optional Challenges

<br>

> 12. If you’re up for some more challenges, try implementing the following features to your program. <br><br>
So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.<br><br>
To do this, you will need to increase the range of randomly generated numbers and add additional <b>elif</b> statements for each new answer.

For example, if we add one more answer to the Magic 8-Ball, there will be a total of <b>10</b> outcomes, we’ll need to expand the range of randomly generated values to <b>10</b> instead of <b>9</b>.
```python
random_number = random.randint(1, 10)
```

Then we’ll need to add another <b>elif</b> statement, which will assign the variable <b>answer</b> to the new possible phrase, like the following:
```python
elif random_number == 10:
  answer = "Signs point to yes"
```

<br>

> 13. What if the asker does not provide a name, such that the value of <b>name</b> is an empty string? If the <b>name</b> string is empty, the output of the program looks like the following:<br><br>
 asks: Will I win the lottery?<br>
Magic 8 Ball's answer: Outlook not so good<br><br>
As you can see, the formatting of the output can use some improvement when there is no name provided.<br><br>
We can address this by printing out just the question, such that it looks like the following:<br><br>
Question: Will I win the lottery?<br>
Magic 8-Ball's answer: Outlook not so good<br><br>
You can implement this by creating an <b>if/else</b> statement such that:<br><br>
>> - If the name is an empty string, it will only print the question.<br><br>
>> - Else, the player’s name and question are both printed.<br><br>

We can write an <b>if</b> statement that checks if the <b>name</b> is set to an empty string. In Python, you can do this a few ways, including:
```python
if name == ""
```
or,
```python
if len(name) == 0
```
Within the <b>if</b> statement, when there is no name provided, we can just print the <b>question</b>:
```python
if name == "":
  print("Question: " + question)
```
Otherwise, we can print the <b>name</b> and the <b>question</b> within an <b>else</b> statement block:
```python
else:
  print(name + " asks: " + question)
```

<br>

> 14. What if the <b>question</b> string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!<br><br>
To ensure that the fabric of reality is safe, we can create an <b>if/else</b> statement where:<br><br>
>> - If the question is an empty string, print out a message to the user.<br><br>
>> - Else, print the name and question, with the Magic 8-Ball’s answer.

If the <b>question</b> is an empty string, we want to let the user know, and prevent the other <b>print()</b> statements from being run.

To check if the <b>question</b> is set to an empty string, we can use one of the following conditions for the <b>if</b> statement:
```python
if question == "":
  # do something
```
or
```python
if len(question) == 0:
  # do something
```
Using either of these conditions to check that the <b>question</b> is empty, we will write a <b>print()</b> statement within the <b>if</b> statement block that will output a message, like so:
```python
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
```

Else, if a question is provided, we can run the other <b>print()</b> statements:
```python
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
```

<br>

> 15. Don’t forget to check off all the tasks before moving on.<br><br>
Sample solutions:<br><br>
>> - [magic8.py](https://github.com/Codecademy/learn-python/blob/main/2-control-flow/magic-8-ball/magic8.py)<br><br>
P.S. If you make something cool, share it with us!



