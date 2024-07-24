import csv
from datetime import datetime

def main():
  
  KEY_COLUMN_INDEX = 0
  product_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
  print("7Evelyn Store")


  try:
    with open("request.csv") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        total_num = 0
        total_quan = 0
        total_per = 0
        subtotal = 0
        discount = .10
        
        for prod_num in reader:
            prod_num_1 = prod_num[0]
            prod_num_2 = int(prod_num[1])
            total_num += prod_num_2
            
            if prod_num_1 in product_dict:
                value = product_dict[prod_num_1]
                product = value[1]
                price = float(value[2])
                total_quan += price
                total_per = prod_num_2 * price
                subtotal += total_per
                tax = subtotal*.06
                print(f"{product}: {prod_num_2} @ {price} ")
                

    print(f"Number of Items: {total_num} ")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {subtotal+tax:.2f}")
    print(f"Thank you for shopping at the 7Evelyn Store.")
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %H:%M:%S %Y}")


    if current_date_and_time.weekday() == 1 or current_date_and_time.weekday() == 2:
       discount_day = subtotal+(subtotal*discount)
       print(f"Discounted Price: {discount_day:.2f} when either Tuesday of Wednesday ")
    # elif: 
  except FileNotFoundError as not_found_err:
    print(not_found_err)
  except KeyError as key_err:
    print(type(key_err).__name__, key_err)


def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  try:
    compound_dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                compound_dictionary[key] = row
  except FileNotFoundError as not_found_err:
    print(f"{not_found_err}")
  except PermissionError as perm_err:
    print(f"{perm_err}")
  return compound_dictionary 



if __name__ == "__main__":
    main()