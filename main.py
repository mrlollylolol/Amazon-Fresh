from tkinter import *
import os
root = Tk()
root.title("Amazon Fresh")
root.maxsize(1366, 728)
root.minsize(1366, 768)
root.configure(background="WHITE")
root.state("zoomed")
fnt = ("Amazon Ember", 30, "bold")
# name: 0   Cost: 1     amt:2      quantity type:3
items = [[["onion", 50, 1, "kg"], ["Carrot", 50, 1, "kg"], ["potato", 50, 1, "kg"], ["radish", 50, 1, "kg"], ["cabbage", 50, 1, "kg"], ["tomato", 50, 1, "kg"]],
         [["eggplant", 70, 1, "kg"], ["Bitter Gourd", 90, 1, "kg"], ["lady finger", 60, 1, "kg"], ["capsicum", 70, .250, "kg"], ["eggs", 50, 1, "dozen"], ["bread", 35, 1, "pack"]],
         [['cauliflower', 40, 1, "piece"], ['lettuce', 50, 1, "piece"], ['broccoli', 100, .250, "kg"], ['Corn', 50, 1, "piece"], ['Milk', 66, .250, "litre"], ['Sugar', 50, 1, "kg"]],
         [['beetroot', 70, 1, "kg"], ['cheese', 50, 1, "pack"], ['butter', 40, 1, "pack"], ['honey', 50, .250, "litre"], ['pepper', 20, .250, "kg"], ['coconutmilk', 50, .250, "litre"]],
         [['almonds', 60, .500, "kg"], ['coconutoil', 30, 1, "litre"], ['jaggery', 60, 1, "kg"], ['coconutwater', 30, 1, "litre"], ["cocoapowder", 50, .500, "kg"], ['curd', 25, .250, "litre"]],
         [['greentea', 30, 1, "pack"], ['jaggerypowder', 50, 1, "kg"], ['salt', 10, 1, "kg"], ['tamarind', 80, .250, "kg"], ["peanutbutter", 50, .250, "litre"], ['ghee', 100, .250, "litre"]]]



search_items = [[["onion", 1], ["carrot", 1], ["potato", 1], ["radish", 1], ["cabbage", 1], ["tomato", 1],
                 ["eggplant", 2], ["bitter gourd", 2], ["lady finger", 2], ["capsicum", 2], ["eggs", 2], ["bread", 2],
                 ["cauliflower", 3], ["lettuce", 3], ["broccoli", 3], ["corn", 3], ["milk", 3], ["sugar", 3],
                 ["beetroot", 4], ["cheese", 4], ["butter", 4], ["honey", 4], ["pepper", 4], ["coconut milk", 4],
                 ["almonds", 5], ["coconut oil", 5], ["jaggery", 5], ["coconut water", 5], ["cocoa powder", 5], ["curd", 5],
                 ["green tea", 6], ["jaggery powder", 6], ["salt", 6], ["tamarind", 6], ["peanut butter", 6], ["ghee", 6]], 

                ["onion", "carrots", "potato", "radish", "cabbage", "tomato", "eggplant", "bitter gourd", "ladyfinger", "capsicum", "cauliflower", "lettuce", "broccoli", "corn", "beetroot"],

                ["milk", "cheese", "butter", "curd", "ghee"],

                ["pepper", "salt", "tamarind"],
                
                ["egg", "bread", 'sugar', 'honey', 'coconutmilk', 'almonds', 'coconutoil', 'jaggery', 'coconut water', "cocoapowder", 'greentea', 'jaggerypowder', "peanutbutter"]]


screen = 1


def screen_change(mode):
    global screen
    global pics

    if mode == "next":
        if screen == 1:
            screen_prev_button["state"] = "active"
        elif screen == 5:
            screen_next_button["state"] = "disabled"
        screen += 1

    elif mode == "prev":
        if screen == 6:
            screen_next_button["state"] = "active"
        elif screen == 2:
            screen_prev_button["state"] = "disabled"
        screen -= 1

    pics = [PhotoImage(file=f"images/{items[screen-1][0][0]}.png"),
            PhotoImage(file=f"images/{items[screen-1][1][0]}.png"),
            PhotoImage(file=f"images/{items[screen-1][2][0]}.png"),
            PhotoImage(file=f"images/{items[screen-1][3][0]}.png"),
            PhotoImage(file=f"images/{items[screen-1][4][0]}.png"),
            PhotoImage(file=f"images/{items[screen-1][5][0]}.png"),
            PhotoImage(file="images/back.PNG"),
            PhotoImage(file="images/search.png")]

    button_1["image"] = pics[0]
    button_2["image"] = pics[1]
    button_3["image"] = pics[2]
    button_4["image"] = pics[3]
    button_5["image"] = pics[4]
    button_6["image"] = pics[5]
    search_button["image"] = pics[7]


