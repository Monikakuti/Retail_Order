import mysql.connector
import streamlit as st

# Function to fetch data 
def fetch_data(query):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',       
        password='',   
        database='retailorder'    
    )
    mycursor = connection.cursor()
    mycursor.execute(query)
    data = mycursor.fetchall()
    mycursor.close()
    connection.close()
    return data

# List of queries
queries = {
    "Top 10 products by revenue": """
    SELECT product_id, SUM(sale_price) AS revenue
    FROM dataframe_1
    GROUP BY product_id
    ORDER BY revenue DESC
    LIMIT 10;
    """, 
    "Top 5 cities with highest profit margins": """
    SELECT city, 
    SUM(profit) / SUM(sale_price) AS profit_margin
    FROM dataframe_1
    GROUP BY city
    ORDER BY profit_margin DESC
    LIMIT 5;
    """,
    "Total discount given for each category": """
    SELECT category, 
    SUM(discount) AS total_discount
    FROM dataframe_1
    GROUP BY category;
    """,
    "Average sale price per product category": """
    SELECT category, 
    AVG(sale_price) AS average_sale_price
    FROM dataframe_1
    GROUP BY category;
    """,  
    "Region with the highest average sale price": """
    SELECT region, 
    AVG(sale_price) AS average_sale_price
    FROM dataframe_1
    GROUP BY region
    ORDER BY average_sale_price DESC
    LIMIT 1;
    """,
    "Total profit per category": """
    SELECT category, 
    SUM(profit) AS total_profit
    FROM dataframe_1
    GROUP BY category;
    """,
    "Top 3 segments with highest quantity of orders": """
    SELECT segment, 
    SUM(quantity) AS total_quantity
    FROM dataframe_1
    GROUP BY segment
    ORDER BY total_quantity DESC
    LIMIT 3;
    """,
    "Average discount percentage per region": """
    SELECT region, 
    AVG(discount_percent) AS average_discount_percentage
    FROM dataframe_1
    GROUP BY region;
    """,
    "Product category with highest total profit": """
    SELECT category, 
    SUM(profit) AS total_profit
    FROM dataframe_1
    GROUP BY category
    ORDER BY total_profit DESC
    LIMIT 1;
    """,
    "Total revenue generated per year": """
    SELECT YEAR(order_date) AS year, 
    SUM(sale_price) AS total_revenue
    FROM dataframe_1
    GROUP BY year;
    """,
    #order_id is primary and foreign key 
    "Find the total sales of each category":""" 
    SELECT dataframe1.category, SUM(dataframe2.sale_price) AS total_sales
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.category;
    """,
    "Total profit on each Region":""" 
    SELECT dataframe1.region, SUM(dataframe2.profit) AS total_profit
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.region;
    """,
    "Top 3 cities with highest total sale ":"""
    SELECT dataframe1.city, SUM(dataframe2.sale_price) AS total_sales
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.city
    ORDER BY total_sales DESC
    LIMIT 3;""",
    "Average discount percentage per region":"""
    SELECT dataframe1.region, 
    AVG(dataframe2.discount_percent) AS average_discount
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.region;
    """,
    "Total profit for each segment":"""
    SELECT dataframe1.segment, SUM(dataframe2.profit) AS total_profit
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.segment;
    """,
    "Top 5 products with the highest quantity sold":"""
    SELECT dataframe2.product_id, SUM(dataframe2.quantity) AS total_quantity
    FROM dataframe2
    GROUP BY dataframe2.product_id
    ORDER BY total_quantity DESC
    LIMIT 5;
    """,
    "Total revenue generated per year":"""
    SELECT YEAR(dataframe1.order_date) AS year, SUM(dataframe2.sale_price) AS total_revenue
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY year;
    """,
    "Sub-categories with the highest average sale price":"""
    SELECT dataframe1.sub_category, AVG(dataframe2.sale_price) AS average_sale_price
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.sub_category
    ORDER BY average_sale_price DESC;
    """,
    "Total discount given for each ship mode:":"""
    SELECT dataframe1.ship_mode, SUM(dataframe2.discount) AS total_discount
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.ship_mode;
    """,
    "Region with the highest average profit per order:":""" 
    SELECT dataframe1.region, AVG(dataframe2.profit) AS average_profit
    FROM dataframe1
    JOIN dataframe2 ON dataframe1.order_id = dataframe2.order_id
    GROUP BY dataframe1.region
    ORDER BY average_profit DESC
    LIMIT 1;
    """
}

# Sidebar for selecting a query
st.sidebar.header("Select a Query")
selected_query = st.sidebar.selectbox("Queries", list(queries.keys()))

# Display the selected query's results
if selected_query:
    st.header(f"Results for: {selected_query}")
    query = queries[selected_query]
    results = fetch_data(query)
    st.table(results)
