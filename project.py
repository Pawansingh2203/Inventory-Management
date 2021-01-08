import sqlite3
import matplotlib.pyplot as plt
print("                                         I N V E N T R Y     M A N A G  E M E N T     S Y S T E M                                                         \n")
db=sqlite3.connect('Inventry')
cur=db.cursor()
qry="create table if not exists Product( ProductId integer primary key,ProductName TEXT(30),PurchasePrice integer,SalePrice decimal(8,2),ProductQty integer)"
cur.execute(qry)

print("                                                              DATABASE ACCESED\n")






qry="create table if not exists Sale( ProductId integer forign key,saleid int,price decimel(8,2),date date)"
cur.execute(qry)







db.commit()
db.close()

while(True):
        db=sqlite3.connect('Inventry')
        cur=db.cursor()
        print("     MAIN MAENU\n")
        ch1=int(input("Enter 1 to Manage Stock\nEnter 2 for Sale Option\nEnter 3 to Manage Product\nEnter 4 to view Profit Details\nEnter 5 to LogOut\n "))
        if(ch1==1):
                print("   MANAGE STOCK\n")
                ch2=int(input("Enter 1 to Update Product Quantity in stock\nEnter 2 to View Stock\nEnter 3 to go to MAIN MENU\n"))
                if(ch2==1):
                        id=int(input("Enter the product id to update the priduct Quantity\n"))
                        qty=int(input("Enter the new  priduct Quantity\n"))
                        qry = "UPDATE Product SET ProductQty = ? WHERE ProductId = ?"
                        cur.execute(qry,(qty,id))
                        qry="select* from Product"
                        cur.execute(qry)
                        result=cur.fetchall()
                        for row in result:
                              print(row)

                elif(ch2==3):
                        pass

                else:
                    qry="select* from Product"
                    cur.execute(qry)
                    result=cur.fetchall()
                    for row in result:
                            print(row)
                              


                              
        elif(ch1==2):
                 print("     SALES OPTION\n")
                 ch2=int(input("Enter 1 to Insert Product Sale Details\nEnter 2 to Update Product Sale Details\nEnter 3 to View Product Sale Details\nEnter 4 for MAIN MENU\n"))
                 if(ch2==1):

                        qry = "INSERT INTO Sale (ProductId,saleid,price,date) VALUES (?,?,?,?)"
                        Pid=int(input("Enter the product id"))
                        sid=input("Enter the sale id")
                        pr=float(input("Enter the price"))
                        d=input("Enter the date")

                        if(cur.execute(qry,(Pid,sid,pr,d))):
                            print("Record Inserted")
                        
                    
                 elif(ch2==2):
                        id=int(input("Enter the product id to update the priduct Quantity\n"))
                        si=int(input("Enter the new  sale id\n"))
                        pr=float(input("Enter the new  price\n"))
                        da=input("Enter the new  date\n")
                        qry = "UPDATE Sale SET saleid=?,price=? ,date=? WHERE ProductId =?"
                        cur.execute(qry,(si,pr,da,id))
                
                 elif(ch2==4):
                         pass               
                

                 else:
                    qry="select* from Sale"
                    cur.execute(qry)
                    result=cur.fetchall()
                    for row in result:
                            print(row)




        elif(ch1==3): 
                ch2=int(input("Enter 1 to Add New Product\nEnter 2 to View All Products\nEnter 3 to Remove Product\nEnter 4 to go to MAIN MENU\n"))
                if(ch2==1):
                        qry = "INSERT INTO Product(ProductId,ProductName,PurchasePrice,SalePrice,ProductQty) VALUES (?,?,?,?)"
                        Pid=int(input("Enter the product id\n"))
                        pn=input("Enter the Product Name\n")
                        pp=int(input("Enter the Purchase price\n"))
                        sp=int(input("Enter the Sales Price\n"))
                        pq=int(input("Enter the ProductQty\n"))
                        if(cur.execute(qry,(Pid,pn,pp,sp))):
                            print("Record Inserted")



                elif(ch2==2):
                    qry="select* from Product"
                    cur.execute(qry)
                    result=cur.fetchall()
                    for row in result:
                            print(row)


                elif(ch2==4):
                        pass
        
                else:
                    id=int(input("Enter the productId to be removed\n"))
                    qry = "DELETE FROM Product WHERE ProductId =? "
                    if(cur.execute(qry,(id,))):
                            print("Deleted sucessfully")
    


        elif(ch1==4):
              l1=[]
              l2=[]
              qry="select saleid ,Product.ProductId,ProductName,date,ProductQty,(SalePrice-PurchasePrice)*ProductQty FROM Product join Sale where Product.ProductId=Sale.ProductId"
              cur.execute(qry)
              res3=cur.fetchall()
              for row in res3:
                      print(row[2],row[5])
                      l1.append(row[2])
                      l2.append(row[5])
              ch=input("Do you want to view Fraphical Data\n")
              if(ch=='Y' or ch=='y'):
                      plt.bar(l1,l2,label="PROFIT",width=.35,color='white',edgecolor='black')
                      plt.legend()
                      plt.grid()
                      print(plt.show())
              else:
                      pass

        else:
             print("Logging Off\n")
             exit()
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        db.commit()
        db.close()

                 
       
            
                