def item_desc_screen(item_no):
    global item_image
    global item_button
    global item_increase_button
    global item_quantity
    global item_decrease_button
    global item_purchase_button
    global add_to_cart_button
    global back_button
    global quantity
    global screen
    global item_price
    global price
    global message_label

    if message_label["text"] != "":
        message_label.config(text="")


    quantity = items[screen-1][item_no-1][2]
    quantity_type = items[screen - 1][item_no - 1][3]
    price = quantity * items[screen - 1][item_no - 1][1]
    item = items[screen-1][item_no-1][0]
    item_image = PhotoImage(file=f"images/{items[screen-1][item_no-1][0]}_image.png")
    back_button = Button(root, image=pics[6], borderwidth=0, highlightthickness=0, background="WHITE",command=lambda: back("menu"))
    item_name["text"] = f"{items[screen - 1][item_no - 1][0]}".capitalize()
    item_quantity["text"] = f"{quantity} {quantity_type}"
    item_price["text"] = f"{quantity * items[screen - 1][item_no - 1][1]}"
    item_purchase_button = Button(frame_item_desc_screen,  text="Purchase $$$", borderwidth=0, highlightthickness=0, font=fnt, background="Green", activebackground="Yellow", command=lambda: purchase("not cart", item, quantity, price))
    add_to_cart_button = Button(frame_item_desc_screen,  text="Add to cart ", borderwidth=0, highlightthickness=0, font=fnt, background="dark turquoise", command= lambda: add_to_cart(username_, item, quantity, quantity_type, price))
    item_increase_button = Button(frame_item_desc_screen, text="+", borderwidth=0, highlightthickness=0, font=fnt, background="WHITE", activebackground="WHITE",command=lambda: quantity_change("add", item_no, quantity))
    item_decrease_button = Button(frame_item_desc_screen, text="-", borderwidth=0, highlightthickness=0, font=fnt, background="WHITE", activebackground="WHITE", command=lambda: quantity_change("subtract", item_no, quantity))
    item_button["image"] = item_image

    frame_main.place_forget()
    frame_item_desc_screen.place(relx=.60, rely=.5, anchor=CENTER)


    back_button.place(anchor=NW)
    item_button.place(relx=.15, rely=.5, anchor=CENTER)

    item_name.grid(row=0, column=1)
    item_increase_button.grid(row=1, column=0)
    item_quantity.grid(row=1, column=1, padx=100)
    item_decrease_button.grid(row=1, column=2)
    item_purchase_button.grid(row=2, column=2, columnspan=5, pady=20)
    add_to_cart_button.grid(row=3, column=2, columnspan=5, pady=20)
    item_price.grid(row=3, column=1)
    message_label.grid(row=4, column=1, columnspan=50, pady=20)


