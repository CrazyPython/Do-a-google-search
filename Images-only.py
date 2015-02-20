import webbrowser,os,time
print "Images-only.py"
print "Searches Google for Images."
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
items = int(raw_input("Max Items (0 for N/A): "))

clear()
if items == 0:
    items = 999999999999
items_far = 0




imp = raw_input("Import (nothing for nothing):")
if imp !="":
    try:
        l = eval(imp)
        items_far = items
    except SyntaxError as err:
        print "Bad syntax"
        raise
else:
    l = []
while items_far !=items:
    l.append(raw_input(str(items_far+1)+">"))
    items_far+=1

print "Enter your items."
clear()
for i in l:
    print "Opening "+i+"..."
    webbrowser.open_new_tab("https://www.google.com/search?q="+i+"&source=lnms&tbm=isch&sa=X&ei=MqjjVKbKCcKBgwSah4T4BQ&ved=0CAgQ_AUoAQ&biw=1440&bih=805")
    print "Sleeping..."
    time.sleep(0.3)
