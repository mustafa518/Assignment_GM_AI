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
        "Item": "🥪 Grilled Cheese Sandwich",
        "Price": 550
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

pizza_sizes = {

    "Small Pizza": 700,

    "Medium Pizza": 1200,

    "Large Pizza": 1800

}



# ----------------------------------
# SIDEBAR CART
# ----------------------------------

with st.sidebar:


    st.image(
        "owner.png",
        width=200
    )


    st.write(
        "👨‍💼 Owner: Ghulam Mustafa"
    )


    st.title(
        "🛒 Your Cart"
    )



    if len(st.session_state.cart) == 0:


        st.info(
            "Cart is Empty"
        )


    else:


        total = 0



        for item in st.session_state.cart:


            item_total = item["Price"] * item["Quantity"]


            total += item_total



            st.write(
                f"""
{item['Item']}

Quantity: {item['Quantity']}

Price: PKR {item_total}

"""
            )



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
# HEADER
# ----------------------------------

col1,col2 = st.columns([1,4])



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


🍔 Fresh Burgers  
🍕 Hot Pizza  
🌯 Delicious Shawarma  
🍟 Crispy Fries  


🚚 Fast Delivery | 💯 Quality Food

""")



# ----------------------------------
# NORMAL MENU
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

                "Select Quantity",

                min_value=1,

                max_value=20,

                value=1,

                key=f"normal_qty_{i}"

            )



            if st.button(

                "➕ Add to Cart",

                key=f"normal_add_{i}"

            ):


                st.session_state.cart.append(

                    {

                        "Item": item["Item"],

                        "Price": item["Price"],

                        "Quantity": quantity

                    }

                )


                st.success(
                    "Added To Cart!"
                )



# ----------------------------------
# PIZZA SECTION
# ----------------------------------

st.divider()


st.header(
    "🍕 Pizza Menu"
)



pizza_cols = st.columns(3)



for i,(pizza,price) in enumerate(pizza_sizes.items()):



    with pizza_cols[i]:


        with st.container(border=True):


            st.subheader(
                f"🍕 {pizza}"
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

                "➕ Add Pizza",

                key=f"pizza_{i}"

            ):


                st.session_state.cart.append(

                    {

                        "Item": pizza,

                        "Price": price,

                        "Quantity": quantity

                    }

                )


                st.success(
                    f"{pizza} Added!"
                )
                # ----------------------------------
# DISCOUNT DEALS
# ----------------------------------

st.divider()


st.markdown("""

# 🔥 GM FAST FOOD DEALS 🔥

### 🎁 Save More With Our Special Offers ❤️

""")


deals = [

    {
        "name": "🎓 Student Deal (20% OFF)",
        "price": 799,
        "items": [
            "🍔 Zinger Burger",
            "🍟 Fries",
            "🥤 Cold Drink"
        ]
    },


    {
        "name": "❤️ Couple Deal (25% OFF)",
        "price": 1499,
        "items": [
            "🍔 2 Zinger Burgers",
            "🍟 Large Fries",
            "🥤 2 Drinks"
        ]
    },


    {
        "name": "👨‍👩‍👧 Family Deal (30% OFF)",
        "price": 2499,
        "items": [
            "🍔 3 Burgers",
            "🍕 Medium Pizza",
            "🍟 Family Fries",
            "🥤 1.5L Drink"
        ]
    }


]



deal_cols = st.columns(3)



for i,deal in enumerate(deals):


    with deal_cols[i]:


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



            deal_quantity = st.number_input(

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

                        "Item": deal["name"],

                        "Price": deal["price"],

                        "Quantity": deal_quantity

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


    food_total = 0



    for item in st.session_state.cart:


        food_total += (

            item["Price"]

            *

            item["Quantity"]

        )



    delivery_charges = 100


    final_total = food_total + delivery_charges



    st.write(
        f"🍔 Food Total: PKR {food_total}"
    )


    st.write(
        f"🚚 Delivery Charges: PKR {delivery_charges}"
    )


    st.subheader(
        f"💰 Final Bill: PKR {final_total}"
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

                "Total": final_total,

                "Status": "✅ Order Confirmed",


                "Items": st.session_state.cart.copy()

            }



            st.success(
                "🎉 Order Placed Successfully!"
            )


            st.info(
                f"📦 Your Order ID: {order_id}"
            )



            st.markdown(f"""

