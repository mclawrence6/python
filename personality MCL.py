import webbrowser as wb
points = 0
import time as t
import pyautogui as pg


name = pg.prompt("What is your name? ").title()

pg.alert(name)
if name == "Caroline":
    pg.alert ("Hi " + name)
    points += 5
    t.sleep(1) 
    wb.open ("https://www.textgiraffe.com/Caroline/Page2/")
elif name == "Bob":
    pg.alert (name + ",you are a great person!")
    points += 3
    t.sleep(1)
    wb.open("http://dreamworks.wikia.com/wiki/File:Bob_the_Builder.jpeg")
elif name == "Catherine":
    pg.alert (name + "I like you already.")
    points += 2
    t.sleep(2)
    wb.open ("https://www.amazon.com/Catherine-Street-Sign-Reflective-Aluminum/dp/B00KY6ZDZW")
elif name == "James":
    pg.alert ("nice to meet you" + name)
    points += 1
    t.sleep(1)
    wb.open ("https://www.youtube.com/watch?v=uV9LYMAEnRA")
elif name == "Kate":
    pg.alert ("Hello!")
    points += 2
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=kate+name&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj-3cyIyJzeAhVRnOAKHRnoCtQQ_AUIDigB&biw=924&bih=639#imgrc=sbQIiK5VLfo7kM:")
elif name == "Will":
    pg.alert ("Coool!")
    ponts += 3
    t.sleep (2)
    wb.open ("https://www.google.com/search?q=will+name&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj3n93PyJzeAhWvY98KHcoWCFEQ_AUIDigB&biw=924&bih=639#imgrc=Z0hfeIoXQgHxJM:")
else:
    pg.alert ("I don't know you!")
    points += 0
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjwsdL4gYveAhXtc98KHaGcAz0Q_AUIDigB&biw=1366&bih=657")
color = pg.prompt ("what is your favorite color? ").title()
if color == "Blue":
    pg.alert ("mine too!")
    points += 5
    t.sleep(1)
    wb.open ("https://www.youtube.com/watch?v=SoIKv3xxuMA")
elif color == "Pink":
    pg.alert ("Do you like unicorns too?")
    points += 2
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=a-xWhG4UU_Y")
elif color == "Purple":
    pg.alert ("cool!")
    points += 3
    t.sleep(1)
    wb.open ("https://www.youtube.com/watch?v=TvnYmWpD_T8")
elif color == "Black":
    pg.alert ("ok...")
    points -= 2
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=goth&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ-tDj-oreAhUpUt8KHWZsAzQQ_AUIDigB&biw=1366&bih=657#imgrc=odGcWJwuqRcJsM:")
elif color == "Yellow":
    pg.alert ("Like a sunflower!")
    points += 1
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=sunflower&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiZyKCTyZzeAhXGc98KHd8kDJ8Q_AUIDigB&biw=924&bih=639#imgrc=8kZ1NZp_9-nr5M:")
elif color == "Brown":
    pg.alert ("wow.")
    points -= 5
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=dsJtgmAhFF4")
else:
    pg.alert("nice")
    points += 1
    t.sleep(2)
    wb.open ("https://giphy.com/explore/rainbow")
sport = pg.prompt ("What is your favorite sport? ").title()
if sport == "Hockey":
    pg.alert ("yep, I guess your cool")
    points += 5
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=JDnZTUkCOBQ")
elif sport == "Soccer":
    pg.alert ("you mean futbol...")
    points += 5
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=K-U1ZgrsGGg")
elif sport == "Lacrosse":
    pg.alert (" I used to play..")
    points += 2
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=o5hsPBsGD44")
elif sport == "Football":
    pg.alert ("that cool.")
    points += 4
    t.sleep(3)
    wb.open ("https://www.google.com/search?q=football&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimsOqj_IreAhUumeAKHd-FD6kQ_AUIDigB&biw=1366&bih=657#imgrc=GCqjPQ-jqckcfM:")
elif sport == "Field Hockey":
    pg.alert ("Nice!")
    points += 2
    t.sleep(3)
    wb.open ("https://www.google.com/search?q=field+hockey&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwieus2jypzeAhWvVN8KHeK1CJ8Q_AUIDigB&biw=924&bih=639#imgrc=FCpGZY2CS5KVXM:")
elif sport == "Surfing":
    pg.alert ("WOAH")
    points += 7
    t.sleep(1)
    wb.open ("https://www.youtube.com/watch?v=HBklS2vYEPo")
