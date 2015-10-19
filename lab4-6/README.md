## Apartament bills manager

With this software you can track every bill from any apartament you want.

To compile this program you must download [WxPython]( http://www.wxpython.org/download.php) and then open ui.py, and compile.

Now you will see something like this

![Image](https://raw.githubusercontent.com/BoldijarPaul/python-labs/master/lab4-6/ss1.PNG)

The apartament number can only be greater than 0 and lower than 101.
The every other integer value must be in [0,10000]

### Features

* GUI - no more console stuff 
* you can add how many bills you want to up to 100 apartaments.
* you can view all apartaments with bills, and data about their bills as well
* you can choose the bill type by selecting it in the combobox dropdown.
* you can edit a bill by providing the bill id as well as the other fields that you want to change.
* you can delete all bills from a certain apartament, you set the id that you want.
* you can delete some certain bills from all apartaments. Let's say that we want to delete all bills that are for the water, from all apartaments. We can do that by only choosing which type we need.
* you can find out all apartaments with the cost (sum of all bills) greather than some provided number, you'll see a dialog with a list of items.




### Tehnical details

* used an MVC arhitecture ![MVC](https://raw.githubusercontent.com/BoldijarPaul/python-labs/master/lab4-6/mvc.png)
* Unit testing made using the [unittest](https://docs.python.org/2/library/unittest.html) framework from Python. Every method from the controller is tested.
* used GUI framework [WxPython]( http://www.wxpython.org)


[Requirements](https://raw.githubusercontent.com/BoldijarPaul/python-labs/master/lab4-6/requirements.PNG)