## ❤️ Thank You {name}

Your order has been confirmed.

🍔 Fresh food preparation started.

🚚 Delivery Time: 20-30 Minutes


📞 Contact: 03368382248


**GM FAST FOOD Team**

""")


            st.session_state.cart = []



else:


    st.info(
        "🍔 Add items to cart first."
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

✅ Order Found


👤 Customer: {order['Name']}

💰 Total Bill: PKR {order['Total']}


📦 Current Status:

{order['Status']}


🚚 Thank you for choosing GM FAST FOOD ❤️

"""
        )


        st.write(
            "### 🛒 Order Items"
        )


        for item in order["Items"]:

            st.write(
                f"""
{item['Item']}  
Quantity: {item['Quantity']}
"""
            )


    else:


        st.error(
            "❌ Invalid Order ID"
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
        "Admin Login Successful ✅"
    )



    if len(st.session_state.orders) > 0:


        selected_order = st.selectbox(

            "Select Order",

            list(st.session_state.orders.keys())

        )



        status = st.selectbox(

            "Update Order Status",

            [

                "✅ Order Confirmed",

                "👨‍🍳 Preparing Food",

                "🚚 Out For Delivery",

                "🎉 Delivered Successfully"

            ]

        )



        if st.button(
            "🔄 Update Status"
        ):



            st.session_state.orders[selected_order]["Status"] = status



            st.success(
                "Order Status Updated!"
            )


            st.rerun()



    else:


        st.info(
            "No Orders Available"
        )



    # ----------------------------------
    # SALES SUMMARY
    # ----------------------------------


    st.divider()


    st.header(
        "📊 Today's Sales Summary"
    )



    sales = {}



    for order in st.session_state.orders.values():


        for item in order["Items"]:


            name = item["Item"]


            qty = item["Quantity"]



            if name in sales:

                sales[name] += qty


            else:

                sales[name] = qty




    if len(sales) > 0:


        for item,qty in sales.items():


            st.write(
                f"🍔 {item} = {qty} Sold"
            )


    else:


        st.info(
            "No Sales Yet"
        )



else:


    st.info(
        "Admin Access Only"
    )
    # ----------------------------------
# CUSTOMER RATING
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
    "Submit Rating"
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



feedback_type = st.selectbox(

    "Select Option",

    [

        "⭐ Feedback",

        "⚠️ Complaint",

        "💡 Suggestion"

    ]

)



message = st.text_area(
    "Write Your Message"
)



if st.button(
    "📩 Send"
):


    if message:


        if feedback_type == "⚠️ Complaint":


            st.warning(

                "Your complaint has been received. We will improve our service ❤️"

            )


        elif feedback_type == "⭐ Feedback":


            st.success(

                "Thank you for your valuable feedback ❤️"

            )


        else:


            st.info(

                "Thank you for your suggestion 💡"

            )


    else:


        st.error(
            "Please write your message."
        )




# ----------------------------------
# SHOP INFORMATION
# ----------------------------------

st.divider()


st.header(
    "🏪 GM FAST FOOD Information"
)



st.write("""

📍 Delivery Area: Quetta Only


⏰ Opening Time:

12:00 PM - 12:00 AM


📅 Open Everyday


📞 Contact / WhatsApp:

03368382248


🚚 Fast & Reliable Delivery


""")




# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()


st.markdown("""

# ❤️ Thank You For Visiting GM FAST FOOD


🍔 Fresh Taste Everyday


⭐ Quality Food • Happy Customers


🚚 Fast Delivery Service


📞 03368382248


**GM FAST FOOD Team**

""")
