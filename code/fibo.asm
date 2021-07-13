label fibo
	org 987
	ldo 1     
	mva      
	const 1   
	le        
	brf fibo_else  
	const 1 
	ret
label fibo_else
	ldo 1     
	mva      
	const 1    
	sub        
	push       
	call fibo 1
	ldo 1  
	mva       
	const 2    
	sub       
	push      
	call fibo 1
	pop       
	mva       
	pop       
	add       
	ret 