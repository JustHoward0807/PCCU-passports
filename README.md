# PCCU-passports

 This is a web scraping project for my graduation work - GP(Graduation Points) 
 Link: <em>https://github.com/JustHoward0807/GP<em>

 Tools: ***Python, BeautifulSoup and Chromedriver***
## Introduction

So... Basically, our school require 5 different points collected in order to graduate which are **'德(Dé)', '智(Zhi)', '體(Ti)', '群(Qún)', '美(Mei)'.**

Each points required totally different activities, such as **'智(Zhi)'** which you need to attend events that is related to gaining knowledge like museum and **'體(Ti)'** need students to attend school events related to sport.

Find more information on our school website: <em>https://pass.pccu.edu.tw/bin/home.php<em>

## How it work

I use Python to capture the .xlsx file from the school website which I just provided and get the data I want and output as a csv file format.

This is before I sort the data out and as you can see how messy and it is not easy understanding for the first time people open this file.

The data still contains invalid events or blank space coming out of nowhere which causes some misunderstanding to students.
[link]

And this is after I erase all the blank space and invalid events, only capture the information I need for the graduation project.
[link]


In the end, I upload all the data I need from the .csv file to firebase.
[link]