from org.bukkit.event.player import PlayerJoinEvent

@event_handler(PlayerJoinEvent)
def player_join(arg):
    if arg.getPlayer().getName() == 'Twister':
        arg.getPlayer().sendMessage('test')
