import gettext
import gtk.glade
import prefix

APP='apertium-tolk'
DIR=prefix.localedir
 
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)
gtk.glade.bindtextdomain(APP, DIR)
gtk.glade.textdomain(APP)

_ = gettext.gettext # the i18n function :)

