# Instagram-Bot  

![alt Instagram](https://image.flaticon.com/icons/png/128/174/174855.png)

-------------------------------------------------

**Multi purpose Bot**
	
For now, it performs only two actions:

1. **Give list of people** :
	- Who don't follow you back 
		- _Optional-> Unfollow them all_
	- Whom you don't follow back 
		- _Optional-> Follow back them all_

2. **Spamming bot** :
	-It can spam multiple people with the custom message you provide




-------------
### Contact:


_For suggestions and bug/error report_
	
Email :- yashjoglekar2012@gmail.com




-----------------
## Requirements:


1. Python 3

- [Python3 download link](https://www.python.org/downloads)

2. Python IDE
	- Any IDE will work. In my case, I used Pycharm Community version. 
		- [Pycharm download link](https://www.jetbrains.com/pycharm/download/#section=windows)

3. Selenium module
- Run " pip install selenium " in your terminal to install selenium.

4. Web driver of your respective browser
	- In my case its Chrome.
		- [Chrome driver download link](https://chromedriver.chromium.org/downloads)
	- Place the .exe file of your webdriver in the directory where the python.exe exist.
	- General directory location :- C:\Program Files\Python38 {or which ever python version is installed, Python37 if python 3.7 is installed}.




---------------
## Instruction:


Please read the comments at line 9,22,26,174,175,176
	
Once you are done with the code, run it:

1. It'll ask you for the username through which you want to login
2. It'll ask for the action you want to perform

Later steps will be clear on your terminal
		
_Note: Please make sure you opt the command/choice in form of numbers(1,2,3,4...), as the numbers will be mentioned in-front of the option_
	
	
	
	
-------------
## Errors:


If your IDE display the message " {Blah Blah} not found in the page " kind of message, it might be due to your connection speed.
if you face the above mentioned error, please add few more seconds in the "Sleep()" function which you'll find after every few lines
