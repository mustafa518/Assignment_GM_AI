import streamlit as st
import random


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


if "orders" not in st.session_state:
    st.session_state.orders = {}



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
# PIZZA SIZE
# ----------------------------------

pizza_menu = {

    "🍕 Small Pizza": 700,

    "🍕 Medium Pizza": 1200,

    "🍕 Large Pizza": 1800

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

## 😋 Welcome to GM FAST FOOD

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

                    "Item": item["Item"],

                    "Price": item["Price"],

                    "Quantity": quantity

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

                    "Item": pizza,

                    "Price": price,

                    "Quantity": quantity

                    }

                )


                st.success(
                    "Pizza Added!"
                )
                # ----------------------------------
# ----------------------------------
# CART SECTION WITH REMOVE BUTTON
# ----------------------------------

with st.sidebar:

    st.title("🛒 Your Cart")


    if len(st.session_state.cart) == 0:

        st.info("Cart is Empty")


    else:

        total = 0


        for index, item in enumerate(st.session_state.cart):

            item_total = item["Price"] * item["Quantity"]

            total += item_total


            st.write(
                f"""
🍔 {item['Item']}

Quantity: {item['Quantity']}

Price: PKR {item_total}
"""
            )


            if st.button(
                "🗑 Remove Item",
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

            st.session_state.cart = []

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

"🌯 GM Special Roll",

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



if len(st.session_state.cart) > 0:


    total = 0


    for item in st.session_state.cart:


        total += item["Price"] * item["Quantity"]



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



        elif city.lower() != "quetta":


            st.error(

                "❌ Sorry! Delivery is only available in Quetta."

            )



        elif not (

            phone.startswith("03")

            and len(phone)==11

            and phone.isdigit()

        ):


            st.error(
                "❌ Enter correct phone number."
            )



        else:


            order_id = "GM" + str(

                random.randint(1000,9999)

            )



            st.session_state.orders[order_id] = {


                "Name": name,

                "Phone": phone,

                "Address": address,

                "City": city,

                "Total": total,

                "Status": "✅ Order Confirmed",

                "Items": st.session_state.cart.copy()

            }



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


    if track_id in st.session_state.orders:


        order = st.session_state.orders[track_id]


        st.success(

f"""

👤 Customer: {order['Name']}


💰 Bill: PKR {order['Total']}


📦 Status:

{order['Status']}


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



if password == "GM123":


    st.success(
        "Admin Login Successful"
    )



    if len(st.session_state.orders)>0:


        order_select = st.selectbox(

            "Select Order",

            list(st.session_state.orders.keys())

        )



        new_status = st.selectbox(

            "Change Status",

            [

            "✅ Order Confirmed",

            "👨‍🍳 Preparing Food",

            "🚚 Out For Delivery",

            "🎉 Delivered Successfully"

            ]

        )



        if st.button(
            "Update Status"
        ):


            st.session_state.orders[order_select]["Status"] = new_status


            st.success(
                "Status Updated!"
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
# FEEDBACK / COMPLAINT
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


        if choice=="⚠️ Complaint":


            st.warning(

                "Your complaint received. We will improve our service ❤️"

            )


        elif choice=="⭐ Feedback":


            st.success(

                "Thank you for your valuable feedback ❤️"

            )


        else:


            st.info(

                "Thank you for your suggestion 💡"

            )


    else:


        st.error(
            "Please write message."
        )




# ----------------------------------
# CONTACT INFORMATION
# ----------------------------------

st.divider()


st.header(
    "📞 Contact GM FAST FOOD"
)



st.write("""

🍔 GM FAST FOOD


📍 Delivery Area:

Quetta Only


📞 Call / WhatsApp:

03368382248


🚚 Fast Delivery

💯 Quality Food


⏰ Timing:

12:00 PM - 12:00 AM

""")




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
