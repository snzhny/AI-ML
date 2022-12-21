#define LED 10
#define LED2 9

int val;
String relay;

void setup() {

Serial.begin(9600);
pinMode (LED, OUTPUT);
pinMode (LED2, OUTPUT);
}

void loop() {
if (Serial.available()) {
  val = Serial.read();
  if(val != 10)
  switch(val){
    case '1':
      for(int j = 0; j < 1; j++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(j == 0){ relay = "1";}
        }
      Serial.println(relay);
      break;
    case '2':
      for(int i=0; i<2; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 1){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '3':
      for(int i=0; i<3; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 2){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '4':
      for(int i=0; i<4; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 3){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '5':
      for(int i=0; i<5; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 4){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '6':
      for(int i=0; i<6; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 5){ relay = "1";}
      }
      Serial.println(relay);
        break;
    case '7':
      for(int i=0; i<7; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 6){ relay = "1";}
      }
      Serial.println(relay);
        break;
    case '8':
      for(int i=0; i<8; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 7){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '9':
      for(int i=0; i<9; i++){
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(500);
        relay = "0";
        if(i == 8){ relay = "1";}
      }
      Serial.println(relay);
      break;
    case '0':
      digitalWrite(LED, LOW);
      digitalWrite(LED2, LOW);
      break;
    case 'w':
      for(int i=0; i<3; i++){
        digitalWrite(LED2, HIGH);
        delay(100);
        digitalWrite(LED2, LOW);
        delay(100);
      }
      break;
  }
  
}
  

  
}