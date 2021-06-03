listing = swtbug
source = e000.s19

$(listing).lst: $(listing).info $(source)
	f9dasm -info $(listing).info > $@

	
%.info: %.py
	./$< > $@