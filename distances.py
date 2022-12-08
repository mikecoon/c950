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

    #Return the packages assigned adresses
    def get_address():
        return address_csv
    
    def get_time_left(distance, truck):
        distance = '{0:02.0f}:{1:02.0f}'.format(*divmod((distance/18)*60,60)) + ':00'
        truck.append(distance)
        remainder = datetime.timedelta()
        for time in truck:
            (h,m,s)=time.split(':')
            remainder += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        return remainder




