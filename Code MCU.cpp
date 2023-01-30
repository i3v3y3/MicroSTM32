#include <iostream>
using namespace std;

//input bit values from the OBC//
 int STARTING_IN_4BIT;
 int PAYLOAD_IN_4BIT;
 int UHF_IN_3BIT;
 int XBAND_IN_4BIT;
 int ENDING_IN_2BIT;

//output vales to the OBC//
 const int STARTING_OUT_4BIT = 9;
 int PAYLOAD_OUT_2BIT  = 0; //1 (ON) or 3 (OFF)//
 int UHF_OUT_2BIT      = 0; //1 (ON) or 3 (OFF)//
 int XBAND_OUT_2BIT    = 0; //1 (ON) or 3 (OFF)//
 int CHARGE_OUT_7BIT   = 0;// 0 to 100//
 int TEMP_OUT_8BIT     = 0;// # -128 to 127//
 const int ENDING_OUT_2BIT  = 3; //constant//

//predefined constant commands//

 const int PAYLOAD_ON  = 4;
 const int PAYLOAD_OFF = 6;
 const int UHF_ON      = 1;
 const int UHF_OFF     = 3;
 const int XBAND_ON    = 7;
 const int XBAND_OFF   = 12;

// input values //
 int payload_STATE;
 int uhf_STATE;
 int xband_STATE;
 int battery_CHARGE;
 int battery_TEMPERATURE;
 int RELEASE;
 
int main(){
    
}