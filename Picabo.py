from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

with open('Token.txt', 'r') as Token:
    TOKEN = Token.read()

updater = Updater(TOKEN,
        use_context=True)

# Start

def start(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
		"Hi there, I am Picaboo..!! 👻")
    time.sleep(1)
    update.message.reply_text(
		"I can help you with,\n\n✿ Textbooks\n✿ Notes\n✿ Assignments\n✿ Lab Manuals\n    ..... and many more..!!")
    time.sleep(1)
    update.message.reply_text(
		"Please, Select the Subject. 📚")
    time.sleep(1)
    update.message.reply_text(
    "Click on to 👉 /Select_a_Subject to Dive In ...")

def selecting_subject(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Subject :-\n\n ➜  /Physics - For Physics\n ➜  /Chemistry - For Chemistry\n ➜  /BEE - For BEE\n ➜  /BXE - For BXE\n ➜  /PPS - For PPS\n ➜  /Mechanics - For Mechanics\n ➜  /MathsII - For Maths-II\n ➜  /Graphics - For Graphics\n ➜  /More")

# Subjects

def physics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Physics_Textbook\n➜ /Physics_Notes\n➜ /Physics_Assignments\n➜ /Physics_LabManual")

def chemistry(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Chemistry_Textbook\n➜ /Chemistry_Notes\n➜ /Chemistry_Assignments\n➜ /Chemistry_LabManual")

def bee(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BEE_Textbook\n➜ /BEE_Notes\n➜ /BEE_Assignments\n➜ /BEE_LabManual")

def bxe(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BXE_Textbook\n➜ /BXE_Notes\n➜ /BXE_Assignments\n➜ /BXE_LabManual")

def pps(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /PPS_Textbook\n➜ /PPS_Notes\n➜ /PPS_Assignments\n➜ /PPS_LabManual")

def mechanics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Mechanics_Textbook\n➜ /Mechanics_Notes\n➜ /Mechanics_Assignments\n➜ /Mechanics_LabManual")

def maths_II(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /MathsII_Textbook\n➜ /MathsII_Notes\n➜ /MathsII_Assignments\n➜ /MathsII_LabManual")

def graphics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Graphics_Textbook\n➜ /Graphics_Notes\n➜ /Graphics_Assignments\n➜ /Graphics_LabManual")

def more(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Timetable\n➜ /Saturday_Timetable\n➜ /Prelims_Timetable\n➜ /EndSem_Timetable\n➜ /I_have_a_Suggestion") #/ERP_ID_List\n

# Content
# Physics

def physics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Physics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/8')

def physics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Physics Notes right now.")

def physics_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Physics Assignments right now.")

def physics_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Physics Lab Manual... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/18')

# Chemistry

def chemistry_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Chemistry Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/11')

def chemistry_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Chemistry Notes right now.")

def chemistry_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Chemistry Assignments right now.")

def chemistry_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Chemistry Lab Manual right now.")

# BEE

def bee_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BEE Textbook right now.")

def bee_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BEE Notes right now.")

def bee_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BEE Assignments right now.")

def bee_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BEE Lab Manual right now.")

# BXE

def bxe_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending BXE Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/9')

def bxe_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BXE Notes right now.")

def bxe_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Dear.., every division has different Assignments.")

def bxe_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have BXE Lab Manual right now.")


# PPS

def pps_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending PPS Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/12')

def pps_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending PPS Notes... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/25')

def pps_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have PPS Assignments right now.")

def pps_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have PPS Lab Manual right now.")

# Mechanics

def mechanics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Mechanics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/10')

def mechanics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Mechanics Notes right now.")

def mechanics_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Mechanics Assignments... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/20')

def mechanics_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Mechanics\nLab Manual... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/19')

# Maths-II

def mathsII_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Maths-II Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/14')

def mathsII_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Maths-II Notes right now.")

def mathsII_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Sorry Dear..., I don't have Maths-II Assignments right now.")

def mathsII_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Dude, does maths have lab manual..? 😂")

# Graphics

def graphics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Graphics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/13')

def graphics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Graphics चा कोण अभ्यास करतं... 🤦‍♂️😂")

def graphics_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Graphics ला Assignment असते... 🤔")

def graphics_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("First time in history pune university,\nI am listening about graphics lab manual, its horrrrrible. 😜😂")

# More

def timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Regular Timetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/21')

def q_div_regular_timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Q-Div\nRegular Timetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/23')
    
def saturday_timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Saturday's\nTimetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/22')

def prelims_timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Prelims's\nTimetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/47')

def endsem_timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending EndSem Timetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/48')

def erpID_list(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending ERP ID List... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/Picabooo_Bot/24')

def whatsapp_me(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
        "https://bit.ly/3RgXdkZ")

def unknown_text(update: Update, context: CallbackContext):
    time.sleep(0.5)
    update.message.reply_text(
        "I am still learning,\ngive me a valid input dear... 😊")

# #####

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Select_a_Subject', selecting_subject))

# Subjects

updater.dispatcher.add_handler(CommandHandler('Physics', physics))
updater.dispatcher.add_handler(CommandHandler('Chemistry', chemistry))
updater.dispatcher.add_handler(CommandHandler('BEE', bee))
updater.dispatcher.add_handler(CommandHandler('BXE', bxe))
updater.dispatcher.add_handler(CommandHandler('PPS', pps))
updater.dispatcher.add_handler(CommandHandler('Mechanics', mechanics))
updater.dispatcher.add_handler(CommandHandler('MathsII', maths_II))
updater.dispatcher.add_handler(CommandHandler('Graphics', graphics))
updater.dispatcher.add_handler(CommandHandler('More', more))

# Physics Content

updater.dispatcher.add_handler(CommandHandler('Physics_Textbook', physics_textbook))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes', physics_notes))
updater.dispatcher.add_handler(CommandHandler('Physics_Assignments', physics_assignments))
updater.dispatcher.add_handler(CommandHandler('Physics_LabManual', physics_labManual))

# Chemistry Content

updater.dispatcher.add_handler(CommandHandler('Chemistry_Textbook', chemistry_textbook))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes', chemistry_notes))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Assignments', chemistry_assignments))
updater.dispatcher.add_handler(CommandHandler('Chemistry_LabManual', chemistry_labManual))

# BEE Content

updater.dispatcher.add_handler(CommandHandler('BEE_Textbook', bee_textbook))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes', bee_notes))
updater.dispatcher.add_handler(CommandHandler('BEE_Assignments', bee_assignments))
updater.dispatcher.add_handler(CommandHandler('BEE_LabManual', bee_labManual))

# BXE Content

updater.dispatcher.add_handler(CommandHandler('BXE_Textbook', bxe_textbook))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes', bxe_notes))
updater.dispatcher.add_handler(CommandHandler('BXE_Assignments', bxe_assignments))
updater.dispatcher.add_handler(CommandHandler('BXE_LabManual', bxe_labManual))

# PPS Content

updater.dispatcher.add_handler(CommandHandler('PPS_Textbook', pps_textbook))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes', pps_notes))
updater.dispatcher.add_handler(CommandHandler('PPS_Assignments', pps_assignments))
updater.dispatcher.add_handler(CommandHandler('PPS_LabManual', pps_labManual))

# Mechanics Content

updater.dispatcher.add_handler(CommandHandler('Mechanics_Textbook', mechanics_textbook))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes', mechanics_notes))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Assignments', mechanics_assignments))
updater.dispatcher.add_handler(CommandHandler('Mechanics_LabManual', mechanics_labManual))

# Maths-II Content

updater.dispatcher.add_handler(CommandHandler('MathsII_Textbook', mathsII_textbook))
updater.dispatcher.add_handler(CommandHandler('MathsII_Notes', mathsII_notes))
updater.dispatcher.add_handler(CommandHandler('MathsII_Assignments', mathsII_assignments))
updater.dispatcher.add_handler(CommandHandler('MathsII_LabManual', mathsII_labManual))

# Graphics Content

updater.dispatcher.add_handler(CommandHandler('Graphics_Textbook', graphics_textbook))
updater.dispatcher.add_handler(CommandHandler('Graphics_Notes', graphics_notes))
updater.dispatcher.add_handler(CommandHandler('Graphics_Assignments', graphics_assignments))
updater.dispatcher.add_handler(CommandHandler('Graphics_LabManual', graphics_labManual))

# More Content

updater.dispatcher.add_handler(CommandHandler('Timetable', timetable))
updater.dispatcher.add_handler(CommandHandler('Q_Div_Timetable', q_div_regular_timetable))
updater.dispatcher.add_handler(CommandHandler('Saturday_Timetable', saturday_timetable))
updater.dispatcher.add_handler(CommandHandler('prelims_Timetable', prelims_timetable))
updater.dispatcher.add_handler(CommandHandler('EndSem_Timetable', endsem_timetable))
#updater.dispatcher.add_handler(CommandHandler('ERP_ID_List', erpID_list))
updater.dispatcher.add_handler(CommandHandler('I_have_a_Suggestion', whatsapp_me))

# Filters out unknown commands & messages.

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# updater.start_polling

updater.start_polling()

# A Special Thanks to Maansi & Sanket.
