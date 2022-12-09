from load_trucks import *
import datetime

def main():
    print("Welcome to WGUPS!!")
    print("1. Print Total Mileage")
    print("2. Get All Packages at a single time.")
    print("3. Get A Specific package at a single time.")
    print("4. Exit the Program")
    while True:
        try:
            i = int(input("Please enter one of the following options [1,2,3,4]: "))
            match i:
                case 1:
                    print(f'Total distance traveled is {get_total_distance():.2f} miles.\n')
                case 2:
                        try:
                            time = input('Enter time in (HH:MM:SS) format: ')
                            (h, m, s) = time.split(':')
                            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                            for i in range(1, 41):
                                try:
                                    ftime = hm.search(i)
                                    print(i,ftime)
                                except:
                                    pass
                        except:
                            print('Invalid input, try again.')
                case 3:
                        pass
                case 4:
                    print('Have a good day.')
                    break

        except:
            print('Invalid input, try again.')
                



if __name__ == "__main__":
    main()