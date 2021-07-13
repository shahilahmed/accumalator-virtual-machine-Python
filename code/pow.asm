label pow
	org 2345
	ldo 1     
	mva      
	const 0   
	le        
	brf pow_else  
	const 1 
	ret
label pow_else
	ldo 1
	mva
	const 1
	sub
	push
	ldo 2
	push
	call pow 2
	pop
	mva
	ldo 2
	mul
	ret