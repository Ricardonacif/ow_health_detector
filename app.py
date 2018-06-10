import health_detector
import hero
import time
import sys

if __name__ == "__main__":
  
    try:
        myHero = hero.Hero()
        last_time = time.time()
        print(myHero)
        while True:
            health, totalHealth = health_detector.get_health_numbers()
            myHero.new_health_received(health, totalHealth)
            print(myHero)
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()

    except KeyboardInterrupt:
        sys.exit()
