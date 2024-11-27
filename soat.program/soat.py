import time
for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            print(
                    f"Soat: {h:02}, Minut: {m:02}, Sekund: {s:02}", end='\r'
                )
            time.sleep(1)
