from __future__ import annotations
from typing import Union
import pandas as pd
import sqlite3

class Dataman:
    """Data manager manages data exchange between the app and the database"""
    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
    
    def add_product(self, product_data) -> bool:
        """Add a new product to the products table using given **product_data**"""
        raise NotImplementedError

    def get_products(self) -> list[str]:
        """Returns a list of the products from the products table"""
        try:
            df = pd.read_sql("SELECT * FROM Products", sqlite3.connect(self.connection_string))
            return list(df["ProductName"].unique())
        except pd.errors.DatabaseError:
            print("Unable to fetch products from the database")

        return ['Database Error']

    def get_items_of_product(self, product_name: str) -> list[int]:
        """ Returns list of available **Serial Number** of given **product_name**
        """
        df = pd.read_sql("SELECT SerialNumber, DateReceived FROM log WHERE ProductName=? AND DateWithdrawn IS NULL", 
                         sqlite3.connect(self.connection_string), 
                         params=[product_name])
        df.sort_values(by=['DateReceived'], inplace=True)

        list_numbers = list(df["SerialNumber"])
        return list_numbers if list_numbers else ["Not in Stock"]
    
    def receive_product(self, product_data: dict[str, Union[str, int]]) -> int:
        """Logs a received product and returns the order_num
        
        Pre-conditions:
            *product_data* is a valid receive product dictionary
        """
        
        ### Step 1 ###
        # Compute the Serial Number (index of this entry in given Product)
        # For example: If there are 3 entries of HCl, new entry will have serial number 4
        count_df = pd.read_sql("SELECT SerialNumber FROM Log WHERE ProductName=?", 
                            sqlite3.connect(self.connection_string), 
                            params=[product_data["ProductName"]])

        if len(count_df):
            new_item_number = count_df.max().iloc[0] + 1
        else:
            new_item_number = 1
        product_data["SerialNumber"] = new_item_number

        ### Step 2 ###
        # reconfigure the data to allow insertion into database

        #: The columns we need to update in the database
        data_columns = [
            "SerialNumber",
            "ProductName",
            "ReceivedBy",
            "Certificate",
            "DateReceived",
            "LotNumber"
            ]
        
        #: Values corresponding to columns as defined in *data_columns*
        data_values = [product_data[item] for item in data_columns]

        #: New entry in the form of a dataframe.
        # Creating a dataframe enables us to use pandas to handle SQL INSERT
        df = pd.DataFrame.from_dict({0: data_values}, orient='index', columns=data_columns)

        ### Step 3 ###
        # push data to the databse
        df.to_sql("log", con=sqlite3.connect(self.connection_string), if_exists="append", index=False)

        return new_item_number

    def withdraw_product(self, product_data: dict[str, Union[str, int]]) -> bool:
        """Withdraw the oldest availble product that matches the given *product_data*"""

        ## Step 1 ##
        # Create the query structure
        qry = "UPDATE log SET DateWithdrawn=?, WithdrawnBy=? WHERE ProductName=? AND SerialNumber=?"
        
        ## Step 2 ##
        # Execute the query
        success = True
        with sqlite3.connect(self.connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute(qry, 
                           [product_data["DateWithdrawn"], 
                            product_data["WithdrawnBy"], 
                            product_data["ProductName"], 
                            product_data["SerialNumber"]])
            
            try:
                conn.commit()
                if cursor.rowcount == 1:
                    success = True
            except sqlite3.IntegrityError as exc:
                print(f"Unable to withdraw {product_data['ProductName']}-{product_data['SerialNumber']}")

        return success

if __name__ == "__main__":
    dataman = Dataman("site.db")
    # product_data = {"name": "CAP-X", "ReceivedBy": "python", "Certificate": "YESS", "DateReceived":"2024-03-30", "LotNumber":299}
    product_data = ["CAP-X", "python", "NO", "2024-04-31", 123]
    p = dataman.receive_product(product_data)
    print(p)
