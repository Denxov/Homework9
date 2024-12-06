def all_variants(text):
    i,ln=0,1
    while ln<=len(text):
        yield text[i:i+ln]
        i+=1
        if i+ln>len(text):
            i=0
            ln+=1

a = all_variants("abc")
for i in a:
    print(i)
