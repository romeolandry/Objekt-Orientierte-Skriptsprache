
import model
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class MyWindow(Gtk.Window):


    def __init__(self):
        identifiant = 1
        Gtk.Window.__init__(self, title="Mein Logbuch")
        Gtk.Window.set_default_size(self, 900, 450)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.box = Gtk.Grid()
        self.box.set_border_width(10)
        self.box.set_halign(Gtk.Align.CENTER)
        self.box.set_column_spacing(25)
        self.box.set_row_spacing(30)
        # self.box.add(Gtk.Label('Add a new information'))
        self.notebook.append_page(self.box, Gtk.Label('New'))

        self.button_save = Gtk.Button(label="Speichern")
        self.button_save.connect("clicked", self.on_button_save_clicked)

        self.label1 = Gtk.Label(label="Titel :")

        self.txttitel = Gtk.Entry()
        # self.set_default_size(, 250)

        self.label2 = Gtk.Label(label="Conten")
        self.journal = Gtk.TextView()
        self.journal = Gtk.TextView()
        self.journal.set_editable(True)
        self.journal.set_margin_left(10)
        self.journal.set_margin_right(10)
        self.journal.set_wrap_mode(True)
        self.journal.set_justification(Gtk.Justification.LEFT)
        self.journal.set_size_request(950, 250)


        self.box.add(self.label1)
        self.box.attach(self.txttitel, 1, 0, 2, 1)
        self.box.attach_next_to(self.label2, self.label1, Gtk.PositionType.BOTTOM, 1, 2)
        self.box.attach_next_to(self.journal, self.label2, Gtk.PositionType.RIGHT, 2, 1)
        self.box.attach(self.button_save, 1, 3, 2, 2)

        # zweite pane

        self.boxshow = Gtk.Grid()
        self.boxshow.set_border_width(10)
        self.boxshow.set_halign(Gtk.Align.CENTER)
        self.boxshow.set_column_spacing(25)
        self.boxshow.set_row_spacing(30)
        # self.box.add(Gtk.Label('Add a new information'))
        self.notebook.append_page(self.boxshow, Gtk.Label('Show'))

        self.label1 = Gtk.Label(label="selecte titel :")
        self.results = model.select_datein()

        name_store = Gtk.ListStore(str, str)
        name_store = self.results
        self.name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
        self.name_combo.connect("changed", self.on_name_combo_changed)
        self.name_combo.set_entry_text_column(0)
        self.label2 = Gtk.Label(label="Conten")
        self.journal = Gtk.TextView()
        self.journal.set_editable(False)
        self.journal.set_margin_left(10)
        self.journal.set_margin_right(10)
        self.journal.set_wrap_mode(True)
        self.journal.set_justification(Gtk.Justification.CENTER)
        self.journal.set_size_request(950, 250)
        #self.journal.set_indent(150)

        self.boxshow.add(self.label1)
        self.boxshow.attach(self.name_combo, 1, 0, 2, 1)
        self.boxshow.attach_next_to(self.label2, self.label1, Gtk.PositionType.BOTTOM, 1, 2)
        self.boxshow.attach_next_to(self.journal, self.label2, Gtk.PositionType.RIGHT, 2, 1)
        self.boxshow.attach(self.button_save, 1, 3, 2, 2)

    def on_button_save_clicked(self, widget):
        #buffertitle = self.box.get_child_at(1, 1).get_buffer()
        titel = self.box.get_child_at(2, 0).get_text()
        buffer = self.box.get_child_at(1, 1).get_buffer()
        journal = buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter(), include_hidden_chars=True)
        results = model.record(titel, journal)
        print(results)
        if results == 1:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, " ")
            dialog.format_secondary_text("Thank you")
            dialog.run()
            print("Info dialog Closed")

            dialog.destroy()

            titel = self.box.get_child_at(2, 0).set_text("")
            buffer = self.box.get_child_at(1, 1).get_buffer()
            buffer.set_text("")

        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Die Datein wurden nicht gespeichern !")
            dialog.format_secondary_text("Preufen Sie bitte das Conten Ihres Logbuchs")
            dialog.run()
            print("Info dialog Closed")

            dialog.destroy()
            # print(titel +" "+ ournal)

    def on_name_combo_changed(self, widget):
        # print (widget.get_active())
        indexItem = widget.get_active()

        if indexItem != None:
            model = widget.get_model()
            row_id, name = model[indexItem][:2]
            # print("Selected: " +row_id +" "+ name)

            buffer = self.boxshow.get_child_at(2, 1).get_buffer()
            buffer.set_text(name)
        else:
            entry = widget.get_child()
            # print("Entered: %s" % entry.get_text())

            # self.boxshow.get_child_at(2, 1).set_buffer(self.results[widget.get_active()])


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
