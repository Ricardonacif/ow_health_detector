import hero
import time
import health_detector


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""



def validate_image_with_filename(filename):
    print(filename)
    if ' ' in filename:
        health_string = find_between(filename, '\\', ' ')
    else:
        health_string = find_between(filename, '\\', '.')

    print("healthstring:")
    print(health_string)
    healths = health_string.split("#")
    img_current_health = healths[0]
    img_total_health = healths[1]
    print("filename:")
    print(img_current_health)
    print(img_total_health)
    det_health, det_total_health = health_detector.get_health_numbers(filename)
    print('detected:')
    print(det_health)
    print(det_total_health)
    if str(det_health) == img_current_health and img_total_health == str(det_total_health):
        return True
    else:
        return False

def percentage(part, whole):
  return 100 * float(part)/float(whole)

if __name__ == "__main__":
  
    try:
        # myHero = hero.Hero()
        # print(myHero)
        # # time.sleep(1)
        # # myHero.new_health_received(150, 200)
        # # print(myHero)

        # # # time.sleep(3)
        # # # print(myHero)


        # time.sleep(1)
        # myHero.new_health_received(30, 200)
        # print(myHero)

        # # time.sleep(1)
        # # myHero.new_health_received(200, 200)
        # # print(myHero)

        # time.sleep(1)
        # myHero.new_health_received(None, None)
        # print(myHero)


        # time.sleep(1)
        # myHero.new_health_received(100, None)
        # print(myHero)

        # time.sleep(1)
        # myHero.new_health_received(None, 600)
        # print(myHero)


        print("porra")
        print('-------')
        import glob
        correct = []
        incorrect = []
        for filename in glob.iglob('test_images/*.png'):
            valid = validate_image_with_filename(filename)
            print(valid)
            if valid:
                correct.append(filename)
            else:
                incorrect.append(filename)

        print("Final result:")
        print("Final result is: Positive: %s. Negative: %s ." % (len(correct), len(incorrect)))
        total_images = len(correct) + len(incorrect)
        print("Accuracy: %s" % (percentage(len(correct), total_images)))






    except KeyboardInterrupt:
        sys.exit()


#-#


