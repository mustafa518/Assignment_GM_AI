import streamlit as st
import random
import sqlite3


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="GM FAST FOOD",
    page_icon="🍔",
    layout="wide"
)


# ----------------------------------
# SESSION STATE
# ----------------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []



# ----------------------------------
# SQLITE DATABASE SETUP
# ----------------------------------

def create_database():

    conn = sqlite3.connect("gm_orders.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        order_id TEXT,

        name TEXT,

        phone TEXT,

        address TEXT,

        city TEXT,

        total INTEGER,

        status TEXT,

        items TEXT

    )
    """)


    conn.commit()

    conn.close()



create_database()



# ----------------------------------
# MENU ITEMS
# ----------------------------------

menu = [


{
    "Item": "🍔 Zinger Burger",
    "Price": 650
},


{
    "Item": "🧀🍔 Cheese Burger",
    "Price": 750
},


{
    "Item": "🍟 French Fries",
    "Price": 300
},


{
    "Item": "🌯 Chicken Shawarma",
    "Price": 450
},


{
    "Item": "🌯 GM Food Special Roll",
    "Price": 650
},


{
    "Item": "🌯 Chicken Chatni Roll",
    "Price": 450
},


{
    "Item": "🌯 Chicken Mayo Roll",
    "Price": 500
},


{
    "Item": "🍢 Reshmi Kabab",
    "Price": 700
},


{
    "Item": "🍗 Chicken Nuggets",
    "Price": 500
}


]



# ----------------------------------
# PIZZA MENU
# ----------------------------------

pizza_menu = {


"🍕 Small Pizza":700,


"🍕 Medium Pizza":1200,


"🍕 Large Pizza":1800


}
# ----------------------------------
# HEADER
# ----------------------------------

col1, col2 = st.columns([1,4])


with col1:

    st.image(
        "owner.png",
        width=200
    )


with col2:

    st.title(
        "🍔 GM FAST FOOD"
    )


    st.write(
        "👨‍💼 Owner: Ghulam Mustafa"
    )



st.markdown("""

## 😋 WELCOME TO GM FAST FOOD
          ( THE NAME OF REAL TASTE )

🍔 Burgers

🌯 Special Rolls

🍕 Pizza

🍟 Fries


🚚 Fast Delivery | 💯 Quality Food


""")



# ----------------------------------
# MENU SECTION
# ----------------------------------

st.divider()


st.header(
    "📋 Our Special Menu"
)



cols = st.columns(2)



for i,item in enumerate(menu):


    with cols[i % 2]:


        with st.container(border=True):


            st.subheader(
                item["Item"]
            )


            st.write(
                f"💰 Price: PKR {item['Price']}"
            )


            quantity = st.number_input(

                "Quantity",

                min_value=1,

                max_value=20,

                value=1,

                key=f"menu_qty_{i}"

            )


            if st.button(

                "➕ Add To Cart",

                key=f"menu_add_{i}"

            ):


                st.session_state.cart.append(

                    {

                    "Item":item["Item"],

                    "Price":item["Price"],

                    "Quantity":quantity

                    }

                )


                st.success(
                    "Added Successfully!"
                )



# ----------------------------------
# PIZZA SECTION
# ----------------------------------

st.divider()


st.header(
    "🍕 Pizza Menu"
)



pizza_cols = st.columns(3)



for i,(pizza,price) in enumerate(pizza_menu.items()):


    with pizza_cols[i]:


        with st.container(border=True):


            st.subheader(
                pizza
            )


            st.write(
                f"💰 Price: PKR {price}"
            )


            quantity = st.number_input(

                "Quantity",

                min_value=1,

                max_value=10,

                value=1,

                key=f"pizza_qty_{i}"

            )



            if st.button(

                "🍕 Add Pizza",

                key=f"pizza_add_{i}"

            ):


                st.session_state.cart.append(

                    {

                    "Item":pizza,

                    "Price":price,

                    "Quantity":quantity

                    }

                )


                st.success(
                    "Pizza Added!"
                )



# ----------------------------------
# CART SECTION WITH REMOVE BUTTON
# ----------------------------------

with st.sidebar:


    st.title(
        "🛒 Your Cart"
    )



    if len(st.session_state.cart)==0:


        st.info(
            "Cart is Empty"
        )


    else:


        total = 0



        for index,item in enumerate(st.session_state.cart):


            item_total = item["Price"] * item["Quantity"]


            total += item_total



            col1,col2 = st.columns([4,1])


            with col1:


                st.write(

f"""
🍔 **{item['Item']}**

