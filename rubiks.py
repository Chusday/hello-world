#Dylan Chu
#4/21/16
#CMSC443
#This program represents a 3d transposition cipher, as represented by a rubiks cube

import numpy as np
#arr = the array to rotate
#face = the face to move
#This function has each rotation hard coded into a 1d array
#Basically you pass in a 1D representation of your rubik's cube and this function will rotate the given face 1 rotation in the clockwise direction
#returns: the rotated array
def rotate (arr, face):
        if face == "F":
            order = [6, 3, 0, 7, 4, 1, 8, 5, 2, 42, 10, 11, 43, 13, 14, 44, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 45, 30, 31, 46, 33, 34, 47, 36, 37, 38, 39, 40, 41, 35, 32, 29, 15, 12, 9, 48, 49, 50, 51, 52, 53]
        elif face == "R":
            order = [0, 1, 47, 3, 4, 50, 6, 7, 53, 15, 12, 9, 16, 13, 10, 17, 14, 11, 44, 19, 20, 41, 22, 23, 38, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 2, 39, 40, 5, 42, 43, 8, 45, 46, 24, 48, 49, 21, 51, 52, 18]
        elif face == "B":
            order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 53, 12, 13, 52, 15, 16, 51, 24, 21, 18, 25, 22, 19, 26, 23, 20, 38, 28, 29, 37, 31, 32, 36, 34, 35, 11, 14, 17, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 27, 30, 33]
        elif face == "L":
            order = [36, 1, 2, 39, 4, 5, 42, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 51, 21, 22, 48, 24, 25, 45, 33, 30, 27, 34, 31, 28, 35, 32, 29, 26, 37, 38, 23, 40, 41, 20, 43, 44, 0, 46, 47, 3, 49, 50, 6, 52, 53]
        elif face == "U":
            order = [9, 10, 11, 3, 4, 5, 6, 7, 8, 18, 19, 20, 12, 13, 14, 15, 16, 17, 27, 28, 29, 21, 22, 23, 24, 25, 26, 0, 1, 2, 30, 31, 32, 33, 34, 35, 42, 39, 36, 43, 40, 37, 44, 41, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53]
        elif face == "D":
            order = [0, 1, 2, 3, 4, 5, 33, 34, 35, 9, 10, 11, 12, 13, 14, 6, 7, 8, 18, 19, 20, 21, 22, 23, 15, 16, 17, 27, 28, 29, 30, 31, 32, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 48, 45, 52, 49, 46, 53, 50, 47]
        else:
            print("Error. Move not recognised.")
        newOrder = [arr[x] for x in order]
        return newOrder
    
#A helper function that takes in user input
#returns the plaintext(max 54 characters) and the rotation key    
def takeInput():
    pt = input("Enter Plaintext: ")
    print("We will use the following notation for rotations: F = front rotate, R = right rotate, B = back, L = left, U = up, D = down")
    print("Each letter represents ONE(1) clockwise rotation of that face.")
    print("Please place a space in between each letter")
    key= input("Enter moves: ")
    key = key.upper()
    return pt, key

#function that cuts a string into substrings of a certain length
def cutstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

#main method driver
def main():
    opt, key = takeInput()
    pts = cutstring(opt,54)#take in input

    
    
    for pt in pts:
        #pad the plaintext to 54 characters if it's not a full block
        pt = pt.ljust(54,'X')
        print("Start of block")
        print("The plaintext will be padded with X's")
        print(pt)
        ptlisted = list(pt)

        keysplit = key.split()#turn the key into a list 
        decryptkey = [] 
        print("The encryption key is: ", keysplit) #display the key
        for i in keysplit[::-1]: #this loop reverses the key
            if (i == "D"):
                decryptkey.append("D")
                decryptkey.append("D")
                decryptkey.append("D")
            if (i == "F"):
                decryptkey.append("F")
                decryptkey.append("F")
                decryptkey.append("F")
            if (i == "R"):
                decryptkey.append("R")
                decryptkey.append("R")
                decryptkey.append("R")
            if (i == "L"):
                decryptkey.append("L")
                decryptkey.append("L")
                decryptkey.append("L")
            if (i == "B"):
                decryptkey.append("B")
                decryptkey.append("B")
                decryptkey.append("B")
            if (i == "U"):
                decryptkey.append("U")
                decryptkey.append("U")
                decryptkey.append("U")

        print("The decryption key is: ", decryptkey)#print the decryption key


        print("This is the original cube")#display the original cube
        arr = np.asarray(ptlisted)
        arr = arr.reshape((6,3,3))
        print(arr)

        print("--------------")
        print("Encrypted rubik's cube: ")#rotate and display the encrypted cube
        for x in keysplit:
            ptlisted = rotate(ptlisted,x)


        arr = np.asarray(ptlisted)
        arr = arr.reshape((6,3,3))   
        print(arr)
        print("Ciphertext as a string")
        print(''.join(ptlisted))

        print("---------------")
        print("Decrypted rubik's cube: ")#rotate and display the decrypted cube
        for x in decryptkey:
            ptlisted = rotate(ptlisted,x)

        arr = np.asarray(ptlisted)
        arr = arr.reshape((6,3,3))   
        print(arr)
        print("Decrypted plaintext:")
        dept = ''.join(ptlisted)

        print(dept)
        print("------------------")

    
main()
