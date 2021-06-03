#!/usr/bin/env python3

import info




l = info.LabelList()

l.source('e000.s19')
l.processor('6800')


# Vectors.

l.add(0xE18B, 'SFE')
l.add(0xE1A7, 'NMI')
l.add(0xE0D0, 'START')

# RAM area

l.add(0xA000, 'IRQ')
l.add(0xA002, 'BEGA')
l.add(0xA004, 'ENDA')
l.add(0xA006, 'NMI')
l.add(0xA008, 'SP')
l.add(0xA00A, 'PORADD')
l.add(0xA00C, 'PORECH')
l.add(0xA00D, 'XHI')
l.add(0xA00E, 'XLOW')
l.add(0xA00F, 'CKSM')
l.add(0xA010, 'XTEMP')
l.add(0xA012, 'SWIJMP')
l.add(0xA014, 'BKPT')
l.add(0xA016, 'BKLST')
l.add(0xA044, 'TW')
l.add(0xA046, 'TEMP')
l.add(0xA047, 'BYTECT')
l.add(0xA042, 'STACK')


# PIO

l.add(0x8007, 'PIASB')
l.add(0x8006, 'PIADB')
l.add(0x8005, 'PIAS')
l.add(0x8004, 'PIAD')

# Other

l.add(0xC000, 'PROM')

# Subroutines

l.add(0xE000, 'IRQV', 'I/O INTERRUPT SEQUENCE')
l.add(0xE005, 'JUMP', 'JUMP TO USER PROGRAM')
l.add(0xE009, 'CURSOR', 'CT-1024 CURSOR CONTROL', data=3)
l.add(0xE00C, 'LOAD', 'ASCII LOADING ROUTINE')
l.add(0xE011, type='char')
l.add(0xE017, type='char')
l.add(0xE01B, type='char')

l.add(0xE30B, 'RDON')


l.add(0xE067, 'OUTHL', 'OUT HEX LEFT BCD DIGIT')
l.add(0xE06B, 'OUTHR', 'OUT HEX RIGHT BCD DIGIT')
l.add(0xE075, 'OUTCH', 'OUTPUT ONE CHAR')
l.add(0xE078, 'INCH', 'INPUT ONE CHAR')
l.add(0xE0AA, 'INHEX', 'INPUT HEX CHAR')
l.add(0xE0AC, 'INHEX2')
l.add(0xE0BE, 'IN1HG')
l.add(0xE0BF, 'sE0BF', 'OUTPUT 2 HEX CHAR')
l.add(0xE1AC, 'INEEE', 'INPUT ONE CHAR INTO A-REGISTER')
l.add(0xE1D1, 'OUTEEE', 'OUTPUT ONE CHAR')
l.add(0xE00f, 'LOAD3')
l.add(0xE044, 'LOAD21')
l.add(0xE055, 'BYTE', 'INPUT BYTE (TWO FRAMES)')
l.add(0xE047, 'BADDR', "BUILD ADDRESS")
l.add(0xE02B, 'LOAD11')
l.add(0xE03B, 'LOAD15')
l.add(0xE040, 'LOAD19', type='char')

l.add(0xE2A0, 'CONTRL')

l.add(0xE31C, 'CTRLS', "OUTPUT CTRL CHARS")
l.add(0xE320, 'CTRLR')
l.add(0xE324, 'CTRLT')
l.add(0xE328, 'PCTRL')

l.add(0xE20D, 'OUTEEE1', 'REAL OUTEEE')
l.add(0xE1D3, 'SAV', 'SAVE X REGISTER')

l.add(0xE1E0, 'sE1E0', '(unknown)')

l.add(0xE101, 'AL1', 'CONTINUE POWER UP SEQUENCE')

l.add(0xE416, 'TABLE', 'COMMAND TABLE')
for a in range(0xE416, 0xE416+45, 3):
    l.add(a, data = 1)
    l.add(a, type = 'char:1')
    l.add(a+1, data = 2)
    l.add(a+1, type = 'word:2')

l.add(0xE276, type="const:2")



if __name__ == "__main__":

    print(l)




"""

* RAM OS area

* Subroutines

label   E047    sE047
label   E055    sE055
label   E057    sE057





label   E07E    sE07E





label   E0C8    sE0C8
label   E0CA    sE0CA
label   E0CC    sE0CC


comment E1D1
comment E1D1

label   E1D3    sE1D3
label   E1D6    sE1D6
label   E1D9    sE1D9
label   E1EE    sE1EE
label   E1F6    sE1F6
label   E25A    sE25A
label   E25E    sE25E
label   E263    sE263
label   E265    sE265
label   E27D    sE27D
label   E284    sE284
label   E28F    sE28F
label   E292    sE292
label   E2D4    sE2D4
label   E2E2    sE2E2
label   E30B    sE30B
label   E31C    sE31C
label   E320    sE320
label   E324    sE324
label   E328    sE328
label   E32F    sE32F
label   E332    sE332
label   E3AF    sE3AF
label   E3B9    sE3B9
label   E3BF    sE3BF

label   E0FC    C1
label   E14A    C1a

"""