Quantity: {item['Quantity']}

Price: PKR {item_total}

"""

                )



            with col2:


                if st.button(

                    "🗑",

                    key=f"remove_{index}"

                ):


                    st.session_state.cart.pop(index)


                    st.rerun()



        st.divider()



        st.subheader(

            f"💰 Total: PKR {total}"

        )



        if st.button(
            "🗑 Clear Cart"
        ):


            st.session_state.cart=[]


            st.rerun()
                # ----------------------------------
# SPECIAL DEALS
# ----------------------------------

st.divider()

st.markdown("""

# 🔥 GM FAST FOOD SPECIAL DEALS 🔥

### 🎁 Save More With Our Offers ❤️

""")


deals = [


{
"name":"🎓 Student Deal (20% OFF)",
"price":799,
"items":[
"🍔 Zinger Burger",
"🍟 Fries",
"🥤 Cold Drink"
]
},



{
"name":"❤️ Couple Deal (25% OFF)",
"price":1499,
"items":[
"🍔 2 Zinger Burger",
"🍟 Large Fries",
"🥤 2 Cold Drinks"
]
},



{
"name":"👨‍👩‍👧 Family Deal (30% OFF)",
"price":2499,
"items":[
"🍔 3 Burgers",
"🍕 Medium Pizza",
"🍟 Family Fries",
"🥤 1.5L Drink"
]
},



{
"name":"🌯 Roll Special Deal (25% OFF)",
"price":1299,
"items":[
"🌯 GM Food Special Roll",
"🌯 Chicken Mayo Roll",
"🍟 Fries",
"🥤 Drink"
]
},



{
"name":"🍕 Pizza Party Deal (30% OFF)",
"price":2999,
"items":[
"🍕 Large Pizza",
"🍟 Fries",
"🥤 1.5L Drink"
]
},



{
"name":"🔥 GM Mega Deal (35% OFF)",
"price":3499,
"items":[
"🍔 2 Zinger Burger",
"🌯 2 Special Rolls",
"🍕 Medium Pizza",
"🍟 Fries"
]
}

]



deal_cols = st.columns(3)



for i,deal in enumerate(deals):


    with deal_cols[i % 3]:


        with st.container(border=True):


            st.subheader(
                deal["name"]
            )


            st.write(
                "📦 Includes:"
            )


            for item in deal["items"]:

                st.write(
                    f"✅ {item}"
                )



            st.success(
                f"💰 PKR {deal['price']}"
            )


            quantity = st.number_input(

                "Deal Quantity",

                min_value=1,

                max_value=10,

                value=1,

                key=f"deal_qty_{i}"

            )


            if st.button(

                "🛒 Add Deal",

                key=f"deal_add_{i}"

            ):


                st.session_state.cart.append(

                {

                "Item":deal["name"],

                "Price":deal["price"],

                "Quantity":quantity

                }

                )


                st.success(
                    "Deal Added!"
                )




# ----------------------------------
# CHECKOUT
# ----------------------------------

st.divider()

st.header(
"🧾 Checkout"
)



if len(st.session_state.cart)>0:


    total=0


    for item in st.session_state.cart:

        total += item["Price"]*item["Quantity"]



    st.subheader(
        f"💰 Total Bill: PKR {total}"
    )



    name = st.text_input(
        "👤 Customer Name"
    )


    phone = st.text_input(
        "📞 Contact Number"
    )


    address = st.text_area(
        "🏠 Delivery Address"
    )


    city = st.text_input(
        "📍 City"
    )



    if st.button(
        "✅ Place Order"
    ):



        if not name or not phone or not address or not city:


            st.error(
                "⚠️ Please fill all details."
            )



        elif city.lower()!="quetta":


            st.error(
                "❌ Delivery only available in Quetta."
            )



        elif not(phone.startswith("03") and len(phone)==11 and phone.isdigit()):


            st.error(
                "❌ Enter correct phone number."
            )



        else:


            order_id="GM"+str(random.randint(1000,9999))



            items_text=""


            for item in st.session_state.cart:


                items_text += (

                    item["Item"]

                    +" x "

                    +str(item["Quantity"])

                    +", "

                )



            conn = sqlite3.connect(
                "gm_orders.db"
            )


            cursor = conn.cursor()



            cursor.execute("""

            INSERT INTO orders

            (order_id,name,phone,address,city,total,status,items)

            VALUES (?,?,?,?,?,?,?,?)

            """,

            (

            order_id,

            name,

            phone,

            address,

            city,

            total,

            "✅ Order Confirmed",

            items_text

            ))



            conn.commit()

            conn.close()



            st.success(
                "🎉 Order Placed Successfully!"
            )


            st.info(
                f"📦 Your Order ID: {order_id}"
            )



            st.write("""

