from org.bukkit.event.player import PlayerJoinEvent, PlayerInteractEvent
from tech.rayline.core.util import ItemShorthand
from org.bukkit import Material
from util import config

@event_handler(PlayerJoinEvent)
def on_player_join(event):
    event.getPlayer().getInventory().setItem(0, ItemShorthand.withMaterial(Material.COMPASS).withName(color("&7&lServer Selector &7(Right Click)")).get())

@event_handler(PlayerInteractEvent)
def on_interact(event):
    if 'CLICK' not in event.getAction().name():
        return

    if not event.getPlayer().getHeldItemSlot() == 0:
        return

    event.getPlayer().performCommand("server")
