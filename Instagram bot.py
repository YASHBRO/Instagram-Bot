from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        #By default this code works only on chrome browser.
        #Replace the browser name(Chrome() here) by your browser name as:
        #self.driver=webdriver.{} ->Your browser name
        
        self.username = username
        self.driver.get("https://instagram.com")
        self.wait = WebDriverWait(self.driver, 10).until

        self.wait(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))\
            .click()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))\
            .click()


    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/{}')]".format(self.username))))\
            .click()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]")))\
            .click()
        following = self._get_names()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))) \
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        you_not_following_back = [user for user in followers if user not in following]
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()

        f1 = open("Not Following Back", "w")
        f1.write("\n".join(not_following_back))
        f1.close()

        f2 = open("You not Following Back", "w")
        f2.write("\n".join(you_not_following_back))
        f2.close()

        print("People who aren't following back ({}) :\n".format(len(not_following_back)))
        print('\n'.join(not_following_back))
        print("\n\nDo you want to UNFOLLOW them all??")
        ans1 = input("Y/N : ")
        if ans1 == "Y" or ans1 == "y":
            InstaBot.unfollow(self, not_following_back)
        elif ans1 == "N" or ans1 == "n":
            pass

        print("\n\n\n\nPeople whom you don't follow back ({}) :\n".format(len(you_not_following_back)))
        print('\n'.join(you_not_following_back))
        print("\n\nDo you want to FOLLOW BACK them all??")
        ans2 = input("Y/N : ")
        if ans2 == "Y" or ans2 == "y":
            InstaBot.follow_back(self, you_not_following_back)
        elif ans2 == "N" or ans2 == "n":
            pass

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button") \
            .click()
        return names

    def unfollow(self, not_following_back):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()
        for i in not_following_back:
            self.wait(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Search')]"))) \
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))) \
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//a[@href='/{}/']".format(i)))) \
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//span[@class='glyphsSpriteFriend_Follow u-__7']")))\
                .click()
            sleep(1)
            self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Unfollow')]").click()))
            sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()

    def follow_back(self, you_not_following_back):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()
        for i in you_not_following_back:
            self.wait(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Search')]")))\
                .click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']") \
                .send_keys(i)
            self.wait(EC.element_to_be_clickable((By.XPATH, "//a[@href='/{}/']".format(i))))\
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Follow Back')]")))\
                .click()
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()

    def spamming(self):
        recipients = input("Recipients (seperate by < , >)").split(",")
        print(recipients)
        msg = input("Message : ")
        count = int(input("How many messages : "))
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()

        for i in recipients:
            self.wait(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Search')]"))) \
                .click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']") \
                .send_keys(i)
            self.wait(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'{}')]".format(i.title())))) \
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Message')]"))) \
                .click()
            self.wait(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Message...']"))) \
                .click()
            for k in range(count):
                self.driver.find_element_by_xpath("//textarea[@placeholder='Message...']") \
                    .send_keys(msg)
                self.wait(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Send')]"))) \
                    .click()
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()

    def log_out(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']") \
            .click()
        self.wait(EC.element_to_be_clickable((By.XPATH, "//span[@class='_2dbep qNELH']"))) \
            .click()
        log_out="/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div"
        self.wait(EC.element_to_be_clickable((By.XPATH, log_out))) \
            .click()
        Users().start_user()

    def quit(self):
        self.driver.quit()


class Users:

    def __init__(self):
        super().__init__()
        self.users = {}
        count = self.check_user()
        if count == 0:
            print("No user found, please add atleast 1 user")
            add_user()

    def check_user(self):
        f = open("Users", "r")
        data = f.readlines()
        if len(data) != 0:
            for i in range(0, len(data) - 1, 2):
                self.users[str(data[i])[0:-1].strip()] = (str(data[i + 1])[0:-1].strip())
        else:
            return 0
        f.close()

    def start_user(self):
        f = open("Users", "r")
        print("\nSelect user : ")
        for i in range(len(self.users)):
            print("( {} ) {}".format(i + 1, list(self.users.keys())[i]))
        print('''\n(a) To Add user      (r) To Remove user      (q) Quit application''')
        self.ans = input(":- ")
        if self.ans == "q" or self.ans == "Q":
            self.bot.quit()
        else:
            if self.ans == "a" or self.ans == "A":
                add_user()
                self.start_user()
            elif self.ans == "r" or self.ans == "R":
                self.remove_user()
                self.start_user()
            self.bot = InstaBot(list(self.users.keys())[int(self.ans) - 1], list(self.users.values())[int(self.ans) - 1])
            f.close()
            self.start_cmd()

    def remove_user(self):
        remove = input("Username that to be removed: ")
        f = open("Users", "w")
        for i in self.users:
            if i != remove:
                f.write(i + "\n" + self.users.get(i) + "\n")
        f.close()
        self.users.pop(remove)
        self.check_user()

    def start_cmd(self):
        print("Choose an action \n(1) Follow Back stats [OPTIONAL->Unfollow/Follow back]\n(2) Spam Bot\n(3) Change User\n(4) Quit application")
        a = int(input().strip())
        if a == 4:
            self.bot.quit()
        else:
            try:
                if a == 1:
                    self.bot.get_unfollowers()
                elif a == 2:
                    self.bot.spamming()
                elif a==3:
                    self.bot.log_out()
            except:
                print("Some error occurred\n Please try again")
                input("\n\n")

            self.start_cmd()


def add_user():
    f = open("Users", "a")
    for i in range(int(input("No. of users to be added : "))):
        f.write(input("Enter username : ") + '\n')
        f.write(input("Enter password of : ") + '\n')
    f.close()
    Users().check_user()


try:
    f = open("Users", "r")
    f.close()
except:
    f = open("Users", "w")
    f.close()

start = Users()
start.check_user()
start.start_user()
print('\n------------------THANKS FOR USING MY BOT------------------\n')
