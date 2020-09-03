from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        self.not_following_back = [user for user in following if user not in followers]
        self.you_not_following_back = [user for user in followers if user not in following]
        sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        f1= open("Not Following Back","w")
        f1.write("\n".join(self.not_following_back))
        f1.close
        f2= open("You not Following Back","w")
        f2.write("\n".join(self.you_not_following_back))
        f2.close
        print (("People who aren't following back ({}) :\n").format(len(self.not_following_back)))
        print('\n'.join(self.not_following_back))
        print("\n\n\Do you want to UNFOLLOW them all??")
        ans1=input("Y/N : ")
        if ans1=="Y" or ans1=="y":
            InstaBot.unfollow(self)
        elif ans1=="N" or ans1=="n":
            pass
        print (("\n\n\n\n\n\n\nPeople whom you don't follow back ({}) :\n").format(len(self.you_not_following_back)))
        print('\n'.join(self.you_not_following_back))
        print("\n\n\Do you want to FOLLOW BACK them all??")
        ans2=input("Y/N : ")
        if ans2=="Y" or ans2=="y":
            InstaBot.follow_back(self)
        elif ans2=="N" or ans2=="n":
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
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def unfollow(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        sleep(2)
        for i in self.not_following_back:
            self.driver.find_element_by_xpath("//span[contains(text(),'Search')]")\
                .click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']")\
                .send_keys(i)
            sleep(2)
            self.driver.find_element_by_xpath(("//a[@href='/{}/']").format(i))\
                .click()
            sleep(4)
            self.driver.find_element_by_xpath("//span[@class='glyphsSpriteFriend_Follow u-__7']")\
                .click()
            sleep(1)
            self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")\
                .click()
            sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()

    def follow_back(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        sleep(2)
        for i in self.you_not_following_back:
            self.driver.find_element_by_xpath("//span[contains(text(),'Search')]")\
                .click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']")\
                .send_keys(i)
            sleep(2)
            self.driver.find_element_by_xpath(("//a[@href='/{}/']").format(i))\
                .click()
            sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(),'Follow Back')]")\
                .click()
            sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()

    def spammig(self):
        reciepents=input("Reciepents (seperate by < , >)").split(",")
        print(reciepents)
        msg=input("Message : ")
        count=int(input("How many messages : "))
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()
        sleep(2)

        for i in reciepents:
            self.driver.find_element_by_xpath("//span[contains(text(),'Search')]")\
                .click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']")\
                .send_keys(i)
            sleep(2)
            self.driver.find_element_by_xpath(("//span[contains(text(),'{}')]").format((i).title()))\
                .click()
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Message')]")\
                .click()
            sleep(2)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Message...']")\
                .click()
            sleep(1)
            for k in range(count):
                sleep(0.5)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Message...']")\
                    .send_keys(msg)
                sleep(.5)
                self.driver.find_element_by_xpath("//button[contains(text(),'Send')]")\
                .click()
                sleep(0.5)
        sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='Instagram']")\
            .click()

    def quit(self):
        self.driver.quit()



user=[]
print("Choose user:")
for i in range(len(user)):
    print("[ {} ]. {}".format((i+1),user[i][0]))
ans=int(input(":- "))
my_bot = InstaBot(user[ans-1][0], user[ans-1][1])
z=1
while z!=0:
    print("Choose an actoin \n( 1 ) Follow Back stats -{OPTIONAL-->Unfollow/Follow back}\n( 2 ) Spam Bot")
    act=int(input(":- "))

    if act==1:
        my_bot.get_unfollowers()
    elif act==2:
        my_bot.spammig()
    
    z=int(input("\n\nIf you want to go back to menu, enter '1'\nTo exit, enter '0' :\n"))
    if z==0:
        my_bot.quit()

print('\n----------------D----O----N----E----------------')
