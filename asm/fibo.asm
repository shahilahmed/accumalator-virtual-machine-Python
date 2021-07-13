start main
	org 2
  
label loop
	ent 4
	const 1
	sto 1
	const 10
	sto 2
	const 0
	sto 3
	const 0
	sto 4
  
label loop_start
	ldo 1
	mva
	ldo 2
	le
	brf loop_end
	const 5
	push
	ldo 1
	push
	call pow 2
	pop
	sto 4
	print
	const 32
	out
	ldo 3
	mva
	ldo 4
	add
	sto 3
	ldo 1
	inc
	sto 1
	br loop_start
label loop_end	
	call println 0
	call println 0
	ldo 3
	print
	call println 0
	call println 0
	ret
label println
	const 10
	out
	ret
  
label main
	const 6
	push 
	call fact 1
	pop
	print 
	call println 0
	call println 0
	const 10  
	push      
	call fibo 1
	pop
	print
	call println 0
	call println 0
	const 10
	push
	const  2
	push
	call pow 2
	pop
	print
	call println 0
	call println 0
	call loop 0
	halt
label pow
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
label fibo
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
label fact
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
