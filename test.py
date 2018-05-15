import hero
import time
if __name__ == "__main__":
  
    try:
        myHero = hero.Hero()
        print(myHero)
        # time.sleep(1)
        # myHero.new_health_received(150, 200)
        # print(myHero)

        # # time.sleep(3)
        # # print(myHero)


        time.sleep(1)
        myHero.new_health_received(30, 200)
        print(myHero)

        # time.sleep(1)
        # myHero.new_health_received(200, 200)
        # print(myHero)

        time.sleep(1)
        myHero.new_health_received(None, None)
        print(myHero)


        time.sleep(1)
        myHero.new_health_received(100, None)
        print(myHero)

        time.sleep(1)
        myHero.new_health_received(None, 600)
        print(myHero)



    except KeyboardInterrupt:
        sys.exit()


#-#
