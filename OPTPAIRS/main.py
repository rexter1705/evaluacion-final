for _ in range(int(input())):
	n = int(input())
	c=0
	i=2
	while(i*i<=n):
	    if(n%i==0):
	        if(i==n/i):
	            c+=1
	        else:
	            c+=2
	    i+=1
	c+=1
	if(n%2==0):
	    print(c*2-1)
	else:
	    print(c*2)