else:
    pg.alert ("cool")
    points += 0
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=no+sports&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiGqOK-_IreAhXFneAKHcEGANIQ_AUIDigB&biw=1366&bih=657#imgrc=y7acx-yoEouoUM:")
subject = pg.prompt ("What is your favorite subject?").title()
if subject == "Math":
    pg.alert ("so your a mathmatician")
    points += 2
    t.sleep(3)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=1366&bih=657&tbm=isch&sa=1&ei=HNvFW9yoDYTm_QbUyKzgDw&q=addiong&oq=addiong&gs_l=img.3..0i10i24.5226.6666..6852...1.0..0.56.417.8......0....1..gws-wiz-img.......0j0i67j0i10.kcqMNDR26RY#imgrc=LqznGvY1fJpCGM:")
elif subject == "Computer science":
    pg.alert ("nice")
    points += 9
    t.sleep(3)
    wb.open ("https://www.google.com/search?q=computers&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiom6vv_IreAhUuneAKHXVGA4kQ_AUIDygC&biw=1366&bih=657")
elif subject == "English":
    pg.alert ("I like it too.")
    points += 3
    t.sleep(3)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=1366&bih=657&tbm=isch&sa=1&ei=hNvFW4e3Jafp_QbR26mIDw&q=+book&oq=+book&gs_l=img.3..0i67l3j0j0i67j0l5.3464.3464..3690...0.0..0.51.51.1......0....1..gws-wiz-img.2n6KjdjVyU0")
elif subject == "Science":
    pg.alert ("Bill Nye the Science Guy.")
    points += 3
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=nDN7M0J3HXc")
elif subject == "Spanish":
    pg.alert ("Hola! Como estas?")
    points += 3
    t.sleep(2)
    wb.open ("https://www.google.com/search?hl=en&authuser=0&rlz=1C1GCEA_enUS752US774&tbm=isch&q=fiesta&chips=q:fiesta,online_chips:mexican+fiesta&usg=AI4_-kQGU87DySQyv0Aqat3pdqhIpYYwjA&sa=X&ved=0ahUKEwjzjvL6lq7eAhWpTd8KHQ6-CIoQ4lYIKygE&biw=924&bih=639&dpr=1#imgrc=6H_w7py8kTIUHM:")
elif subject == "History":
    pg.alert ("In 1492 Christopher Columbus sailed the ocean blue")
    points += 3
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=history&rlz=1C1GCEA_enUS752US774&biw=1366&bih=657&tbm=isch&source=lnms&sa=X&ved=0ahUKEwiZ_YDvutHeAhXOVN8KHdEUDEkQ_AUICygC")
else:
    pg.alert ("cool")
    points += 1
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=school+gif&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjqpI_f_YreAhWsd98KHblYBY8Q_AUIDigB&biw=1366&bih=657#imgrc=kk5pi12VrUoKGM:")

food = pg.prompt ("What is your favorite food?").title()
if food == "Pizza":
    pg.alert ("Pizza Hut? Dominos?")
    points += 2
    t.sleep(2)
    wb.open ("https://cooking.nytimes.com/guides/1-how-to-make-pizza")
elif food == "Chocolate cake":
    pg.alert ("Now I want one")
    points += 9
    t.sleep(3)
    wb.open ("https://www.youtube.com/watch?v=dsJtgmAhFF4")
elif food == "Pasta":
    pg.alert ("I like pasta!")
    points += 3
    t.sleep(3)
    wb.open ("https://www.google.com/search?q=pasta&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiH_JXSlK7eAhWKT98KHScQASEQ_AUIDigB&biw=924&bih=639")
elif food == "Ice cream":
    pg.alert ("What kind? I like cookie monster.")
    points += 3
    t.sleep(2)
    wb.open("https://barefeetinthekitchen.com/homemade-ice-cream-recipe/")
elif food == "Fruit":
    pg.alert ("Refreshing!")
    points += 3
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=fruit&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijobOcla7eAhVyUt8KHfONDGUQ_AUIDigB&biw=924&bih=639#imgrc=ACrdFKwEzni-QM:")
elif food == "Chicken":
    pg.alert ("Yum!")
    points += 2
    t.sleep(2)
    wb.open ("https://www.google.com/search?q=chicken&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj59fTCutHeAhXLct8KHRV6D88Q_AUIEygB&biw=1366&bih=657")
else:
    pg.alert ("YUUMMM")
    points += 1
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=11HK5EuYwSk")

movie = pg.prompt ("What is your favorite movie series?").title()
if "Divergent" in movie:
    number = pg.prompt("Which movie is your favorite").title()

    if number == "1":
        pg.alert("Nice!")

ice_cream = pg.confirm("Which of these flavors is your favorite?", "Choose one", ["chocolate", "vanilla", "cookies and cream"])
if ice_cream == "cookies and cream":
    pg.alert("YES")

pg.alert ("Your final score is " + str(points))
