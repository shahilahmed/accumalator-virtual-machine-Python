start mainorg 4096data 1 2 1 3 2 3 -1 ; CONST 2 CONST 3 ADD PRINT HALT	org 2label vm_run	ent 5label vm_loop_start		ldr 0	mva	const -1	ne	brf vm_loop_end	ldr 0	print	const 32	out	lda 0	inc	sta 0	br vm_loop_startlabel vm_loop_end	retlabel println	const 10	out	retlabel main		const 4096	sta   0	const 2048	sta   1	call vm_run 0	call println 0	call println 0	halt