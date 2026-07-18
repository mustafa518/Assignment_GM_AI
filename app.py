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

    {"Item": "🍔 Zinger Burger", "Price": 650},
    {"Item": "🧀🍔 Cheese Burger", "Price": 750},
    {"Item": "🍟 French Fries", "Price": 300},
    {"Item": "🌯 Chicken Shawarma", "Price": 450},
    {"Item": "🥪 Grilled Cheese Sandwich", "Price": 550},
    {"Item": "🍢 Reshmi Kabab", "Price": 700},
    {"Item": "🍗 Chicken Nuggets", "Price": 500},
    {"Item": "🍕 Pizza", "Price": 1200}

]



# ----------------------------------
# DISCOUNT DEALS
# ----------------------------------

deals = [

    {
        "name": "🔥 Student Special Deal (20% OFF)",
        "price": 799,
        "items": [
            "🍔 Zinger Burger",
            "🍟 French Fries",
            "🥤 Cold Drink",
            "🏷️ 20% OFF"
        ]
    },


    {
        "name": "❤️ Couple Deal (25% OFF)",
        "price": 1499,
        "items": [
            "🧀 2 Cheese Burgers",
            "🍟 Large Fries",
            "🥤 2 Cold Drinks",
            "🏷️ 25% OFF"
        ]
    },


    {
        "name": "👨‍👩‍👧 Family Deal (30% OFF)",
        "price": 2499,
        "items": [
            "🍔 3 Zinger Burgers",
            "🍟 Large Fries",
            "🍕 Medium Pizza",
            "🥤 1.5L Drink",
            "🏷️ 30% OFF"
        ]
    },


    {
        "name": "🌯 Shawarma Deal (15% OFF)",
        "price": 999,
        "items": [
            "🌯 2 Shawarma",
            "🍟 Fries",
            "🥤 Cold Drink",
            "🏷️ 15% OFF"
        ]
    },


    {
        "name": "🎉 Weekend Mega Deal (35% OFF)",
        "price": 2999,
        "items": [
            "🍔 2 Zinger Burgers",
            "🧀 2 Cheese Burgers",
            "🍟 Family Fries",
            "🥤 1.5L Drink",
            "🏷️ 35% OFF"
        ]
    }

]



# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.image(
        "owner.png",
        width=220
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

        cart_total = sum(
            item["Price"]
            for item in st.session_state.cart
        )


        for item in st.session_state.cart:

            st.write(
                f"✅ {item['Item']} - PKR {item['Price']}"
            )


        st.divider()


        st.subheader(
            f"💰 Total: PKR {cart_total}"
        )


        if st.button(
            "🗑 Clear Cart"
        ):

            st.session_state.cart = []

            st.rerun()



# ----------------------------------
# HEADER
# ----------------------------------

col1, col2 = st.columns([1,4])


