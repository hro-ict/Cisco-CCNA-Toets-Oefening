from easygui import *
enter= enterbox(msg= "WAT IS JE NAAM?", image= "images/home2.gif")
choices= ["GELIJK INZAGE ", "INZAGE NA HET AFRONDEN"]
button= buttonbox(msg= "WELKOM {}\
\n\nALS JE NA ELKE VRAAG INZAGE WIL DOEN,\
\nKLIK OP (GELIJK INZAGE)\
\n\nALS JE NA HET AFRONDEN WIL INZAGE DOEN\
\nKLIK DAN OP (INZAGE NA HET AFRONDEN)".format(enter)
            , choices= ["GELIJK INZAGE ", "INZAGE NA HET AFRONDEN"],image="images/home2.gif")

if button == choices[0]:
    import met_inzage as c
else:
    import cisco2 as c
choices= ["A ","  B", "  C", "  D", "***INLEVEREN***"]
c.toets(1,choices[1])
c.toets(2,choices[1])
c.toets(3,choices[1])
c.toets(4,choices[0])
c.toets(5,choices[2])
c.toets(6,choices[3])
c.toets(7,choices[1])
c.toets(8,choices[3])
c.toets(9,choices[0])
c.toets(10,choices[3])
c.toets(11,choices[2])
c.toets(12,choices[3])
c.toets(13,choices[1])
c.toets(14,choices[2])
c.toets(15,choices[0])
c.toets(16,choices[2])
c.toets(17,choices[0])
c.toets(18,choices[1])
c.toets(19,choices[2])
c.toets(20,choices[3])
c.toets(21,choices[0])
c.toets(22,choices[3])
c.toets(23,choices[1])
c.toets(24,choices[3])
c.toets(25,choices[2])
c.toets(26,choices[3])
c.toets(27,choices[2])
c.toets(28,choices[0])
c.toets(29,choices[2])
c.toets(30,choices[2])
c.toets(31,choices[0])
c.toets(32,choices[1])
c.toets(33,choices[2])
c.toets(34,choices[2])
c.toets(35,choices[2])
c.toets(36,choices[1])
c.toets(37,choices[3])
c.toets(38,choices[1])
c.toets(39,choices[1])
c.toets(40,choices[2])
c.toets(41,choices[3])
c.toets(42,choices[1])
c.toets(43,choices[3])
c.toets(44,choices[3])
c.yes_no()
c.overzicht_vragen()
