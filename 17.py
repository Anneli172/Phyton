tehingute_arve = 0
tehingute_arve_pos = 0
pos_arv_summa = 0




with open("pangakonto.txt") as fail:
    sisu = fail.readlines()
    for number in sisu:
        #print(float(number))
        tehingute_arve+=1
        if float(number) > 0:
            tehingute_arve_pos+=1
            pos_arv_summa += float(number)

        print(f"Tehingute arv:{tehingute_arve}")
        print(f"Positiivsete tehingute arv:{tehingute_arve_pos}")
        print(f"Positiivsete arvude summa;{pos_arv_summa:-2f}")

