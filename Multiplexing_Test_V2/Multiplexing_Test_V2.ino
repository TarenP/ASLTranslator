//---How many potentiometers are connected directly to pins?--
byte NUMBER_POTS = 1;
//---How many potentiometers are connected to a multiplexer?--
byte NUMBER_MUX_POTS = 1;
//************************************************************

//***ANY MULTIPLEXERS? (74HC4067)************************************
//MUX address pins must be connected to Arduino UNO pins 2,3,4,5
//A0 = PIN2, A1 = PIN3, A2 = PIN4, A3 = PIN5
//*******************************************************************
//Mux NAME (OUTPUT PIN, , How Many Mux Pins?(8 or 16) , Is It Analog?);

Mux M1(A0, 8, true); //Analog multiplexer on Arduino analog pin A0

//***DEFINE POTENTIOMETERS CONNECTED TO MULTIPLEXER*******************
//Pot::Pot(Mux mux, byte muxpin, byte command, byte control, byte channel)
//**Command parameter is for future use**

Pot MPO1(M1, 0);

Pot *MUXPOTS[] {&MPO1};


void setup() {
  Serial.begin(9600);
}

void loop() {
  if (NUMBER_MUX_POTS != 0) updateMuxPots();
}


void updateMuxPots() {
  for (int i = 0; i < NUMBER_MUX_POTS; i = i + 1) {
    MUXPOTS[i]->muxUpdate();
    byte potmessage = MUXPOTS[i]->getValue();
    if (potmessage != 255) MIDI.sendControlChange(MUXPOTS[i]->Pcontrol, potmessage, MUXPOTS[i]->Pchannel);
  }
}
