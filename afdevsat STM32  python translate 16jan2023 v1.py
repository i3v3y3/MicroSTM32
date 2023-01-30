"""
OBC master-providing clock signal
"""

START_OUT
position=0
WORD_FROM_OBC=0
WORD_TO_OBC=0

"""
STM32 INPUT FROM OBC
"""
STARTING_IN_4BIT  =
PAYLOAD_IN_4BIT   =
UHF_IN_3BIT       =
XBAND_IN_4BIT     =
ENDING_IN_2BIT    =

"""
STM32 OUTPUT TO OBC
"""
STARTING_OUT_4BIT = 9 #constant
PAYLOAD_OUT_2BIT  = 0 #1 (ON) or 3 (OFF)
UHF_OUT_2BIT      = 0 #1 (ON) or 3 (OFF)
XBAND_OUT_2BIT    = 0 #1 (ON) or 3 (OFF)
CHARGE_OUT_7BIT   = 0 # 0 to 100
TEMP_OUT_8BIT     = 0 # -128 to 127
ENDING_OUT_2BIT   = 3 #constant

"""
PREDEFINED COMMANDS
"""
PAYLOAD_ON  = 4
PAYLOAD_OFF = 6
UHF_ON      = 1
UHF_OFF     = 3
XBAND_ON    = 7
XBAND_OFF   = 12

payload_STATE  = #read from pin powering the payload mosfet
uhf_STATE      = #read from pin powering the uhf mosfet
xband_STATE    = #read from pin powering the xband mosfet
battery_CHARGE = #read from the battery balancing circuit
battery_TEMPERATURE= #read from battery board thermometer circuit

RELEASE = #read from external release switches to determine if satellite is ejected

def read_PIN_SCL_FROM_OBC():
    return 0
def read_PIN_SDA_FROM_OBC():
    return 0
def set_PIN_SDA_TO_OBC(value):
    if (value):
    if (not value):
def payload_ON():
    PAYLOAD_OUT_2BIT=1
    #activate payload supply mosfet
def payload_OFF():
    PAYLOAD_OUT_2BIT=3
    #deactivate payload supply mosfet
def uhf_ON():
    UHF_OUT_2BIT=1
    #activate uhf supply  mosfet
def uhf_OFF():
    UHF_OUT_2BIT=3
    #deactivate uhf supply mosfet
def xband_ON():
    XBAND_OUT_2BIT=1
    #activate xband supply mosfet
def xband_OFF():
    XBAND_OUT_2BIT=3
    #deactivate xband supply mosfet
def RELEASE_ONE():
    #release switch 1, return True  means it's activated
def RELEASE_TWO():
    #release switch 2, return True  means it's activated
def RELEASE_THREE():
    #release switch 3, return True  means it's activated
def RELEASE_FOUR():
    #release switch 4, return True  means it's activated
def deploy_PANELS():
    #activate motors to deploy panels
    
while(True):
    if (position    ==17):position    =0 #0 to 16
    if (position_out==27):position_out=0 #0 to 26
    if (read_PIN_SCL_FROM_OBC()) :
        sda = read_PIN_SDA_FROM_OBC()
        if(  sda   ) : WORD_FROM_OBC = (WORD_FROM_OBC | (  1<<(16-position) ))
        if(not sda ) : WORD_FROM_OBC = (WORD_FROM_OBC & (~(1<<(16-position))))
        set_PIN_SDA_TO_OBC( WORD_TO_OBC & (1<<(26-position)) )
        if( ((WORD_FROM_OBC>>13) == STARTING_IN_4BIT) and ((WORD_FROM_OBC&3) == ENDING_IN_2BIT) ):#start and end
            if( ((WORD_FROM_OBC>>9)&15) == PAYLOAD_ON  ): payload_ON()
            if( ((WORD_FROM_OBC>>9)&15) == PAYLOAD_OFF ): payload_OFF()
            if( ((WORD_FROM_OBC>>6)&7 ) == UHF_ON      ): uhf_ON()
            if( ((WORD_FROM_OBC>>6)&7 ) == UHF_OFF     ): uhf_OFF()
            if( ((WORD_FROM_OBC>>2)&15) == XBAND_ON    ): xband_ON()
            if( ((WORD_FROM_OBC>>2)&15) == XBAND_OFF   ): xband_OFF()
    if(RELEASE_ONE and RELEASE_TWO and RELEASE_THREE and RELEASE_FOUR): deploy_PANELS()
    WORD_TO_OBC = (STARTING_OUT_4BIT<<23) | (payload_STATE<<18) | (uhf_STATE<<20) | (xband_STATE<<20)| (battery_CHARGE<<10) | (battery_TEMPERATURE<<2) | ENDING_OUT_2BIT
    while( read_PIN_SCL_FROM_OBC() ):#Pause        
    position     = position+1
    position_out = position_out+1

