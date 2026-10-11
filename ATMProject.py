#ATMProject.py

#ATMMenu
def menu():
    print("-"*50)
    print("ATM OPeration / Fund Transfer Flow Application")
    print("-"*50)
    print("\t1.Deposit")
    print("\t2.Withdraw")
    print("\t3.Balance Enquiry")
    print("\t4.Exit")
    print("-"*50)

# ATMExcept 
class DepositError(Exception): pass
class WithDrawError(Exception): pass
class InsuffFundError(Exception): pass


#ATMOperations
from ATMExcept import DepositError,WithDrawError,InsuffFundError
bal=500.0
def deposit():
    damt=float(input("Enter UR Deposit Amount:"))
    if (damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR ACCO1UNT XXXXXXXXXX44 CREDITED WITH INR:{}".format(damt))
        print("\tUR ACCOUNT XXXXXXXXXX44 BALANCE AFTER DEPOSIT INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter UR Withdraw Amount:"))
    if (wamt<=0):
        raise WithDrawError
    elif ((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-wamt
        print("\tUR ACCOUNT XXXXXXXXXX44 DEBITED WITH INR:{}".format(wamt))
        print("\tNOW UR ACCOUNT XXXXXXXXXX44 BALANCE AFTER WITHDRAW INR:{}".format(bal))
def balenq():
    print("\tNOW UR ACCOUNT XXXXXXXXX44 BALANCE IS INR:{}".format(bal))



#ATMOperationsDemo <--Main Project
from ATMExcept import DepositError,WithDrawError,InsuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from builtins import ValueError
while(True):
    try:
        menu()
        ch=int(input("\tEnter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                        print("\tDONT ENTER -VE / ZERO AMOUNT FRO DEPOSIT")
                except ValueError:
                        print("\tDONT ENTER ALNUMS/STRS/ AND SYMBOLS FOR DEPOSIT")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDONT ENTER -VE / ZERO AMOUNT FRO WITHDRAW")
                except InsuffFundError:
                    print("\tUR ACCOUNT DOSE NOT HAVE SUFF FUNDS FIXED IN THIS AMOUNT")
                except ValueError:
                    print("\tDONT ENTER ALNUMS/STRS/ AND SYMBOLS FOR DEPOSIT")
            case 3:
                balenq()
            case 4:
                print("\tTHX FOR USING THIS PROGRAM")
                break
            case _:
                print("\tUE SELECTION OF OPERATION IS WRONG--TRY AGAIN")
    except ValueError:
        print("\tDONT ENTER ALNUMS/STRS/ AND SYMBOLS FOR CHOICE--TRY AGAIN")
