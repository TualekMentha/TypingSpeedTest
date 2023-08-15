from tkinter import *
from tkinter import messagebox
import random

# Colors
bgColor = '#BBD6B8'
titleColor = '#3f4739'
textColor = '#525E75'
textHit = '#AC4425'
textWT = '#483838'

# List of Words
words_list = ['computer', 'software', 'hardware', 'network', 'internet', 'website', 'database', 'programming',
              'algorithm', 'cybersecurity', 'encryption', 'firewall', 'malware', 'virus', 'server', 'cloud', 'data',
              'storage', 'virtualization', 'authentication', 'hacking', 'router', 'protocol', 'browser', 'application',
              'operating', 'system', 'debugging', 'mobile', 'analytics', 'artificial', 'intelligence', 'machine',
              'learning', 'blockchain', 'API', 'IoT', 'UX', 'UI', 'coding', 'scripting', 'serverless', 'agile',
              'frontend', 'backend', 'compiler', 'debugger', 'responsive', 'interface', 'integration', 'platform',
              'cloud', 'computing', 'open', 'source', 'cybersecurity', 'privacy', 'intrusion', 'network', 'topology',
              'bandwidth', 'protocol', 'vulnerability', 'exploit', 'firewall', 'authentication', 'encryption',
              'ransomware', 'phishing', 'spam', 'cookie', 'cache', 'algorithm', 'recursion', 'machine', 'code',
              'bug', 'version', 'control', 'CMS', 'SaaS', 'HTML', 'CSS', 'JavaScript', 'Python', 'Java', 'C++', 'Ruby',
              'SQL', 'PHP', 'DNS', 'URL', 'SSL', 'HTTPS', 'LAN', 'WAN', 'VPN', 'IP', 'address', 'subnet', 'cloud',
              'service', 'data', 'center', 'machine', 'code', 'framework', 'responsive', 'design', 'Docker', 'DevOps']

# Function
sliderWords = ''
i = 0
count_word = 0
oneMin = 60
correct_word = 0
incorrect_word = 0


def timer():
    global oneMin, i
    if oneMin > 0:
        oneMin -= 1
        timeCount_label.config(text=oneMin)
        timeCount_label.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        theResult = correct_word - incorrect_word
        instructionLabel.config(text=f'Correct Words {correct_word}\n Incorrect Words {incorrect_word} \n '
                                     f'Final Score {theResult}')
        if theResult < 15:
            emoji1Label.config(image=sadPic)
            emoji2Label.config(image=incorrectPic)
        if theResult > 15:
            emoji1Label.config(image=happyPic)
            emoji2Label.config(image=correctPic)
        result = messagebox.askyesno('Confirm', 'Do you want to test again?')
        if result:
            i = 0
            oneMin = 60
            countLabel.config(text=0)
            timeCount_label.config(text=oneMin)
            wordEntry.config(state=NORMAL)
            instructionLabel.config(text='Please! Type The Word And Hit Enter')
            emoji1Label.config(image='')
            emoji2Label.config(image='')


def start_testing(e):
    if wordEntry.get() != '':
        global count_word, correct_word, incorrect_word
        count_word += 1
        countLabel.config(text=count_word)
        instructionLabel.config(text='')
        if oneMin == 60:
            timer()

        if wordEntry.get() == wordList_label['text']:
            correct_word += 1
        else:
            incorrect_word += 1

        random.shuffle(words_list)
        wordList_label.config(text=words_list[0])
        wordEntry.delete(0, END)


def sliderText():
    global sliderWords, i
    text = 'Welcome to Typing Speed Test'
    if i >= len(text):
        i = 0
        sliderWords = ''
    sliderWords = sliderWords + text[i]
    titleLabel.config(text=sliderWords)
    i += 1
    titleLabel.after(200, sliderText)


# GUI Part
root = Tk()
root.title('Typing Speed Test By Siriluk')
root.iconbitmap('icon.ico')
root.geometry('900x800+400+50')
root.config(bg=bgColor)
root.resizable(0, 0)
logo = PhotoImage(file='logo.png')

logoLabel = Label(root, image=logo, bg=bgColor)
logoLabel.place(x=320, y=150)

titleLabel = Label(root, text='', bg=bgColor, font=('Helvetica', 30, 'bold'),
                   width=37, height=2, fg=titleColor)
titleLabel.place(x=0, y=20)
sliderText()
random.shuffle(words_list)
wordList_label = Label(root, text=words_list[0], font=('Comic Sans MS', 30, 'italic bold'), bg=bgColor, fg=textColor)
wordList_label.place(x=450, y=480, anchor=CENTER)

wordLabel = Label(root, text='Words', font=('Courier New', 35, 'bold'), bg=bgColor, fg=textWT)
wordLabel.place(x=90, y=220)

countLabel = Label(root, text='0', font=('Courier New', 35, 'bold'), bg=bgColor, fg=textWT)
countLabel.place(x=130, y=290)

timeLabel = Label(root, text='Timer', font=('Courier New', 35, 'bold'), bg=bgColor, fg=textWT)
timeLabel.place(x=670, y=220)

timeCount_label = Label(root, text='60', font=('Courier New', 35, 'bold'), bg=bgColor, fg=textWT)
timeCount_label.place(x=710, y=290)

wordEntry = Entry(root, font=('Helvetica', 30, 'bold'), bd=10, justify=CENTER, fg=textColor)
wordEntry.place(x=220, y=530)
wordEntry.focus_set()

instructionLabel = Label(root, text='Please! Type The Word And Hit Enter',
                         font=('Courier New', 20, 'bold'), bg=bgColor, fg=textHit)
instructionLabel.place(x=160, y=660)

happyPic = PhotoImage(file='happy.png')
sadPic = PhotoImage(file='sad.png')
correctPic = PhotoImage(file='correct.png')
incorrectPic = PhotoImage(file='incorrect.png')

emoji1Label = Label(root, bg=bgColor)
emoji1Label.place(x=90, y=525)
emoji2Label = Label(root, bg=bgColor)
emoji2Label.place(x=740, y=525)


root.bind('<Return>', start_testing)


root.mainloop()