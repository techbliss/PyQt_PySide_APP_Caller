This is a PyQt helper for Ida Pro

insteed of writing QT for ida pro like Hex-ray blog shows http://www.hexblog.com/?p=229

I always found that method to be very time consuming.

It's much easyer to write Qt and PySide apps via Qt designer.Then save as *.ui
then covert them pyuic4 -o test.py test.ui -x
remember to fix the code http://techbliss.org/threads/bringing-ida-pro-plugin-writing-into-2014.527/#post-1453

Now for the Plugin
Its make Use off calling Qtapps more easy.

You have to make a folder in your ida folder called QTApps so its idadir/QTApps
Put test.py in that folder.

Put Call_PyQt.py in plugin folder and run via edit/plugin/PyQt caller
this is the basic layout for calling QT and pyside apps, ones runned find the Qt app in the same
menu edit/plugin/call PyQt Plugin

It then calls the Test.py PyQt i made in this reposotery.
So all your Qt apps should go in this folder.

Regards storm


