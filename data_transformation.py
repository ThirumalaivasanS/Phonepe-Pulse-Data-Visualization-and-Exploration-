import json
import plotly


csv_path = "/path/to/save/data.csv"

# Save the DataFrame as a CSV file
df.to_csv(csv_path, index=False)

#####################top_transactions
import os
import json
import pandas as pd

# Path to get the data as states from top/transaction folder
path = r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\top\transaction\country\india\state"
top_state = os.listdir(path)

# Initialize an empty list to store dictionaries
data_list = []

# Iterate over top_state, top_year, and top_year_list
for state in top_state:
    state_path = os.path.join(path, state)
    top_year = os.listdir(state_path)
    
    for year in top_year:
        year_path = os.path.join(state_path, year)
        top_year_list = os.listdir(year_path)
        
        for quarter in top_year_list:
            quarter_path = os.path.join(year_path, quarter)
            
            with open(quarter_path, 'r') as file:
                quarter_data = json.load(file)
            
            for district in quarter_data['data']['districts']:
                district_data = {
                    'State': state,
                    'Year': year,
                    'Quarter': int(quarter.strip('.json')),
                    'District_name': district['entityName'],
                    'Txn_count': district['metric']['count'],
                    'Txn_amount': district['metric']['amount']
                }
                data_list.append(district_data)

# Create a DataFrame from the list of dictionaries
top_transactionDM = pd.DataFrame(data_list)



#######################top users
import os
import json
import pandas as pd

# Path to get the data as states from top/user folder
data_path = r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\top\user\country\india\state"
top_user_states = os.listdir(data_path)

# To extract the data to create a dataframe
user_data = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Reg_name': [],
    'Reg_users': []
}

for state in top_user_states:
    state_path = os.path.join(data_path, state)
    top_user_years = os.listdir(state_path)

    for year in top_user_years:
        year_path = os.path.join(state_path, year)
        top_user_quarters = os.listdir(year_path)

        for quarter in top_user_quarters:
            quarter_path = os.path.join(year_path, quarter)
            with open(quarter_path, 'r') as file:
                data = json.load(file)

            for district in data['data']['districts']:
                region_name = district['name']
                reg_users = district['registeredUsers']
                user_data['Reg_name'].append(region_name)
                user_data['Reg_users'].append(reg_users)
                user_data['State'].append(state)
                user_data['Year'].append(year)
                user_data['Quarter'].append(int(quarter.strip('.json')))

# Create a dataframe
top_usersDM = pd.DataFrame(user_data)



######################aggre trans
import os
import json
import pandas as pd

# Path to get the data as states
data_path =r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\aggregated\transaction\country\india\state"
aggregated_states = os.listdir(data_path)

# To extract the data and sub_data to create a dataframe
transaction_data = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Txn_type': [],
    'Txn_count': [],
    'Txn_amount': []
}

for state in aggregated_states:
    state_path = os.path.join(data_path, state)
    aggregated_years = os.listdir(state_path)

    for year in aggregated_years:
        year_path = os.path.join(state_path, year)
        aggregated_year_list = os.listdir(year_path)

        for quarter in aggregated_year_list:
            quarter_path = os.path.join(year_path, quarter)
            with open(quarter_path, 'r') as file:
                data = json.load(file)

            for transaction in data['data']['transactionData']:
                txn_name = transaction['name']
                txn_count = transaction['paymentInstruments'][0]['count']
                txn_amount = transaction['paymentInstruments'][0]['amount']

                transaction_data['Txn_type'].append(txn_name)
                transaction_data['Txn_count'].append(txn_count)
                transaction_data['Txn_amount'].append(txn_amount)
                transaction_data['State'].append(state)
                transaction_data['Year'].append(year)
                transaction_data['Quarter'].append(int(quarter.strip('.json')))

# Create a dataframe
aggregated_transactionDM = pd.DataFrame(transaction_data)


#################map transactions
import os
import json
import pandas as pd

# Path to get the data as states from map/transaction folder
data_path =r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\map\transaction\hover\country\india\state"
map_states = os.listdir(data_path)

# To extract the data and sub_data to create a dataframe
transaction_data = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Region_name': [],
    'Txn_count': [],
    'Txn_amount': []
}

for state in map_states:
    state_path = os.path.join(data_path, state)
    map_years = os.listdir(state_path)

    for year in map_years:
        year_path = os.path.join(state_path, year)
        map_year_list = os.listdir(year_path)

        for quarter in map_year_list:
            quarter_path = os.path.join(year_path, quarter)
            with open(quarter_path, 'r') as file:
                data = json.load(file)

            for hover_data in data['data']["hoverDataList"]:
                region_name = hover_data['name']
                txn_count = hover_data["metric"][0]['count']
                txn_amount = hover_data["metric"][0]['amount']

                transaction_data['Region_name'].append(region_name)
                transaction_data['Txn_count'].append(txn_count)
                transaction_data['Txn_amount'].append(txn_amount)
                transaction_data['State'].append(state)
                transaction_data['Year'].append(year)
                transaction_data['Quarter'].append(int(quarter.strip('.json')))

# Create a dataframe
agg_map_transactionDM = pd.DataFrame(transaction_data)

#############agg user
import os
import json
import pandas as pd

data_list = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Brand_type': [],
    'Users_count': [],
    'Percentage': []
}

path = r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\aggregated\user\country\india\state"
Agg_user_state = os.listdir(path)

for state in Agg_user_state:
    state_path = os.path.join(path, state)
    Agg_user_year = os.listdir(state_path)    
    
    for year_folder in Agg_user_year:
        year_path = os.path.join(state_path, year_folder)
        quarter_list = os.listdir(year_path)        
        
        for quarter_file in quarter_list:
            quarter_path = os.path.join(year_path, quarter_file)
            data_file = open(quarter_path, 'r')
            data = json.load(data_file)
            
            if data['data'].get("usersByDevice") is not None:
                for device in data['data']["usersByDevice"]:
                    brand = device['brand']
                    count = device['count']
                    percentage = device['percentage']
                    
                    data_list['Brand_type'].append(brand)
                    data_list['Users_count'].append(count)
                    data_list['Percentage'].append(percentage)
                    data_list['State'].append(state)
                    data_list['Year'].append(year_folder)
                    data_list['Quarter'].append(int(quarter_file.strip('.json')))

df = pd.DataFrame(data_list)


#####################map  user
import os
import json
import pandas as pd

data_list = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Reg_name': [],
    'Reg_users': [],
    'App_opening': []
}

path =r"C:\Users\Hp\Desktop\Phonepe Pulse Data Visualization and Exploration\pulse\data\map\user\hover\country\india\state"
map_user_state = os.listdir(path)

for state in map_user_state:
    state_path = os.path.join(path, state)
    map_user_year = os.listdir(state_path)    
    
    for year_folder in map_user_year:
        year_path = os.path.join(state_path, year_folder)
        year_list = os.listdir(year_path)        
        
        for quarter_file in year_list:
            quarter_path = os.path.join(year_path, quarter_file)
            data_file = open(quarter_path, 'r')
            data = json.load(data_file)
            
            for region_name in data['data']["hoverData"]:
                reg_users = data['data']["hoverData"][region_name]['registeredUsers']
                app_opens = data['data']["hoverData"][region_name]['appOpens']
                
                data_list['App_opening'].append(app_opens)
                data_list['Reg_name'].append(region_name)
                data_list['Reg_users'].append(reg_users)
                data_list['State'].append(state)
                data_list['Year'].append(year_folder)
                data_list['Quarter'].append(int(quarter_file.strip('.json')))

df = pd.DataFrame(data_list)

