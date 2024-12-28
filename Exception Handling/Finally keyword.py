def func1():
    try:
        a=[2,5,6,7,8,9]
        b=int(input("Enter the Index : "))
        print(a[b])
        return 1
    except:
        print("Error Occured Due To Wrong Input")
        return 0
    
    finally:
        print("This Will Executed anyway")  # Executes anyway 

    print("This will not executed always") # Runs only if execution reaches

x = func1()

print(x)
