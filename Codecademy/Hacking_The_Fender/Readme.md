# <img src="https://github.com/phuongtrieu97coder/Readme_Content_Structure/assets/82598726/174e2883-2d0b-4d01-8992-32f709b72373" alt="Python" width="100px" height="100px">


<img src="https://github.com/phuongtrieu97coder/Python_projects/assets/82598726/19e383e6-169d-428b-8879-766b22b50211" alt="python_poster" width="400px" height="300px"> <a type="button" title="Codecademy_Learn_Python3_Course_button" href="https://www.codecademy.com/courses/learn-python-3/projects/hacking-the-fender" target="_blank" data-CodecademyLearnPython3CourseButt="CodecademyLearnPython3CourseButt_data"><img src="https://user-images.githubusercontent.com/82598726/175697552-f960b057-9e97-4c3e-a3e2-f2b5f7876de9.png" alt="Codecademy_Learn_Python3_Course_button" width="400px" height="300px"></a>


<br><br>


# Hacking The Fender

# 1. Introduction:
<b>The Fender</b>, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to <b>The Fender</b>‘s systems, you must update his <b>"passwords.txt"</b> file to scramble the secret data. The last thing you need to do is add the signature of <b>Slash Null</b>, a different hacker whose nefarious deeds could be very conveniently halted by <b>The Fender</b> if they viewed <b>Slash Null </b>as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

# 2. Output:
We are going to have new files with new contents inside it when we finish this project

# 3. Prompts:

> 1. Are you there? We’ve opened up a communications link to <b>The Fender</b>‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called <b>"passwords.csv"</b>.<br><br>
First import the CSV module, since we’ll be needing it to parse the data.
```python
import csv
```

<br>

> 2. We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable <b>compromised_users</b>.
```python
compromised_users = []
```

> 3. Next we’ll need you to open up the file itself. Store it in a file object called <b>password_file</b>.
<br>

<br>

> 4. Pass the <b>password_file</b> object holder to our CSV reader for parsing. Save the parsed <b>csv.DictReader</b> object as <b>password_csv</b>.
```python
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
```

<br>

> 5. Now we’ll want to iterate through each of the lines in the CSV.<br><br>
Create a for loop and save each row of the CSV into the temporary variable <b>password_row</b>.

<br>

> 6. Inside your for loop, print out <b>password_row['Username']</b>. This is the username of the person whose password was compromised.<br><br>
Run your code, do you see a list of usernames?
```python
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    print(password_row['Username'])
```

<br>

> 7. Remove the <b>print</b> statement. We want to add each username to the list of <b>compromised_users</b>. Use the list’s <b>.append()</b> method to add the username to <b>compromised_users</b> instead of printing them.
```python
compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])
```

<br>

> 8. Exit out of your <b>with</b> block for <b>"passwords.csv"</b>. We have all the data we need from that file.<br><br>
Start a new <b>with</b> block, opening a file called <b>compromised_users.txt</b>. Open this file in write-mode, saving the file object as <b>compromised_user_file</b>.
```python

with open('compromised_users.txt','w') as compromised_user_file:
  
```

<br>

> 9. Inside the new context-managed block opened by the <b>with</b> statement start a new <b>for</b> loop.<br><br>
Iterate over each of your <b>compromised_users</b>.

<br>

> 10. Write the username of each <b>compromised_user</b> in <b>compromised_users</b> to <b>compromised_user_file</b>.
```python
with open('compromised_users.txt','w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

```

<br>

> 11. Exit out of that <b>with</b> block. You’re doing great so far! We’ve got the data we need to employ as insurance against <b>The Fender</b>.

<br>

## Notifying the Boss

<br>

> 12. Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.<br><br>
First we’ll need to import the <b>json</b> module.
```python
import json
```

<br>

> 13. Open a new JSON file in write-mode called <b>boss_message.json</b>. Save the file object to the variable <b>boss_message</b>.
```python
with open('boss_message.json','w') as boss_message
```

<br>

> 14. Create a Python dictionary object within your <b>with</b> statement that relays a boss message. Call this <b>boss_message_dict</b>.<br><br>
Give it a <b>"recipient"</b> key with a value <b>"The Boss"</b>.<br><br>
Also give it a <b>"message"</b> key with the value <b>"Mission Success"</b>.
```python
with open('boss_message.json','w') as boss_message:
  boss_message_dict = {
    "recipient":"The Boss",
    "message":"Mission Success"
  }
```
<br>

> 15. Write out <b>boss_message_dict</b> to <b>boss_message</b> using <b>json.dump()</b>.
```python
  json.dump(boss_message_dict,boss_message)
```
<br>

## Scrambling the Password

<br>

> 16. Now that we’ve safely recovered the compromised users we’ll want to remove the <b>"passwords.csv"</b> file completely.<br><br>
Create a new <b>with</b> block and open <b>"new_passwords.csv"</b> in write-mode. Save the file object to a variable called <b>new_passwords_obj</b>.
```python

with open("new_passwords.csv",'w') as new_passwords_obj:

```

<br>

> 17. Enemy of the people, <b>Slash Null</b>, is who we want <b>The Fender</b> to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches. Here is the signature:
```python
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

"""

```
> Save that as a multiline string to the variable <b>slash_null_sig</b>.

<br>

> 18. Write <b>slash_null_sig</b> to <b>new_passwords_obj</b>. Now we have the file to replace <b>passwords.csv</b> with!
```python
with open("new_passwords.csv",'w') as new_passwords_obj:
 new_passwords_obj.write(slash_null_sig)
```

<br>

> 19. What an incredible success! We’ll take care of moving the new passwords file over the old one in case you want to practice hacking <b>The Fender</b> in the future.<br><br>
Thank you for your service, programmer.