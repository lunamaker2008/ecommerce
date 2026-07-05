import streamlit as st

# 1. Page Title (This shows up at the top of your web browser tab)
st.set_page_config(page_title="School Project E-Shop", page_icon="🎒")

# 2. Creating Navigation Links (Sidebar menu)
st.sidebar.title("Navigation Menu")
selected_page = st.sidebar.radio("Go to page:", ["Home", "Products for Sale", "Contact Us"])

# 3. Product Database (Added "image" URLs to each dictionary)
items_for_sale = [
    {
        "name": "School Backpack",
        "price": "₹499",
        "description": "Waterproof bag with multiple compartments and a laptop sleeve.",
        "image": "https://unsplash.com"
    },
    {
        "name": "Scientific Calculator",
        "price": "₹750",
        "description": "Multi-function calculator perfect for high school math and science classes.",
        "image": "https://unsplash.com"
    },
    {
        "name": "Gel Pen Set",
        "price": "₹120",
        "description": "Smooth writing pack of 10 colored gel pens for project work.",
        "image": "https://unsplash.com"
    }
]

# ================= PAGE 1: HOME =================
if selected_page == "Home":
    st.title("🎒 Welcome to Student Supply Co.")
    st.write("This is an e-commerce website built entirely using **Python**.")
    st.info("👈 Please use the navigation menu on the left side to visit our shop or contact us!")

# ================= PAGE 2: PRODUCTS =================
elif selected_page == "Products for Sale":
    st.title("🛒 Items Available for Sale")
    st.write("Below are the items currently in stock, along with their prices and details:")
    st.write("---") # Creates a horizontal line separator

    # Loop through our database to display each item automatically
    for item in items_for_sale:
        st.subheader(item["name"])              # Displays product name
        
        # NEW: Displays the product image (width limits it to a clean box size)
        st.image(item["image"], width=250)
        
        st.write(item["description"])          # Displays description
        st.code(f"Price: {item['price']}")     # Displays price in a highlighted box
        
        # Interactive click button
        if st.button(f"Buy {item['name']}"):
            st.success(f"🎉 Success! {item['name']} has been added to your virtual cart.")
        
        st.write("---") # Line separator between products

# ================= PAGE 3: CONTACT =================
elif selected_page == "Contact Us":
    st.title("📞 Contact Store Owner")
    st.write("Fill out this simple form to place an order or ask a question.")
    
    # Input text boxes
    user_name = st.text_input("Enter Your Name:")
    user_message = st.text_area("Enter Your Message or Order Details:")
    
    # Submit button
    if st.button("Submit Message"):
        if user_name and user_message:
            st.success(f"Thank you, {user_name}! Your message was sent successfully.")
        else:
            st.error("Please fill in both fields before clicking submit.")