❤️ Thank you for ordering from GM FAST FOOD.

👨‍🍳 Your food preparation has started.

🚚 Delivery Time: 20-30 Minutes

📞 Contact: 03368382248

""")


            st.session_state.cart=[]


else:

    st.info(
        "🍔 Please add items first."
    )
    # ----------------------------------
# ORDER TRACKING
# ----------------------------------

st.divider()

st.header(
"📦 Track Your Order"
)



track_id = st.text_input(
"Enter Order ID"
)



if st.button(
"🔍 Check Status"
):


    conn = sqlite3.connect(
        "gm_orders.db"
    )

    cursor = conn.cursor()


    result = cursor.execute(

    "SELECT * FROM orders WHERE order_id=?",

    (track_id,)

    ).fetchone()


    conn.close()



    if result:


        st.success(

f"""

👤 Customer: {result[2]}

🍔 Items:

{result[8]}


💰 Bill:

PKR {result[6]}


📦 Status:

{result[7]}


🚚 Thank You For Choosing GM FAST FOOD ❤️

"""

        )


    else:

        st.error(
            "❌ Order ID Not Found"
        )




# ----------------------------------
# ADMIN PANEL
# ----------------------------------

st.divider()

st.header(
"👨‍💼 Admin Panel"
)



password = st.text_input(

"Admin Password",

type="password"

)



if password=="GM123":


    st.success(
        "Admin Login Successful"
    )


    conn = sqlite3.connect(
        "gm_orders.db"
    )

    cursor = conn.cursor()


    orders = cursor.execute(
    "SELECT * FROM orders"
    ).fetchall()


    conn.close()



    if orders:


        for order in orders:


            st.write("----------------")


            st.write(

f"""

📦 Order ID: {order[1]}


👤 Customer: {order[2]}


📞 Phone: {order[3]}


🏠 Address: {order[4]}


🍔 Items:

{order[8]}


💰 Total:

PKR {order[6]}


📌 Status:

{order[7]}

"""

            )



            new_status = st.selectbox(

            "Change Status",

            [

            "✅ Order Confirmed",

            "👨‍🍳 Preparing Food",

            "🚚 Out For Delivery",

            "🎉 Delivered Successfully"

            ],

            key=order[1]

            )


            if st.button(
                "Update Status",
                key="update"+order[1]
            ):


                conn=sqlite3.connect(
                    "gm_orders.db"
                )

                cursor=conn.cursor()


                cursor.execute(

                "UPDATE orders SET status=? WHERE order_id=?",

                (new_status,order[1])

                )


                conn.commit()

                conn.close()


                st.success(
                    "Status Updated"
                )


                st.rerun()



# ----------------------------------
# RATING
# ----------------------------------

st.divider()

st.header(
"⭐ Customer Rating"
)


rating = st.slider(

"Give Rating",

1,

5,

5

)


if st.button(
"⭐ Submit Rating"
):

    st.success(
    f"Thank you for giving {rating} ⭐"
    )



# ----------------------------------
# FEEDBACK
# ----------------------------------

st.divider()

st.header(
"💬 Feedback & Complaint"
)


choice = st.selectbox(

"Select",

[
"⭐ Feedback",
"⚠️ Complaint",
"💡 Suggestion"
]

)


message = st.text_area(
"Your Message"
)



if st.button(
"📩 Submit"
):

    if message:

        st.success(
        "Thank you for your response ❤️"
        )

    else:

        st.error(
        "Please write message"
        )



# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()


st.markdown("""

# ❤️ Thank You For Visiting GM FAST FOOD

🍔 Fresh Taste Everyday

⭐ Quality Food • Happy Customers

🚚 Fast & Reliable Delivery


📞 03368382248


**GM FAST FOOD Team**

""")
