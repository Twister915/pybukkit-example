from org.bukkit.event.player import PlayerChatTabCompleteEvent

@event_handler(PlayerChatTabCompleteEvent)
def on_tab_complete(event):
    if event.getPlayer.hasPermission('mcl.admin'):
        return

    if 'ver' in event.getMessage():
        event.setCancelled(True)