with col1:

    st.image(
        "owner.png",
        width=220
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

Fresh Taste • Quality Food • Fast Delivery ❤️

🍔 Burgers • 🌯 Shawarma • 🍕 Pizza • 🍟 Fries

""")


st.info(
    "🔥 Get Amazing Discounts Up To 35% OFF!"
)



# ----------------------------------
# MENU
# ----------------------------------

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


            if st.button(
                "➕ Add to Cart",
                key=f"menu_{i}"
            ):

                st.session_state.cart.append(
                    {
                        "Item": item["Item"],
                        "Price": item["Price"]
                    }
                )


                st.success(
                    "Added Successfully!"
                )
                # ----------------------------------
# DISCOUNT DEALS SECTION
# ----------------------------------

st.divider()


st.markdown("""

# 🔥 GM FAST FOOD SPECIAL DEALS 🔥

### 🎁 Save More With Our Discount Offers ❤️

""")


deal_cols = st.columns(3)


for i, deal in enumerate(deals):


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
                f"💰 Price: PKR {deal['price']}"
            )


            if st.button(
                "🛒 Add Deal",
                key=f"deal_{i}"
            ):


                st.session_state.cart.append(

                    {
                        "Item": deal["name"],
                        "Price": deal["price"]
                    }

                )


                st.success(
                    "🎉 Deal Added Successfully!"
                )



# ----------------------------------
# CHECKOUT SECTION
# ----------------------------------

st.divider()


st.header(
    "🧾 Checkout"
)



if len(st.session_state.cart) > 0:


    total = sum(

        item["Price"]

        for item in st.session_state.cart

    )


    delivery_charges = 100


    final_total = total + delivery_charges



    st.write(
        f"🛒 Food Bill: PKR {total}"
    )


    st.write(
        f"🚚 Delivery Charges: PKR {delivery_charges}"
    )


    st.subheader(
        f"💰 Total Bill: PKR {final_total}"
    )



    name = st.text_input(
        "👤 Customer Name"
    )


    address = st.text_area(
        "🏠 Delivery Address"
    )


    phone = st.text_input(
        "📞 Contact Number"
    )



    if st.button(
        "✅ Place Order"
    ):



        if not name or not address or not phone:


            st.error(
                "⚠️ Please fill all details."
            )



        elif not (

            phone.startswith("03")
            and len(phone) == 11
            and phone.isdigit()

        ):


            st.error(
                "❌ Enter correct phone number"
            )



        else:


            order_id = "GM" + str(
                random.randint(1000,9999)
            )


            st.session_state.orders[order_id] = {


                "Name": name,

                "Phone": phone,

                "Address": address,

                "Total": final_total,

                "Status": "✅ Order Confirmed"

            }



            st.success(
                "🎉 Your Order Has Been Placed Successfully!"
            )


            st.info(
                f"📦 Your Order ID is: {order_id}"
            )


            st.markdown(f"""

### ❤️ Thank You {name}

Your order has been received successfully.

🍔 We are preparing your fresh food.

🚚 Delivery Time: 20-30 Minutes


**GM FAST FOOD Team**

""")


            st.session_state.cart = []



else:


    st.info(
        "🍔 Please add food items or deals to your cart."
    )
    # ----------------------------------
# CUSTOMER ORDER TRACKING
# ----------------------------------

st.divider()


st.header(
    "📦 Track Your Order"
)


search_id = st.text_input(
    "Enter Your Order ID"
)



if st.button(
    "🔍 Check Order Status"
):


    if search_id in st.session_state.orders:


        order = st.session_state.orders[search_id]


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


admin_password = st.text_input(
    "Enter Admin Password",
    type="password"
)



if admin_password == "GM123":


    st.success(
        "Admin Login Successful ✅"
    )



    if len(st.session_state.orders) > 0:



        selected_order = st.selectbox(

            "Select Order",

            list(st.session_state.orders.keys())

        )



        new_status = st.selectbox(

            "Change Order Status",

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



            st.session_state.orders[selected_order]["Status"] = new_status



            st.success(
                "Order Status Updated Successfully!"
            )


            # refresh page so customer tracking updates

            st.rerun()



    else:


        st.info(
            "No Orders Available"
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
    "⭐ Rate Your Experience"
)


rating = st.slider(
    "Select Rating",
    1,
    5,
    5
)



if st.button(
    "⭐ Submit Rating"
):


    st.success(
        f"Thank you for giving {rating} ⭐ rating!"
    )



# ----------------------------------
# FEEDBACK & COMPLAINT
# ----------------------------------

st.divider()


st.header(
    "💬 Feedback & Complaint"
)


feedback_type = st.selectbox(

    "Select Type",

    [

        "⭐ Feedback",

        "⚠️ Complaint",

        "💡 Suggestion"

    ]

)



customer_message = st.text_area(
    "Write Your Message"
)



if st.button(
    "📩 Submit"
):


    if customer_message:


        if feedback_type == "⚠️ Complaint":


            st.warning(
                "Thank you. Your complaint has been received. We will improve our service ❤️"
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
# SHOP TIMING
# ----------------------------------

st.divider()


st.header(
    "🕒 Shop Timing"
)


st.write("""

⏰ Opening Hours:

12:00 PM - 12:00 AM


📅 Open Everyday


🚚 Online Delivery Available

""")



# ----------------------------------
# CONTACT
# ----------------------------------

st.divider()


st.header(
    "📞 Contact Us"
)


st.write("""

🍔 GM FAST FOOD


📱 Call / WhatsApp:

03368382248


🚚 Fast & Reliable Delivery


💯 Quality Food & Customer Satisfaction

""")



# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()


st.markdown("""

## ❤️ Thank You For Visiting GM FAST FOOD


🍔 Fresh Taste Everyday


⭐ Quality Food • Best Service


🚚 Fast Delivery


📞 Customer Support: 03368382248


**GM FAST FOOD Team**

""")
