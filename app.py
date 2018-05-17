import health_detector
import hero

if __name__ == "__main__":
  
    try:
        # get_health_numbers('output/251.png')
        i = 226
        myHero = hero.Hero()
        print(myHero)
        while True:
            # time.sleep(0.1)
            # im=ImageGrab.grab(bbox=(350,1205,475,1260)) # X1,Y1,X2,Y2
            # print(pyautogui.size()) 
            
            # im.show()
            # im.save("output/" + str(i) + '.png', 'PNG')
            health, totalHealth = health_detector.get_health_numbers()
            print("health:")
            print(str(health))
            print("totalhealth:")
            print(str(totalHealth))
            myHero.new_health_received(health, totalHealth)
            print(myHero)

            # print(i)
            i=i+1
    except KeyboardInterrupt:
        sys.exit()


#-#
