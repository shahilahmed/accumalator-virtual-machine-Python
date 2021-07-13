start main
label println
	const 10
	out
	ret
label main
	org 512
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
	halt