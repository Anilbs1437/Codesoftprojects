 
import random    
                     
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    
    selected_char = random.sample(list_of_chars, len)  
    pass_str = "".join(selected_char)  
    return pass_str  

if __name__ == "__main__":  
    while True:  
        userSelection = input("Do you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")  
        if userSelection == 'N' or userSelection == 'n':  
            print("Thank You! See you next time.")  
            break 
        
        elif userSelection == 'Y' or userSelection == 'y':  
            len = int(input("Enter the length of the Password: "))  
            pass_str = generate_password(len) 
            print("A randomly generated Password is:", pass_str)  
            print("")   
            
        else: 
            print("Invalid Input! Try Again.")  
            print("") 
            
  
        
  
            
              
            
             
  
            
             
  
          
        
