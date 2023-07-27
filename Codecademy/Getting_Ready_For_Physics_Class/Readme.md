# <img src="https://github.com/phuongtrieu97coder/Readme_Content_Structure/assets/82598726/174e2883-2d0b-4d01-8992-32f709b72373" alt="Python" width="100px" height="100px">


<img src="https://github.com/phuongtrieu97coder/Python_projects/assets/82598726/19e383e6-169d-428b-8879-766b22b50211" alt="python_poster" width="400px" height="300px"> <a type="button" title="Codecademy_Learn_Python3_Course_button" href="https://www.codecademy.com/courses/learn-python-3/projects/physics-class" target="_blank" data-CodecademyLearnPython3CourseButt="CodecademyLearnPython3CourseButt_data"><img src="https://user-images.githubusercontent.com/82598726/175697552-f960b057-9e97-4c3e-a3e2-f2b5f7876de9.png" alt="Codecademy_Learn_Python3_Course_button" width="400px" height="300px"></a>


<br><br>


# Getting Ready for Physics Class

# 1. Introduction:
You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.


# 2. Output:
>226800<br>
The GE train supplies 226800 Newtons of force.<br>
A 1kg bomb supplies 600000000 Joules.<br>
The GE train does 22680000 Joules of work over 100 meters.

# 3. Prompts:

> 1. Write a function called <b>f_to_c</b> that takes an input <b>f_temp</b>, a temperature in Fahrenheit, and converts it to <b>c_temp</b>, that temperature in Celsius.<br><br>
It should then return <b>c_temp</b>.<br><br>
The equation you should use is:<br><br>
Temp (C) = (Temp (F) - 32) * 5/9
```python
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9
  return c_temp
```
<br>

> 2. Let’s test your function with a value of 100 Fahrenheit.<br><br>
Define a variable <b>f100_in_celsius</b> and set it equal to the value of <b>f_to_c</b> with <b>100</b> as an input.
```python
f100_in_celsius = f_to_c(100)
```
<br>

> 3. Write a function called <b>c_to_f</b> that takes an input <b>c_temp</b>, a temperature in Celsius, and converts it to <b>f_temp</b>, that temperature in Fahrenheit.<br><br>
It should then return <b>f_temp</b>.<br><br>
The equation you should use is:<br><br>
Temp (F) = Temp (C) * (9/5) + 32
```python
def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32
  return f_temp
```

<br>

> 4. Let’s test your function with a value of 0 Celsius.<br><br>
Define a variable <b>c0_in_fahrenheit</b> and set it equal to the value of <b>c_to_f</b> with <b>0</b> as an input.
```python
c0_in_fahrenheit = c_to_f(0)
```
<br>

### Use the Force

> 5. Define a function called <b>get_force</b> that takes in <b>mass</b> and <b>acceleration</b>. It should return <b>mass</b> multiplied by <b>acceleration</b>.
```python
def get_force(mass,acceleration):
  return mass*acceleration
```

<br>

> 6. Test <b>get_force</b> by calling it with the variables <b>train_mass</b> and <b>train_acceleration</b>.<br><br>
Save the result to a variable called <b>train_force</b> and print it out.<br><br>
<b>train_mass</b> and <b>train_acceleration</b> have been defined for you at the top of <b>script.py</b>. Make sure to uncomment those lines before trying to use these variables.

```python
train_force = get_force(train_mass,train_acceleration)
print(train_force)
```

<br>

> 7. Print the string <b>“The GE train supplies X Newtons of force.”</b>, with <b>X</b> replaced by <b>train_force</b>.
```python
print("The GE train supplies",train_force,"Newtons of force.")
```

<br>

> 8. Define a function called <b>get_energy</b> that takes in <b>mass</b> and <b>c</b>.<br><br>
<b>c</b> is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set <b>c</b> to have a default value of <b>3*10**8</b>.<br><br>
<b>get_energy</b> should return <b>mass</b> multiplied by <b>c</b> squared.

```python
def get_energy(mass,c=3*10**8):
  return mass*c*2
```

<br>

> 9. Test <b>get_energy</b> by using it on <b>bomb_mass</b>, with the default value of <b>c</b>. Save the result to a variable called <b>bomb_energy</b>.<br><br>
<b>bomb_mass</b> has been defined for you at the top of <b>script.py</b>. Make sure to uncomment this line before trying to use <b>bomb_mass</b>.

```python
bomb_energy = get_energy(bomb_mass)
```
<br>

> 10. Print the string <b>“A 1kg bomb supplies X Joules.”</b>, with <b>X</b> replaced by <b>bomb_energy</b>.
```python
print("A 1kg bomb supplies",bomb_energy,"Joules.")
```

<br>

### Do the Work

<br>


> 11. Define a final function called <b>get_work</b> that takes in <b>mass</b>, <b>acceleration</b>, and <b>distance</b>.<br><br>
Work is defined as force multiplied by distance. First, get the <b>force</b> using <b>get_force</b>, then multiply that by <b>distance</b>. Return the result.

```python
def get_work(mass,acceleration,distance):
   return get_force(mass,acceleration)*distance
```

<br>

> 12. Test <b>get_work</b> by using it on <b>train_mass</b>, <b>train_acceleration</b>, and <b>train_distance</b>. Save the result to a variable called <b>train_work</b>.

```python
train_work = get_work(train_mass,train_acceleration,train_distance)
```

<br>

> 13. Print the string <b>"The GE train does X Joules of work over Y meters."</b>, with <b>X</b> replaced with <b>train_work</b> and <b>Y</b> replaced with <b>train_distance</b>.

```python
print("The GE train does",train_work,"Joules of work over",train_distance,"meters.")
```


