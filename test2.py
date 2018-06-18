import hero
import time
import health_detector
import glob
import sys

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
        health_string = find_between(filename, '/', ' ')
    else:
        health_string = find_between(filename, '/', '.')

    print("healthstring:")
    print(health_string)
    healths = health_string.split("#")
    print(healths)
    img_current_health = healths[0]
    img_total_health = healths[1]
    print("filename:")
    print(img_current_health)
    print(img_total_health)
    det_health, det_total_health = health_detector.get_health_numbers(filename)
    print('detected:')
    print(det_health)
    print(det_total_health)
    if det_health is not None and det_total_health is not None:
        if str(det_health) == img_current_health and img_total_health == str(det_total_health):
            return 'values_match'
        else:
            return 'values_doesnt_match'
    else:
        return 'cant_read'



def percentage(part, whole):
  return 100 * float(part)/float(whole)

if __name__ == "__main__":
  
    try:
        values_match = []
        values_doesnt_match = []
        cant_read = []
        wrong_values = ['test_images/0#600 (37).png',
            # 'test_images/489#600 (4).png',
            # 'test_images/443#600 (10).png',
            # 'test_images/484#600.png',
            # 'test_images/469#600.png',
            # 'test_images/324#600.png',
            # 'test_images/0#600 (30).png'
            ]
        for filename in wrong_values:
            result = validate_image_with_filename(filename)
            print(result)
            if result == 'values_match':
                values_match.append(filename)
            elif result == 'values_doesnt_match':
                values_doesnt_match.append(filename)
            else:
                cant_read.append(filename)
        print("---------------------\n")
        print("Final result is:")
        print("values_match: %s." % (len(values_match)))
        print("values_doesnt_match: %s." % (len(values_doesnt_match)))
        print("cant_read: %s." % (len(cant_read)))
        # print("Final result is: Positive: %s. Negative: %s ." % (len(correct), len(incorrect)))
        # print("Final result is: Positive: %s. Negative: %s ." % (len(correct), len(incorrect)))
        # print()
        total_images = len(values_match) + len(values_doesnt_match) + len(cant_read)
        incorrect = len(values_doesnt_match) + len(cant_read)
        print("Accuracy: %s" % (percentage(len(values_match), total_images)))
        readables_total = len(values_match) + len(values_doesnt_match)
        print("Accuracy ignoring cant read: %s" % (percentage(len(values_match), readables_total)))

    except KeyboardInterrupt:
        sys.exit()
