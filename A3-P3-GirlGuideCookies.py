#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0425777   
#Student Name: Katherine

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    GuideName=[]
    Cookies=[]
    #Lists

    def GetGuides(): 
        GG=input("\nEnter the number of guides selling cookies: ")
        return int(GG)
    
    Guides=GetGuides()

    for i in range(Guides):
        def GetName(i): 
            GN=input(f"\nEnter the name of guide #{i}: ")
            return GN
        GuideName.append(GetName(i+1))

    #i tried to make the name and boxes sold print at the smae time but it messed with the out so I left it like this
    for i in range(len(GuideName)):
        Ck=input("\nEnter the number of boxes sold by {0}: ".format(GuideName[i]))
        Cookies.append(Ck)

    for i in range(len(Cookies)):
        Cookies[i] = float(Cookies[i])
    
    Avg= sum(Cookies) / Guides

    print("\nThe average number of boxes sold by each guide was {0:.1f}".format(Avg))
    
    print("\nGuide\t\t\tPrizes Won")
    print("-"*100)

    Max= max(Cookies)

    #output prizes by comparing Cookies list and using names list in output
    for i in range(len(GuideName)):
        if Cookies[i] == 0:
            print("{0}\t\t\t-".format(GuideName[i]))
        elif (Cookies[i] > 0) and (Cookies[i] < Avg):
            print("{0}\t\t\t-Left over cookies".format(GuideName[i]))
        elif (Cookies[i] > Avg) and (Cookies[i] < Max):
            print("{0}\t\t\t-Super Seller Badge".format(GuideName[i]))
        elif Cookies[i] == Max:
            print("{0}\t\t\t-Trip to Girl Guide Jamboree in Aruba".format(GuideName[i]))

    #if max the index of the cookies and the names if they they meet the require ment print the name then a the phrase





    # YOUR CODE ENDS HERE

main()