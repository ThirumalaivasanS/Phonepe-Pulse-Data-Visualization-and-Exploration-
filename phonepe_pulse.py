import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Phonepe Pulse Data Visualization and Exploration",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("Phonepe Pulse Data Visualization and Exploration:", unsafe_allow_html=True)
option = st.selectbox(
    "What story does your data want to tell? Let's bring it to life through captivating visualization!",
    ('Top Data', 'All Data')
)

st.write('You selected:', option)

if option == "Top Data":
    visibility = st.radio(
        "Set the category of data",
        key="visibility",
        options=["About Transactions", "About Users"]
    )

    quarterly = st.checkbox("Select if you want to visualize quarterly", key="disabled")

    if visibility == "About Transactions" and not quarterly:
        st.write("To visualize top transaction data")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
        )

        mycursor = mydb.cursor(buffered=True)

        table_name = "top_trans"
        query = f"SELECT * FROM {table_name}"
        mycursor.execute(query)


        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()

        toptrans = pd.DataFrame(rows, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction_count',
                                          'Transaction_amount', 'Pincode_log', 'Transaction_count_log',
                                          'Transaction_amount_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Pincode','Transaction_count','Transaction_amount', 'Pincode_log', 'Transaction_count_log','Transaction_amount_log']
        st.write("For best visulatization : Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            fig = px.choropleth(toptrans,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Year',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)
    elif visibility == "About Transactions" and quarterly:
        st.write("To visualize quarterly transaction data")
        year_options = [2018,2019,2020, 2021, 2022]
        year_selection = st.selectbox("Select a year", year_options, key="year_selection")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
            )

        mycursor = mydb.cursor(buffered=True)
        table_name = "top_trans"
        query = f"SELECT * FROM {table_name} WHERE Year = '{year_selection}' "
        mycursor.execute(query)

        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()
        toptrans = pd.DataFrame(rows, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction_count',
                                               'Transaction_amount', 'Pincode_log', 'Transaction_count_log',
                                                'Transaction_amount_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Pincode','Transaction_count','Transaction_amount', 'Pincode_log', 'Transaction_count_log','Transaction_amount_log']
        st.write("For best visualization: Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            st.write(year_selection)
            fig = px.choropleth(toptrans,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Quarter',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)


    elif visibility == "About Users" and not quarterly:
        st.write("To Visualize top user data")
        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
        )

        mycursor = mydb.cursor(buffered=True)

        table_name = "top_user"
        query = f"SELECT * FROM {table_name}"
        mycursor.execute(query)


        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()

        topuser = pd.DataFrame(rows, columns=['State', 'Year', 'Quarter', 'Pincode', 'RegisteredUsers', 'Pincode_log','RegisteredUsers_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Pincode', 'RegisteredUsers', 'Pincode_log','RegisteredUsers_log']
        st.write("For best visulatization : Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            fig = px.choropleth(topuser,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Year',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)

    elif visibility == "About Users" and quarterly:
        st.write("To Visualize quarterly user data")
        year_options = [2018,2019,2020, 2021, 2022]
        year_selection = st.selectbox("Select a year", year_options, key="year_selection")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
            )

        mycursor = mydb.cursor(buffered=True)
        table_name = "top_user"
        query = f"SELECT * FROM {table_name} WHERE Year = '{year_selection}' "
        mycursor.execute(query)

        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()
        topuser = pd.DataFrame(rows, columns=['State', 'Year', 'Quarter', 'Pincode', 'RegisteredUsers', 'Pincode_log','RegisteredUsers_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Pincode', 'RegisteredUsers', 'Pincode_log','RegisteredUsers_log']
        st.write("For best visualization: Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            st.write(year_selection)
            fig = px.choropleth(topuser,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Quarter',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)

elif option =="All Data":
    visibility = st.radio(
        "Set the category of data",
        key="visibility",
        options=["About Transactions", "About Users"]
    )

    quarterly = st.checkbox("Select if you want to visualize quarterly", key="disabled")
    if visibility == "About Transactions" and not quarterly:
        st.write("To visualize Aggregated transaction data")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
        )

        mycursor = mydb.cursor(buffered=True)

        table_name = "agg_trans"
        query = f"SELECT * FROM {table_name}"
        mycursor.execute(query)


        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()

        aggtrans = pd.DataFrame(rows, columns=['Unnamed: 0',
                                               'State', 'Year', 'Quarter', 'Transaction_type','Transaction_count',
                                               'Transaction_amount', 'Transaction_count_log','Transaction_amount_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Transaction_type','Transaction_count','Transaction_amount', 'Transaction_count_log','Transaction_amount_log']
        st.write("For best visulatization : Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            fig = px.choropleth(aggtrans,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Year',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)
    elif visibility == "About Transactions" and quarterly:
        st.write("To visualize quarterly transaction data")
        year_options = [2018,2019,2020, 2021, 2022]
        year_selection = st.selectbox("Select a year", year_options, key="year_selection")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
            )

        mycursor = mydb.cursor(buffered=True)
        table_name = "agg_trans"
        query = f"SELECT * FROM {table_name} WHERE Year = '{year_selection}' "
        mycursor.execute(query)

        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()
        aggtrans = pd.DataFrame(rows, columns=['Unnamed_0',
                                               'State', 'Year', 'Quarter', 'Transaction_type','Transaction_count',
                                               'Transaction_amount', 'Transaction_count_log','Transaction_amount_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['Transaction_type','Transaction_count','Transaction_amount', 'Transaction_count_log','Transaction_amount_log']
        st.write("For best visualization: Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            st.write(year_selection)
            fig = px.choropleth(aggtrans,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Quarter',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)


    elif visibility == "About Users" and not quarterly:
        st.write("To Visualize Aggregated user data")
        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
        )

        mycursor = mydb.cursor(buffered=True)

        table_name = "agg_user"
        query = f"SELECT * FROM {table_name}"
        mycursor.execute(query)


        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()

        agguser = pd.DataFrame(rows, columns=['Unnamed_0', 'State', 'Year', 'Quarter', 'brands', 'Count','Percentage', 'Count_log', 'Percentage_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['brands', 'Count','Percentage', 'Count_log', 'Percentage_log']
        st.write("For best visulatization : Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            fig = px.choropleth(agguser,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Year',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)

    elif visibility == "About Users" and quarterly:
        st.write("To Visualize aggregated quarterly user data")
        year_options = [2018,2019,2020, 2021, 2022]
        year_selection = st.selectbox("Select a year", year_options, key="year_selection")

        # CONNECTING WITH MYSQL DATABASE
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="123412341234",
            database="phonepe_data"
            )

        mycursor = mydb.cursor(buffered=True)
        table_name = "agg_user"
        query = f"SELECT * FROM {table_name} WHERE Year = '{year_selection}' "
        mycursor.execute(query)

        # Fetch all the rows returned by the query
        rows = mycursor.fetchall()
        agguser = pd.DataFrame(rows, columns=['Unnamed_0', 'State', 'Year', 'Quarter', 'brands', 'Count','Percentage', 'Count_log', 'Percentage_log'])

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        selected_columns = ['brands', 'Count','Percentage', 'Count_log', 'Percentage_log']
        st.write("For best visualization: Unlock the power of visualization with logarithmically valued columns for stunning visual insights!")
        color_column = st.selectbox("Select a column for color", selected_columns)
        if st.button('Visualize'):
            st.write("Button clicked!")
            st.write(year_selection)
            fig = px.choropleth(agguser,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                animation_frame='Quarter',
                                color=color_column,
                                color_continuous_scale='Inferno',
                                title='Phonepe Pulse Data Visualization',
                                height=700
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)

        

    
    




    





    









