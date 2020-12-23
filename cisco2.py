from PIL import Image, ImageDraw, ImageFont
from easygui import *





goed= 0
fout= 0
vraag= 0
overzicht=0
choices= ["A ","  B", "  C", "  D", "***INLEVEREN***"]
alle_vragen= []
vragen_images=[]
overzichten= []
msgbox(msg= "WELKOM CCNA Routing And Switching Exam",image="images\home.gif")

def image_maker(file, tekst):
    img = Image.new('RGB', (600, 320), color=("yellow"))
    fnt = ImageFont.truetype('CALIBRI.ttf', 25)
    d = ImageDraw.Draw(img)
    d.text((70, 25), tekst, font=fnt, fill="blue")
    # d.text((300, 47), tekst2, font=fnt, fill="red")
    # d.text((70, 20), tekst3, font=fnt, fill="green")
    # d.text((70, 310), tekst4, font=fnt, fill="purple")

    img.save(file)
def yes_no():
    percentage = round(100 / vraag) * goed
    tekst= "\nJE HEBT {} VAN {} VRAGEN GOED BEANTWOORD\n\nJOUW PERCENTAGE IS {}%\
        \n\nWIL JE INZAGE DOEN?".format(goed,vraag,round(100 / vraag) * goed)
    if percentage < 55:
        tekst= "HELAAS \nJE BENT GEZAKT\n{}\n".format(tekst)
    else:
        tekst= "GEOD ZO!\nJE BENT GESLAAGD\n{}\n".format(tekst)

    image_maker("images/V37.GIF",tekst)
    yn= ynbox("",image="images/picture.gif")
    if yn == True:
        overzicht_vragen()
        msgbox(msg= "BEDANKT EN TOT VOLGENDE KEER", image="images/seeyou.gif")
        exit()
    else:
        msgbox(msg= "BEDANKT EN TOT VOLGENDE KEER",image= "images/seeyou.gif")
        exit()
def overzicht_vragen():
    vrnummer= 0
    for x in range(len(alle_vragen)):
        vrnummer+=1
        msgbox(title= "INZAGE VAN VRAAG-{}".format(vrnummer),image=overzichten[x], msg=alle_vragen[x])
def toets(vrmummer,juiste_antwoord):
    choices= ["A ","  B", "  C", "  D", "***INLEVEREN***"]
    global goed
    global fout
    global overzicht
    global vraag
    vraag += 1
    overzicht += 1
    button= buttonbox("KLIK OP (INLEVEREN) OM AF TE RONDEN", "VRAAG-{}".format(vrmummer),choices,  image="images/v"+str(vrmummer)+".gif")
    if button== choices[4]:
       yes_no()
    elif button == juiste_antwoord:
        goed+=1
        alle_vragen.append("JE HEBT DEZE VRAAG GOED BEANTWOORD\n\n"
                           "JOUW ANTWOORD :{}\n\nJUISTE ANTWOORD :{}".format(button,button))
        overzichten.append("images\o"+str(overzicht) + ".gif")

    else:
        fout+=1
        alle_vragen.append("JE HEBT DEZE VRAAG  FOUT BEANTWOORD\n\n"
                           "JOUW ANTWOORD  : {}\n\nJUISTE ANTWOORD: {}".format(button, juiste_antwoord))
        overzichten.append("images\o"+str(overzicht)+".gif")


