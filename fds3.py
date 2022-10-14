def read(p,k,w,q,mat1,mat2):
    print("enter for mat 1 :")
    for i in range (p):
        a=[]
        for j in range (k):
            a.append(int(input("enter the value : ")))
        mat1.append(a)
    print("enter for mat 2 :")

    for i in range (w):
        a=[]
        for j in range (q):
            a.append(int(input("enter the value : ")))
        mat2.append(a)
def disp(p,k,w,q,mat1,mat2):
    print("mat 1")

    for i in range (p):
        for j in range (k):
            print(mat1[i][j],end=" ")
        print()
    print("mat 2")
    for i in range (w):
        for j in range (q):
            print(mat2[i][j],end=" ")
        print()
def addition(p,k,w,q,mat1,mat2):
    sum=[]
    if(p==w) and (k==q):
            for i in range (p):
                t=[]
                for j in range (k):
                    t.append(mat1[i][j]+mat2[i][j])
                sum.append(t)
            print("addition of two matrices is :")
            for i in range (w):
                for j in range (q):
                    print(sum[i][j],end=" ")
                print()
    else:
        print("addition of two matrix is not possible :")
def subtraction(p,k,w,q,mat1,mat2):
    sub=[]
    if(p==w) and (k==q):
            for i in range (p):
                t=[]
                for j in range (k):
                    t.append(mat1[i][j]-mat2[i][j])
                sub.append(t)
            print("subtraction of two matrices is :")
            for i in range (w):
                for j in range (q):
                    print(sub[i][j],end=" ")
                print()
    else:
        print("subtraction of two matrix is not possible :")
def transpose(p,k,w,q,mat1,mat2):
    print("enter the transpose of matrix you want :")
    print("press:1=matrix 1\npress:2=matrix 2")
    ch=int(input("enter your choice"))
    if(ch==1):   
      print("The transpose of matrix 1 is ")
      for i in range (p):
                for j in range (k):
                    print(mat1[j][i],end=" ")
                print()
    if(ch==2):   
     print("The transpose of matrix 2 is ")
     for i in range (w):
                for j in range (q):
                    print(mat2[j][i],end=" ")
                print()
def multiplication(p,k,w,q,mat1,mat2):
    if(k==w):
        
        multi=[]
        for i in range (p):
            a=[]
            for j in range (q):
                sum1=0
                for n in range (k):
                    mut= mat1[i][n] * mat2[n][j]
                    sum1=sum1+mut
                a.append(sum1)
            multi.append(a)
            
    
        print("The multiplication of matrix  is :")
        for i in range (p):
                for j in range (q):
                    print(multi[i][j],end=" ")
                print()

p=int(input("enter th number of rows in mat 1 :"))
k=int(input("enter th number of col in mat 1 :"))
mat1=[]
mat2=[]
w=int(input("enter th number of rows in mat 2 :"))
q=int(input("enter th number of col in mat 2 :"))
            
read(p,k,w,q,mat1,mat2)
disp(p,k,w,q,mat1,mat2)
while(True):
 print("press:1=addition,press:2=subtraction,press:3=transpose,press:4=multiplication")
 n=int(input("enter the choice :"))
 if(n==1):
  addition(p,k,w,q,mat1,mat2) #addition of two number 
 if(n==2):
  subtraction(p,k,w,q,mat1,mat2)#subtraction of two number 
 if(n==3):
  transpose(p,k,w,q,mat1,mat2)#transpose of two number 
 if(n==4):
  multiplication(p,k,w,q,mat1,mat2)#multiplication of two number 
 else:
     print("you have entered the wrong choice :")
