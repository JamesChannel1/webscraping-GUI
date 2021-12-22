import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

main = tkinter.Tk()
main.geometry("300x300")
main.title("webscraping tool")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

l = tkinter.Label(main, text="webscrape:")
l.pack()

#RT news

def fun1():
    driver.get("https://www.rt.com/news/")
    time.sleep(5)
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("russia")
    time.sleep(0.5)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.5)

def fun2():
    thing = driver.find_element_by_class_name("js-listing__content")
    print(thing.text)
    time.sleep(0.5)

def fun3():
    thing = driver.find_element_by_class_name("js-listing__content")
    root = tkinter.Tk()
    root.title("text window")
    root.geometry("1600x768")
    text1 = tkinter.Text(root, height=100, width=400)
    text1.insert(tkinter.INSERT, thing.text)
    text1.pack()

def fun4():
    fun1()
    fun2()
    fun3()

# mmafighting news

def fun1a():
    driver.get("https://www.mmafighting.com/latest-news")
    time.sleep(5)
    mma = driver.find_element_by_class_name("l-col__main")
    print(mma)
    time.sleep(0.5)

def fun2a():
    mma = driver.find_element_by_class_name("l-col__main")
    root = tkinter.Tk()
    root.title("text window")
    root.geometry("1600x768")
    text1 = tkinter.Text(root, height=100, width=400)
    text1.insert(tkinter.INSERT, mma.text)
    text1.pack()

def fun3a():
    fun1a()
    fun2a()

# techmeme

def fun1b():
    driver.get("https://www.techmeme.com/")
    time.sleep(5)
    techmeme = driver.find_element_by_class_name("clus")
    print(techmeme)
    time.sleep(0.5)

def fun2b():
    techmeme = driver.find_element_by_class_name("clus")
    root = tkinter.Tk()
    root.title("text window")
    root.geometry("1600x768")
    text1 = tkinter.Text(root, height=100, width=400)
    text1.insert(tkinter.INSERT, techmeme.text)
    text1.pack()

def fun3b():
    fun1b()
    fun2b()


b1 = tkinter.Button(main, text="RT news", command=fun4)
b1.pack()

b2 = tkinter.Button(main, text="mmafighting", command=fun3a)
b2.pack()

b3 = tkinter.Button(main, text="techmeme", command=fun3b)
b3.pack()

main.mainloop()
