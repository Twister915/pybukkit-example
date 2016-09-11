def get_lilypad_name():
    return pyb.Bukkit.getPluginManager().getPlugin("LilyPad-Connect").getConnect().getSettings().getUsername()
