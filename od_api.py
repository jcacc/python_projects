import json
import requests
import os

od_Store_ID = os.environ.get('OD_STORE')
od_API_Key = os.environ.get('OD_API')

def od_FetchStore():
  od_Store_URL = "https://app.orderdesk.me/api/v2/store"
  od_Store_Headers = {
      "ORDERDESK-STORE-ID": od_Store_ID,
      "ORDERDESK-API-KEY": od_API_Key,
      "Content-Type": "application/json"
  }
  store_Response = requests.get(od_Store_URL,headers=od_Store_Headers).json()
  print(store_Response)

def od_FetchInventory():
  od_InventoryURL = "https://app.orderdesk.me/api/v2/inventory-items/"
  od_Inv_Headers = {
    "ORDERDESK-STORE-ID": od_Store_ID,
    "ORDERDESK-API-KEY": od_API_Key,
    "Content-Type": "application/json"
  }
  inv_Response = requests.get(od_InventoryURL,headers=od_Inv_Headers).json()
  print(inv_Response)

def od_FetchInventory(od_itemNumber):
  od_InventoryItemURL = "https://app.orderdesk.me/api/v2/inventory-items/" + str(od_itemNumber)
  od_Inv_Headers = {
    "ORDERDESK-STORE-ID": od_Store_ID,
    "ORDERDESK-API-KEY": od_API_Key,
    "Content-Type": "application/json"
  }
  invItem_Response = requests.get(od_InventoryItemURL,headers=od_Inv_Headers).json()
  print(invItem_Response)

def od_NewInventoryItem():
  od_newItemURL = "https://app.orderdesk.me/api/v2/inventory-items/"
  od_new_Item_Headers = {
    "ORDERDESK-STORE-ID": od_Store_ID,
    "ORDERDESK-API-KEY": od_API_Key,
    "Content-Type": "application/json"
  }
  od_new_Item_Description = {
    "name": "Three Wolf Moon T-Shirt"
  }
  new_Item_Response = requests.post(od_newItemURL,headers=od_new_Item_Headers,json=od_new_Item_Description)()
  print(new_Item_Response)


