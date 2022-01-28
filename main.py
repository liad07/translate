import webbrowser

heb="https://translate.google.co.il/?hl=iw&sl=iw&tl=en&text="
eng="https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text="
rec="https://translate.google.co.il/?hl=iw&sl=auto&tl=iw&text="
var=input ('please select type eng/heb/idk \n')

amen=input ('please enter word \n')
if(var=="heb"):
    webbrowser.open(heb+amen+"&op=translate")
if(var=="eng"):
    webbrowser.open(eng+amen+"&op=translate")
if(var=="idk"):
    webbrowser.open(rec+ amen + "&op=translate")