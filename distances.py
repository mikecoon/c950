import datetime
import csv

#Read in distance and address csv files
with open('csv_files/distance.csv') as csv_distance:
    distance_csv = csv.reader(csv_distance, delimiter=',')
    distance_csv = list(distance_csv)
with open('csv_file/address.csv') as csv_address:
    address_csv = csv.reader(csv_distance, delimiter=',')
    address_csv = list(address_csv)

    #Compute the total distance
    def get_total_distance(col_val, row_val, sum_val):
        d = distance_csv[row_val][col_val]
        if not d:
            d = distance_csv[col_val][row_val]
        sum_val += d
        return float(sum_val)
    
    #Compute the current distance
    def get_current_distance(col_val, row_val):
        d = distance_csv[row_val][col_val]
        if not d:
            d = distance_csv[col_val][row_val]
        return float(d)

    def get_address():
        return address_csv
    
    def get_time_left(distance, Truck):
        pass