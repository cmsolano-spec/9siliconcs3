year = int(input("Enter your birth year: ")) #blocks non integer inputs
if year < 1900:
  print("Invalid Year, it should not be earlier than 1900")
        
else:
  update = (year - 1900) % 12 #To get which year it is like the 1st year
  
  if update == 0:
      print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")

  elif update == 1:
          print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")
          
  elif update == 2:
          print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
          
  elif update == 3:
          print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
          
  elif update == 4:
          print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
          
  elif update == 5:
          print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
          
  elif update == 6:
          print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
          
  elif update == 7:
          print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
          
  elif update == 8:
          print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
          
  elif update == 9:
          print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
          
  elif update == 10:
          print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")

  elif update == 11:
          print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")
    
