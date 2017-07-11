import model
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Gridpan")
        Gtk.Window.set_default_size(self, 400, 200)

        self.gridpane = Gtk.Grid()
        self.gridpane.set_halign(Gtk.Align.CENTER)
        self.gridpane.set_column_spacing(25)
        self.gridpane.set_row_spacing(30)
        self.add(self.gridpane)

        labelLogin = Gtk.Label(label="Login :")
        labelPwd = Gtk.Label(label="Password :")

        txtLogin = Gtk.Entry()
        txtLogin.set_text("")
        txtLogin.connect('key-press-event', self.add_tick_callback, 'Entry complet')

        txtpwd = Gtk.Entry()
        txtpwd.set_text("")
        txtpwd.set_visibility(False)
        txtpwd.connect('key-press-event', self.add_tick_callback, 'Entry complet')

        btLogin = Gtk.Button(label="Login")
        btLogin.connect("clicked", self.on_btLogin_clicked)

        self.gridpane.add(labelLogin)
        self.gridpane.attach(txtLogin, 1, 0, 2, 1)
        self.gridpane.attach_next_to(labelPwd, labelLogin, Gtk.PositionType.BOTTOM, 1, 2)
        self.gridpane.attach_next_to(txtpwd, labelPwd, Gtk.PositionType.RIGHT, 2, 1)
        self.gridpane.attach_next_to(btLogin, labelPwd, Gtk.PositionType.BOTTOM, 2, 1)

    def add_tick_callback(self, event, *args):  # args um felende argument zu speicher
        # print(event.get_text())
        login = event.get_text()
        if model.read_from_db_login(login):
            print ("correkt")

    def add_tick_callback(self, event, *args):
        # print(event.get_text())
        pwd = event.get_text()

    def on_btLogin_clicked(self, widget):
        #recuperation des entrees dans le grid
        print(self.gridpane.get_child_at(1, 0).get_text())
        print(self.gridpane.get_child_at(1, 1).get_text())

        login = self.gridpane.get_child_at(1, 0).get_text()
        pwd = self.gridpane.get_child_at(1, 1).get_text()

        results = model.login(login, pwd)
        if results:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "You are login")
            dialog.format_secondary_text("Thank you")
            dialog.run()
            print("Info dialog Closed")

            dialog.destroy()
            #Anruf des neuen Fenster
            win = GridWindow()
            win.close()

            import myLogbuch
        else :
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Login oder Password was not recognise !")
            dialog.format_secondary_text("Please try again")
            dialog.run()
            print("Info dialog Closed")

            dialog.destroy()


win = GridWindow()
win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()
