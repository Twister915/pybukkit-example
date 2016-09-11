from org.bukkit.event.entity import FoodLevelChangeEvent

@event_handler(FoodLevelChangeEvent)
def on_food_change(event):
    event.getEntity().setFoodLevel(20)
    event.setCancelled(true)