def back(mode):
    global back_button
    global no_of_items_in_cart_label

    if mode == "menu":
        frame_item_desc_screen.place_forget()

        for i in frame_item_desc_screen.winfo_children():
            i.grid_remove()

        back_button.place_forget()
        item_button.place_forget()

        fh = open(f"users/{username_}.txt", "r+")
        fh.seek(6)
        data = fh.read()
        items_in_cart = data.split()
        
        if len(items_in_cart)//4 == 0:
            check_out_button.config(state="disabled")
        else:
            check_out_button.config(state="normal")

        frame_main.place(relx=.5, rely=.5, anchor=CENTER)
        no_of_items_in_cart_label.grid_remove()
        no_of_items_in_cart_label.config(text=f"No. of items in cart: {len(items_in_cart)//4}")
        fh.close()

        no_of_items_in_cart_label.grid(row=0, column=2, pady=25)

    elif mode == "purchase":
        frame_purchase.place_forget()
        for i in frame_purchase.winfo_children():
            i.grid_remove()
        
        frame_item_desc_screen.place(relx=.60, rely=.5, anchor=CENTER)
        back_button = Button(root, image=pics[6], borderwidth=0, highlightthickness=0, background="WHITE",command=lambda: back("menu"))
        back_button.place(anchor=NW)
        item_button.place(relx=.15, rely=.5, anchor=CENTER)
        item_name.grid(row=0, column=1)
        item_increase_button.grid(row=1, column=0)
        item_quantity.grid(row=1, column=1, padx=100)
        item_decrease_button.grid(row=1, column=2)
        item_purchase_button.grid(row=2, column=2, columnspan=5, pady=20)
        add_to_cart_button.grid(row=3, column=2, columnspan=5, pady=20)
        item_price.grid(row=3, column=1)

    elif mode == "check out":
        back_button.grid_remove()
        frame_purchase.place_forget()
        frame_check_out.place_forget()

        fh = open(f"users/{username_}.txt", "r+")
        fh.seek(6)
        data = fh.read()
        items_in_cart = data.split()
        
        if len(items_in_cart)//4 == 0:
            check_out_button.config(state="disabled")
        else:
            check_out_button.config(state="normal")

        frame_main.place(relx=.5, rely=.5, anchor=CENTER)
        no_of_items_in_cart_label.config(text=f"No. of items in cart: {len(items_in_cart)//4}")
        fh.close()

        no_of_items_in_cart_label.grid(row=0, column=2, pady=25)

def quantity_change(mode, item_no, qty):
    global item_quantity
    global item_price
    global quantity
    global price
    if mode == "add" and qty < 5:
        quantity = qty + items[screen-1][item_no-1][2]

    elif mode == "subtract" and qty > 1:
        quantity = qty - items[screen-1][item_no-1][2]
    item_quantity["text"] = f"{quantity} {items[screen-1][item_no-1][3]}"
    item_price["text"] = f"{quantity * items[screen-1][item_no-1][1]}"

    price = quantity * items[screen - 1][item_no - 1][1]


def purchase(mode, item, quantity, price):
    global back_button
    frame_purchase.place(relx=.5, rely=.5, anchor=CENTER)
    
    if mode == "not cart":
        frame_item_desc_screen.place_forget()
        back_button.place_forget()
        item_button.place_forget()

        thank_you_label = Label(frame_purchase, text=f"Thank you for purchasing {quantity} of {item} the cost will be:\n₹{price}", font=fnt, background="WHITE")
        back_button = Button(frame_purchase, text="Back to item screen", font=fnt, borderwidth=0, highlightthickness=0, background="WHITE",command=lambda: back("purchase"))
        quit_button = Button(frame_purchase, text="Quit", font=fnt, borderwidth=0, highlightthickness=0, background="WHITE",command=quit)
    elif mode == "cart":

        back_button.grid_forget()
        fh = open(f"users/{username_}.txt", "r+")
        data = fh.read(6)
        fh.close()
        fh = open(f"users/{username_}.txt", "w")
        fh.write(f"{data}\n")
        fh.close()

        frame_check_out.place_forget()

        thank_you_label = Label(frame_purchase, text=f"Thank you for purchasing pur products the total will be\n₹{price}", font=fnt, background="WHITE")
        back_button = Button(frame_purchase, text="Back to main menu", font=fnt, borderwidth=0, highlightthickness=0, background="WHITE",command=lambda: back("check out"))
        quit_button = Button(frame_purchase, text="Quit", font=fnt, borderwidth=0, highlightthickness=0, background="WHITE",command=quit)

    thank_you_label.grid(row=0, column=0, columnspan=2, pady=50)
    back_button.grid(row=1, column=0)
    quit_button.grid(row=1, column=1)

