label fact
	org 64
	ldo 1     
	mva      
	const 1   
	le        
	brf fact_else  
	const 1 
	ret
label fact_else
	ldo 1     
	mva      
	const 1    
	sub        
	push       
	call fact 1
	ldo 1
	mva
	pop
	mul
	ret 