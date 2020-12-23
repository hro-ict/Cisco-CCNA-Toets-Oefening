from easygui import *
import cisco2 as c
goed= 0
fout= 0
vraag= 0
overzicht=0
choices= ["A ","  B", "  C", "  D", "***INLEVEREN***"]
alle_vragen= []
vragen_images=[]
overzichten= []

msgbox(msg= "WELKOM\
\nCCNA Routing And Switching Oefentoets",image="images\home.gif")
def yes_no():
    percentage = round(100 / vraag) * goed
    tekst = "JE HEBT {} VAN {} VRAGEN GOED BEANTWOORD\n\nJOUW PERCENTAGE IS {}%\
            \n\n".format(goed, vraag,percentage )
    if percentage < 55:
        tekst= "{}\nJE BENT GEZAKT".format(tekst)
    else:
        tekst= tekst, "{}\nJE BENT GESLAAGD".format(tekst)
    c.image_maker("picture.gif", tekst)
    msgbox("", image="picture.gif")
    msgbox(msg= "BEDANKT EN TOT VOLGENDE KEER", image="images/seeyou.gif")
    exit()

def toets(vrmummer,juiste_antwoord):
    choices= ["A ","  B", "  C", "  D", "***INLEVEREN***"]
    global goed
    global fout
    global overzicht
    global vraag
    vraag += 1
    overzicht += 1

    button= buttonbox("KLIK OP (INLEVEREN) OM AF TE RONDEN", "VRAAG-{}".format(vrmummer),choices,image="images/v"+str(vrmummer)+".gif")

    if button== choices[4]:
       yes_no()
    elif button == juiste_antwoord:
        goed+=1
        msgbox("JE HEBT DEZE VRAAG GOED BEANTWOORD\n\n"
                           "JOUW ANTWOORD :{}\n\nJUISTE ANTWOORD :{}".format(button,button),
               image="images\o"+str(overzicht) + ".gif")

    else:
        fout+=1
        msgbox("JE HEBT DEZE VRAAG  FOUT BEANTWOORD\n\n"
               "\nJOUW ANTWOORD  : {}\n\nJUISTE ANTWOORD: {}".format(button,juiste_antwoord),image="images\o"+str(overzicht) + ".gif")

