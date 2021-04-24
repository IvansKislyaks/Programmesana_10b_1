print("\n\nSveiki lietotajs,es esmu Ivans Kuznecovs-sportameistara kondidats un es palidzçðu uzturçt jusu sporta formu tonusâ' \n")
print("Kâd jûs atbildesiet uz jautâjumiem,cik jums vajag treneties nedela un kadi vingrinâjumi pildît.")


a=input(str("Grîbi sakt? (jâ/nç)\n"))
if a=="jâ":
    print("Sâksim ar pirmu jautâjumu")
elif a == "ne":
    print("Tad ej prom,ja nav vajadzigs tev")
else:
    print("Atbildi ja vai ne formata")
    
    
a=input(str("Cik edienreizes tev ir dienâ?(2/3)\n"))
if a=="2":
    print("loti slikti,vajag est 3-5 veselus edienus katru dienu")
if a=="3":
    print("viss ir kartiba,turpinat")

a=input(str("Cik jus treneties katra darba diena,uzraksti laiku VESELOS SKAITLOS-STUNDAS,pirmo virkni vajag izlaist ,videjais skaits treninu laika bus uzrakstits no taviem atbildiem? (laiks)\n"))
A=float(input("ievadi pirmo skaitli - "))
B=float(input("ievadi otro skaitli - "))
C=float(input("ievadi treso skaitli - "))
D=float(input("ievadi ceturto skaitli - "))
E=float(input("ievadi piekto skaitli - "))
Videjais = (A+B+C+D+E)/5
print(Videjais)
print("Ja ir vairak neka 1,1,tad jus esat malaci,ne-tad jums vajag but aktivak,jo viena stunda ir optimala visiem cilvekiem,ari parasta staigasana bus labi")


a=input(str("Cik stundas vajag treneties darba dienas,pajautat?"))
x= range(4, 10)
for n in x:
    print(n)
    

print("\n\nTas ir pedejajs jautajums,pec kura programma iedod saites kodu kuru vajag ievietot interneta,lai izpildit si vingrnajumi ' \n")
print("Cik jums ir gadi?")




a=int(input("10;"))
if a < 10:
    print(a,"https://ne-np.facebook.com/LATswimming/videos/vfs-peld%C4%93t%C4%81jiem-video-1-iesild%C4%AB%C5%A1an%C4%81s-vingrin%C4%81jumi/1323398607845848")
elif a > 18:
    print(a,"https://ne-np.facebook.com/LATswimming/videos/1333512360370744/?__so__=permalink&__rv__=related_videos")
    print("paldies,ka jus lietojat musu programmu")
else:
    print (a, "https://ne-np.facebook.com/LATswimming/videos/542628276662759/")
    print("Paldies,ka jus lietojat manu programmu")