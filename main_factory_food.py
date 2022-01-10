""""""
import time
import lib.factory_class as fc
import lib.function as fun
import lib.defines as df
import threading

# import json
# import lib.gui as gui

fac = fc.Factory()
fac.need = {"wood": 2, "stone": 1}
fac.out = 10
fac.type = "food"
fac.name = "Food Factory"
fac.jf = "data/factory/food_factory.json"
fac.get_data()


def run(v1, v2):
    while True:
        fac.day_sub()
        print(fac.name,'  worker',fac.type )
        print('  '*7,'{:>5d} '.format(fac.worker),fac.int_to_str(),fac.count)
        print()


threading.Thread(target=run, args=("Thread----", 2)).start()
# threading.Thread(target=fac.app.mainloop, args=("Thread----", 2)).start()


fac.app.mainloop()