def login(username, password):
    global username_
    global password_
    if os.path.exists(f"users/{username}.txt"):
        fh = open(f"users/{username}.txt", "r+")
        data = fh.read(6)
        real_password = data
        if password == real_password:
            fh = open(f"users/{username}.txt", "r+")
            fh.seek(6)
            data = fh.read()
            fh = open(f"users/{username}.txt", "r+")
            fh.seek(6)
            data = fh.read()
            items_in_cart = data.split()
            username_label = Label(frame_main, text=f"User: {username}", font=("Amazon Ember", 20, "bold"), background="WHITE")
            no_of_items_in_cart_label = Label(frame_main, text=f"No. of items in cart: {len(items_in_cart)//4}", font=("Amazon Ember", 20, "bold"), background="WHITE")
            fh.close()

            if len(items_in_cart)//4 == 0:
                check_out_button.config(state="disabled")
            else:
                check_out_button.config(state="normal")

            username_ = username
            password_ = password

            frame_login.place_forget()

            frame_main.place(relx=.5, rely=.5, anchor=CENTER)
            username_label.grid(row=0, column=0, pady=25)
            no_of_items_in_cart_label.grid(row=0, column=2, pady=25)
            button_1.grid(row=1, column=0, padx=80, pady=25)
            button_2.grid(row=1, column=1, padx=80, pady=25)
            button_3.grid(row=1, column=2, padx=80, pady=25)
            button_4.grid(row=2, column=0, padx=80, pady=25)
            button_5.grid(row=2, column=1, padx=80, pady=25)
            button_6.grid(row=2, column=2, padx=80, pady=25)
            screen_next_button.grid(row=3, column=1, columnspan=2, padx=20)
            screen_prev_button.grid(row=3, column=0, columnspan=2, padx=20)
            check_out_button.grid(row=3, column=2, padx=20)
            search_button.grid(row=3, column=0)

def signup(username, password):
    if not os.path.exists(f"users/{username}.txt") and len(password) == 6:
        fh=open(f"users/{username}.txt", "w+")
        fh.write(f"{password} \n")
        fh.close()
    elif len(password) != 6:
        message_label1.config(text="Password should contain at least 6 characters.")

def character_limit(entry_text):
    if len(entry_text.get()) > 6:
        entry_text.set(entry_text.get()[:6])

