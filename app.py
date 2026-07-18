import streamlit as st

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="GM Fast Food",
    page_icon="🍔",
    layout="wide"
)


# ----------------------------------
# SESSION STATE
# ----------------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []


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
            "🥤 Regular Cold Drink",
            "🏷️ Discount: 20% OFF"
        ]
    },


    {
        "name": "❤️ Couple Deal (25% OFF)",
        "price": 1499,
        "items": [
            "🧀 2 Cheese Burgers",
            "🍟 Large French Fries",
            "🥤 2 Cold Drinks",
            "🏷️ Discount: 25% OFF"
        ]
    },


    {
        "name": "👨‍👩‍👧 Family Feast Deal (30% OFF)",
        "price": 2499,
        "items": [
            "🍔 3 Zinger Burgers",
            "🍟 Large Fries",
            "🍕 Medium Pizza",
            "🥤 1.5L Cold Drink",
            "🏷️ Discount: 30% OFF"
        ]
    },


    {
        "name": "🌯 Shawarma Lovers Deal (15% OFF)",
        "price": 999,
        "items": [
            "🌯 2 Chicken Shawarma",
            "🍟 French Fries",
            "🥤 Cold Drink",
            "🏷️ Discount: 15% OFF"
        ]
    },


    {
        "name": "🎉 Weekend Mega Deal (35% OFF)",
        "price": 2999,
        "items": [
            "🍔 2 Zinger Burgers",
            "🧀 2 Cheese Burgers",
            "🍟 Family Fries",
            "🥤 1.5L Cold Drink",
            "🏷️ Discount: 35% OFF"
        ]
    }

]


# ----------------------------------
# SIDEBAR CART
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


        total = sum(
            item["Price"]
            for item in st.session_state.cart
        )


        for item in st.session_state.cart:

            st.write(
                f"✅ {item['Item']} - PKR {item['Price']}"
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

## 😋 Welcome to GM Fast Food

Fresh Burgers • Crispy Fries • Delicious Shawarma • Hot Pizza

🚚 Fast Delivery | 💯 Quality Food | 💵 Cash On Delivery

""")


st.info(
    "🔥 Today's Special: Get Amazing Discounts Up To 35% OFF!"
)



# ----------------------------------
# MENU SECTION
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
# DISCOUNT OFFERS SECTION
# ----------------------------------

st.divider()


st.markdown("""

# 🔥 GM FAST FOOD DISCOUNT OFFERS 🔥

### 🎁 Get Amazing Discounts Up To 35% OFF ❤️

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
                f"🔥 Limited Offer Price: PKR {deal['price']}"
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


    st.subheader(
        f"💰 Total Bill: PKR {total}"
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
                "❌ Wrong Phone Number"
            )



        else:



            st.success(
                "🎉 Your Order Has Been Placed Successfully!"
            )


            st.balloons()



            st.markdown(f"""

# ❤️ Thank You {name}!


Your order has been received successfully. 😊


🍔 Our team is preparing your fresh food with care.


🚚 Delivery Time: 20-30 Minutes


⭐ Your satisfaction is our first priority.


We hope you enjoy your meal and visit us again.


**With Love ❤️**  
**GM Fast Food Team**

""")



            st.write(
                f"📞 Contact: {phone}"
            )


            st.write(
                f"🏠 Address: {address}"
            )



            st.write(
                "### 🛍️ Order Summary"
            )



            for item in st.session_state.cart:


                st.write(

                    f"✅ {item['Item']} - PKR {item['Price']}"

                )



            st.session_state.cart = []



else:


    st.info(
        "🍔 Please add food items or discount deals to your cart."
    )
    # ----------------------------------
# CUSTOMER FEEDBACK & COMPLAINT
# ----------------------------------

st.divider()


st.header(
    "💬 Customer Feedback & Complaint"
)


st.write(
    "Your feedback helps us improve our food quality and customer service."
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
    "Write your message"
)



customer_name = st.text_input(
    "Your Name"
)



if st.button(
    "📩 Submit"
):


    if not message or not customer_name:


        st.warning(
            "⚠️ Please fill all details."
        )



    elif feedback_type == "⚠️ Complaint":


        st.error(
            f"""

Dear {customer_name},

We are sorry for the inconvenience.

Your complaint has been received successfully.

Our team will review your complaint and work
to improve our service.

Thank you for informing us ❤️

"""
        )



    elif feedback_type == "⭐ Feedback":


        st.success(
            f"""

Dear {customer_name},

Thank you for your valuable feedback ❤️

We really appreciate your support.

Your feedback helps GM Fast Food provide
better taste and service.

Visit us again! 🍔

"""
        )



    else:


        st.info(
            f"""

Dear {customer_name},

Thank you for your suggestion 💡

We will consider your idea to improve
our food quality and customer experience.

"""
        )



# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()


st.markdown("""

## ❤️ Thank You For Visiting GM Fast Food

🍔 Fresh Food Everyday

⭐ Quality Taste & Fresh Ingredients

🚚 Fast & Reliable Delivery

💬 Customer Satisfaction Is Our Priority


**GM Fast Food Team**

""")
