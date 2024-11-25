import screeninfo


monitors = screeninfo.get_monitors()

for monitor in monitors:
    print(monitor.name)
    print(monitor.height)