def add_to_cart(username, item, quantity, quantity_type, price):
    global no_of_items_in_cart_label
    global no_of_items_in_cart
    global message_label
    fh = open(f"users/{username}.txt", "r+")
    fh.seek(6)
    data = fh.read()
    items_in_cart = data.split()
    if item not in items_in_cart and (len(items_in_cart)//4) < 5:
        fh.write(f"{item} {quantity} {quantity_type} {price} ")
    elif len(items_in_cart)//4 == 0:
        fh.write(f"\n{item} {quantity} {quantity_type} {price} ")
    elif item in items_in_cart:
        message_label.config(text="Item is already in your cart")
    elif item not in items_in_cart and len(items_in_cart)//4 >= 5:
        message_label.config(text="The maximum number of items that can\nbe in the cart has been reached.")
    fh.close()
    fh = open(f"users/{username}.txt", "r+")
    fh.seek(6)
    data = fh.read()
    items_in_cart = data.split()
    no_of_items_in_cart_label = Label(frame_main, text=f"No. of items in cart: {len(items_in_cart)//4}", font=("Amazon Ember", 20, "bold"), background="WHITE")
    fh.close()

def check_out():
    global back_button
    frame_main.place_forget()

    item_name_label = Label(frame_check_out, text="Item Name", font=("Amazon Ember", 20, "bold"), background="WHITE")
    item_quantity_label = Label(frame_check_out, text="Quantity", font=("Amazon Ember", 20, "bold"), background="WHITE")
    item_price_label = Label(frame_check_out, text="Price", font=("Amazon Ember", 20, "bold"), background="WHITE")

    cart_item_1 = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_1_qty = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_1_price = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    cart_item_2 = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_2_qty = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_2_price = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    cart_item_3 = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_3_qty = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_3_price = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    cart_item_4 = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_4_qty = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_4_price = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    cart_item_5 = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_5_qty = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_item_5_price = Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    total = 0
    total_label = Label(frame_check_out, text="Total:", font=("Amazon Ember", 20, "bold"), background="WHITE")
    cart_total_price= Label(frame_check_out, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

    fh = open(f"users/{username_}.txt", "r+")
    fh.seek(6)
    data = fh.read()
    items_in_cart = data.split()

    if len(items_in_cart)//4 > 0 :
        cart_item_1.config(text=items_in_cart[0].capitalize())
        cart_item_1_qty.config(text=f"{items_in_cart[1]}{items_in_cart[2]}")
        cart_item_1_price.config(text=items_in_cart[3])
        total = float(items_in_cart[3])

    if len(items_in_cart)//4 > 1:
        cart_item_2.config(text=items_in_cart[4].capitalize())
        cart_item_2_qty.config(text=f"{items_in_cart[5]}{items_in_cart[6]}")
        cart_item_2_price.config(text=items_in_cart[7])
        total = float(items_in_cart[3]) + float(items_in_cart[7]) 

    if len(items_in_cart)//4 > 2:
        cart_item_3.config(text=items_in_cart[8].capitalize())
        cart_item_3_qty.config(text=f"{items_in_cart[9]}{items_in_cart[10]}")
        cart_item_3_price.config(text=items_in_cart[11])
        total = float(items_in_cart[3]) + float(items_in_cart[7]) + float(items_in_cart[11])
    
    if len(items_in_cart)//4 > 3:
        cart_item_4.config(text=items_in_cart[12].capitalize())
        cart_item_4_qty.config(text=f"{items_in_cart[13]}{items_in_cart[14]}")
        cart_item_4_price.config(text=items_in_cart[15])
        total = float(items_in_cart[3]) + float(items_in_cart[7]) + float(items_in_cart[11]) + float(items_in_cart[15])

    if len(items_in_cart)//4 > 4:
        cart_item_5.config(text=items_in_cart[16].capitalize())
        cart_item_5_qty.config(text=f"{items_in_cart[17]}{items_in_cart[18]}")
        cart_item_5_price.config(text=items_in_cart[19])
        total = float(items_in_cart[3]) + float(items_in_cart[7]) + float(items_in_cart[11]) + float(items_in_cart[15]) + float(items_in_cart[19])
    
    buy_now_button = Button(frame_check_out, text="Buy", foreground="blue", font=("Amazon Ember", 20, "bold"), borderwidth=0, highlightthickness=0, background="WHITE", command=lambda: purchase("cart", 0, 0, total))

    cart_total_price.config(text=total)  
    fh.close()

    back_button = Button(root, image=pics[6], borderwidth=0, highlightthickness=0, background="WHITE",command=lambda: back("check out"))

    for i in frame_check_out.winfo_children():
        i.grid_remove()

    back_button.grid(row=0, column=0)
    frame_check_out.place(relx=.5, rely=.5, anchor=CENTER)

    item_name_label.grid(row=0, column=0)
    item_quantity_label.grid(row=0, column=1, padx=500, pady=25)
    item_price_label.grid(row=0, column=2)

    cart_item_1.grid(row=1, column=0)
    cart_item_1_qty.grid(row=1, column=1, padx=500, pady=25)
    cart_item_1_price.grid(row=1, column=2)

    cart_item_2.grid(row=2, column=0)
    cart_item_2_qty.grid(row=2, column=1, padx=100, pady=25)
    cart_item_2_price.grid(row=2, column=2)

    cart_item_3.grid(row=3, column=0)
    cart_item_3_qty.grid(row=3, column=1, padx=100, pady=25)
    cart_item_3_price.grid(row=3, column=2)

    cart_item_4.grid(row=4, column=0)
    cart_item_4_qty.grid(row=4, column=1, padx=100, pady=25)
    cart_item_4_price.grid(row=4, column=2)

    cart_item_5.grid(row=5, column=0)
    cart_item_5_qty.grid(row=5, column=1, padx=100, pady=25)
    cart_item_5_price.grid(row=5, column=2)

    total_label.grid(row=6, column=0)
    cart_total_price.grid(row=6, column=2)

    buy_now_button.grid(row=7, column=2)


def Bring_up_search():
    frame_main.place_forget()
    search_button = Button(frame_search, text="Search", font=("Amazon Ember", 20, "bold"), borderwidth=0, highlightthickness=0, background="WHITE", command= search)
    frame_search.place(relx=.5, rely=.5, anchor=CENTER)
    update(search_items[0])
    search_entry.grid(row=0, column=0)
    search_button.grid(row=0, column=1)
    search_listbox.grid(row=1, column=0, columnspan=2,pady=1)

def fillout(event):
    search_entry.delete(0, END)
    search_entry.insert(0, search_listbox.get(ANCHOR))

def update(data):
    search_listbox.delete(0, END)
    
    for i in data:
        search_listbox.insert(END, i[0].capitalize())

def check(event):
    if search_entry.get() == "":
        data = search_items[0]
    else:
        data = []
        for i in search_items[0]:
            if search_entry.get().lower() in i.lower():
                data.append(i)
    update(data)

def search():
    global screen
    typed = search_entry.get().lower()
    position = 0
    for i in range(len(search_items[0])):
        if typed in search_items[0][i][0]:
            position = i
            break
    screen = search_items[0][position][1]
    position -= 6*(screen-1)
    search_button = Button(frame_main, image=pics[7], borderwidth=0, highlightthickness=0, background="WHITE", command = Bring_up_search)
    search_button.grid_remove()
    for i in frame_search.winfo_children():
        i.grid_remove()
    frame_search.place_forget()
    item_desc_screen(position+1)


        
# ValueError
pics = [PhotoImage(file=f"images/{items[screen-1][0][0]}.png"),
        PhotoImage(file=f"images/{items[screen-1][1][0]}.png"),
        PhotoImage(file=f"images/{items[screen-1][2][0]}.png"),
        PhotoImage(file=f"images/{items[screen-1][3][0]}.png"),
        PhotoImage(file=f"images/{items[screen-1][4][0]}.png"),
        PhotoImage(file=f"images/{items[screen-1][5][0]}.png"),
        PhotoImage(file="images/back.PNG"),
        PhotoImage(file="images/search.png")]

frame_login = Frame(root, background="WHITE")
frame_main = Frame(root, background="WHITE")
frame_item_desc_screen = Frame(root, background="WHITE")
frame_purchase = Frame(root, background="WHITE")
frame_check_out = Frame(root, background="WHITE")
frame_search = Frame(root, background="WHITE")

button_1 = Button(frame_main, image=pics[0], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(1))
button_2 = Button(frame_main, image=pics[1], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(2))
button_3 = Button(frame_main, image=pics[2], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(3))
button_4 = Button(frame_main, image=pics[3], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(4))
button_5 = Button(frame_main, image=pics[4], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(5))
button_6 = Button(frame_main, image=pics[5], borderwidth=0, highlightthickness=0, command=lambda: item_desc_screen(6))

username_label = Label(frame_login, text="Username:", font=fnt, background="WHITE")
password_label = Label(frame_login, text="Password:", font=fnt, background="WHITE")
username_entry = Entry(frame_login, font=fnt, background="light grey")

password_entry_text = StringVar()
password_entry_text.trace("w", lambda *args: character_limit(password_entry_text))
password_entry = Entry(frame_login, font=fnt, background="light grey", textvariable=password_entry_text)
login_button = Button(frame_login, text="LOGIN", font=fnt, command= lambda: login(username_entry.get(), password_entry.get()))
signup_button = Button(frame_login, text="SIGN UP", font=fnt, command= lambda: signup(username_entry.get(), password_entry.get()))
message_label1 = Label(frame_login, text="", font=fnt, background="WHITE")
no_of_items_in_cart_label = Label(frame_main, font=("Amazon Ember", 20, "bold"), background="WHITE")

item_button = Button(root, borderwidth=0, highlightthickness=0, background="WHITE")
back_button = Button(root, image=pics[6], borderwidth=0, highlightthickness=0, background="WHITE", command= lambda: back("menu"))
item_name = Label(frame_item_desc_screen, font=fnt, background="WHITE")
item_quantity = Label(frame_item_desc_screen, font=fnt, background="WHITE")
item_price = Label(frame_item_desc_screen, font=fnt, background="WHITE")
message_label = Label(frame_item_desc_screen, text="", font=("Amazon Ember", 20, "bold"), background="WHITE")

screen_next_button = Button(frame_main, text=">", command=lambda: screen_change("next"), font=("Amazon Ember", 16, "bold"), borderwidth=0, highlightthickness=0, background="WHITE")
screen_prev_button = Button(frame_main, text="<", command=lambda: screen_change("prev"), state="disabled", font=("Amazon Ember",16, "bold"), borderwidth=0, highlightthickness=0, background="WHITE")
check_out_button = Button(frame_main, text="Check Out", font=fnt, borderwidth=0, highlightthickness=0, background="WHITE", command=check_out)
search_button = Button(frame_main, image=pics[7], borderwidth=0, highlightthickness=0, background="WHITE", command = Bring_up_search)
search_entry = Entry(frame_search, font=("Amazon Ember", 30, "bold"), width=56, background="grey")
search_listbox = Listbox(frame_search, width=61, height=14, font=fnt, background="grey")
   

search_listbox.bind("<<ListboxSelect>>", fillout)
search_entry.bind("<KeyRelease>", check)

frame_login.place(relx=.5, rely=.5, anchor=CENTER)
username_label.grid(row=0, column=0, pady=20)
password_label.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=0, padx=20, pady=50)
signup_button.grid(row=2, column=1)
message_label1.grid(row=3, column=0, columnspan=2)

root.mainloop()