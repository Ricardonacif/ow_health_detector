from blinkstick import blinkstick

class Hero:
    def __init__(self):
        self.currentHealth = 200
        self.totalHealth = 200
        self.currentHealthState = 'full'
        self.light_green()
	




    def __str__(self):
        return "Hero stats: currentHealth: %s, totalHealth: %s, currentHealthState: %s" % (self.currentHealth, self.totalHealth, self.currentHealthState)


    def new_health_received(self, newHealth, newTotalHealth):
        if newHealth:
            self.currentHealth = newHealth
        if newTotalHealth:
            self.totalHealth = newTotalHealth
        percentage = self.classifyHealthPercentage(self.currentHealth, self.totalHealth)
        print(percentage)
        if percentage >= 70 and self.currentHealthState != 'full' :
            self.assign_new_health_state('full')
        elif percentage >= 30 and percentage < 70 and self.currentHealthState != 'half':
            self.assign_new_health_state('half')
        elif percentage < 30 and self.currentHealthState != 'low':
            self.assign_new_health_state('low')

    def classifyHealthPercentage(self, health, totalHealth):
        return 100 * float(health)/float(totalHealth)

    def assign_new_health_state(self, newState):
        self.currentHealthState = newState
        if self.currentHealthState == 'low':
            self.light_red()
        elif self.currentHealthState == 'half':
            self.light_yellow()
        else:
            self.light_green()

    def light_red(self ):
        bstick = blinkstick.find_first()
        for bstick in blinkstick.find_all():
            for x in xrange(1,60):
                bstick.set_color(channel=0, index=x, name="red")

    def light_green(self ):
        bstick = blinkstick.find_first()
        for bstick in blinkstick.find_all():
            for x in xrange(1,60):
                bstick.set_color(channel=0, index=x, name="green")

    def light_yellow(self ):
        bstick = blinkstick.find_first()
        for bstick in blinkstick.find_all():
            for x in xrange(1,60):
                bstick.set_color(channel=0, index=x, name="yellow")