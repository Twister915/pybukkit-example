from org.bukkit.event.player import PlayerInteractEvent
from org.bukkit.util import Vector
from org.bukkit import Sound
from tech.rayline.core.util import RunnableShorthand
from rx.functions import Action0

print 'init bouncy pads'

in_progress = []

class Ticker(Action0):
    def __init__(self, event):
        self.start_location = event.getPlayer().getLocation()
        self.player = event.getPlayer()
        self.time_left = 3 #means 2

        self.call()

    def call(self):
        if self.player.getName() in in_progress:
            in_progress.remove(self.player.getName())
        self.time_left = self.time_left - 1
        if not self.check():
            return
        if self.time_left == 0:
            self.go()
        else:
            self.schedule()

    def schedule(self):
        in_progress.append(self.player.getName())
        self.player.playSound(self.player.getLocation(), Sound.CLICK, 20, 1)
        pyb.scheduler.scheduleSync(self, '1 seconds')

    def go(self):
        self.player.setVelocity(Vector(0, 6, 0))
        self.player.playSound(self.player.getLocation(), Sound.BAT_TAKEOFF, 20, 1)
        self.player.sendMessage(color('&7Woosh...'))

    def check(self):
        return self.player.isOnline() and self.player.getLocation().distanceSquared(self.start_location) < 2

@event_handler(PlayerInteractEvent)
def on_player_interact(event):
    if not event.getAction().name() == 'PHYSICAL':
        return

    block = event.getClickedBlock()
    if block is None or not block.getType().name() == 'STONE_PLATE':
        return

    if event.getPlayer().getName() in in_progress:
        return

    Ticker(event)
    event.setCancelled(True)
