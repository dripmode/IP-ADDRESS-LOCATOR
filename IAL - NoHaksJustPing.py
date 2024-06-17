import json
import urllib.request
import webbrowser
import os

R = "\033[91m"
Y = "\033[93m"
G = "\033[92m"
CY = "\033[96m"
W = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    clear_screen()
    print(CY + """
____________________________________________________________
    """ + R + """      IAL (IP ADDRESS LOCATOR) """ + CY + """v1""" + CY + """
""" + R + """    >>""" + Y + """------------------------------------------------""" + CY + """
        dev - nohaksjustping | https://github.com/dripmode
""" + Y + """    ------------------------------------------------<<""" + R + """
____________________________________________________________
""")

def menu():
    try:
        while True:
            print(R + """
#""" + Y + """ Select option""" + G + """ >>""" + Y + """
1)""" + Y + """ Check your IP info""" + Y + """
2)""" + Y + """ Check other IP info""" + Y + """
3)""" + Y + """ Exit
""")
            choice = input(CY + "Enter Your choice: " + W).strip()
            
            if choice == '1':
                main2()
            elif choice == '2':
                main()
            elif choice == '3':
                print(Y + "Exit................" + W)
                break
            else:
                print(R + "\nInvalid choice! Please try again\n")
    except KeyboardInterrupt:
        print(Y + "\nInterrupted! Have a nice day :)" + W)

def ip_finder(url):
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)

        print(R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(Y + '\n>>>' + CY + ' IP address details\n ')
        print(G + "1) IP Address : " + Y, data['query'], '\n')
        print(G + "2) Org        : " + Y, data['org'], '\n')
        print(G + "3) City       : " + Y, data['city'], '\n')
        print(G + "4) Region     : " + Y, data['regionName'], '\n')
        print(G + "5) Country    : " + Y, data['country'], '\n')
        print(G + "6) Location\n")
        print(G + "\tLatitude   : " + Y, data['lat'], '\n')
        print(G + "\tLongitude  : " + Y, data['lon'], '\n')
        
        google_maps_link = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
        print(R + "\n#" + Y + " Google Map link : " + CY, google_maps_link)
        
        if os.name == 'posix':
            link = 'am start -a android.intent.action.VIEW -d ' + google_maps_link
            pr = input(R + "\n>>" + Y + " Open link in browser? (y|n): " + W)
            if pr.lower() == "y":
                os.system(link + " > /dev/null")
            elif pr.lower() != "n":
                print(R + "\nInvalid choice! Please try again\n")
        else:
            pr = input(R + "\n>>" + Y + " Open link in browser? (y|n): " + W)
            if pr.lower() == "y":
                webbrowser.open(google_maps_link, new=0)
        
    except urllib.error.URLError:
        print(R + "\nError! Please check your internet connection!\n" + W)
    except KeyError:
        print(R + "\nError! Invalid IP/Website Address!\n" + W)

def main():
    try:
        u = input(G + "\n>>> " + Y + "Enter IP Address/website address: " + W).strip()
        if u == "":
            print(R + "\nEnter valid IP Address/website address!")
        else:
            url = 'http://ip-api.com/json/' + u
            ip_finder(url)
    except KeyboardInterrupt:
        print(Y + "\nInterrupted! Have a nice day :)" + W)

def main2():
    try:
        url = 'http://ip-api.com/json/'
        ip_finder(url)
    except KeyboardInterrupt:
        print(Y + "\nInterrupted! Have a nice day :)" + W)

if __name__ == "__main__":
    start()
    menu()
