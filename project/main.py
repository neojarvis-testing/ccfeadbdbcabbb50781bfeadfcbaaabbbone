        print("1.Add a hotel")
        print("2.Delete a hotel")
        print("3.Update hotel rating")
        print("4.View all hotels")
        print("5.Search hotels")
        print("6.Exit")
        menu = input()

        if(menu=="1"):#add hotel
            hotels_.append(add_hotel())
        elif(menu=="2"): #delete hotel
            delete_hotel(hotels_)
        elif(menu=="3"): #update hotel rating
            update_rating(hotels_,FILENAME)
        elif(menu=="4"): #fetching all hotels
            fetch_hotel(hotels_)
        elif(menu=="5"): #search hotels
            find_hotel(hotels_)
        elif(menu=="6"):#exit from hotel
            save_hotels(hotels_,FILENAME)
            print("Exited")
            break
        else:
            print("Invalid choice")

if __name__=="__main__": main()