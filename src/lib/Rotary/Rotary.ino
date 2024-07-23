// Define pin for step (pulse) and dir (direction)

int step = 7;
int dir = 8;
int incoming = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(step, OUTPUT);
  pinMode(dir, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){

    incoming = Serial.read();

    if (incoming == 112){
      digitalWrite(step, HIGH); // sets the digital pin 7 on
      delay(2);            // waits for a second
      digitalWrite(step, LOW);  // sets the digital pin 7 off
      delay(2); 

    }

  }

  
}
