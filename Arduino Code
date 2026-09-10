void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  
}

void loop() {
 static unsigned long record = 209088;
//  static unsigned long timestampSeconds = 0;
 unsigned long timestampSeconds = millis() / 1000;   //changed
  
  // Create timestamp that advances by 5 seconds each message
  int hh = timestampSeconds / 3600;
  int mm = (timestampSeconds % 3600) / 60;
  int ss = timestampSeconds % 60;
  
  char timestamp[25];
  
  sprintf(
    timestamp,
    "2026-09-10 %02d:%02d:%02d",
    hh,
    mm,
    ss
  );
  
  // timestampSeconds += 20;

  // Randomised values similar to CR3000 file
  float batt = 12.5 + random(-50, 51) / 100.0;   //changed
  
  int pulse1 = random(0, 15);
  int pulse2 = random(0, 15);
  
  float cnr1_1 = random(0, 7000) / 1000.0;
  float cnr1_2 = -random(0, 1000) / 1000.0;
  float cnr1_3 = random(0, 1200) / 1000.0;
  float cnr1_4 = random(-50, 150) / 1000.0;
  
  int pressure = random(820, 840);
  
  float temp1 = random(2650, 2720);
  float temp2 = random(150, 250);

  //Simulate occasional missing battery values
  String battField;
  if(random(0, 20) == 0)
  {
    battField = "";
  }
  else
  {
    battField = String(batt, 2);
  }
  
  // Build CR3000-style line
  String line =
  "\"" + String(timestamp) + "\"," +
  String(record++) + "," +
  battField + "," +
  String(pulse1) + "," +
  String(pulse2) + ",0," +
  String(cnr1_1,3) + "," +
  String(cnr1_2,3) + "," +
  String(cnr1_3,3) + "," +
  String(cnr1_4,3) + ",0," +
  String(pressure) + "," +
  String(temp1,0) + "," +
  String(temp2,1) +
  ",-1";
  
  // Send line
  // Serial.println(line);

  //Send line with Corruption
  if(random(0,50) == 0)
  {
    Serial.println("CORRUPTED");
   }
  else
  {
    Serial.println(line);
  }
  
  // delay(20000);

  // Random gap between messages
  // delay(random(5000, 60000));

 // Droppouts
  int outage = random(0,100);
  
  if(outage < 3)
  {
//    Serial.println("Simulating 10 minute outage");
    delay(600000);
  }
  else if(outage<10)
  {
//    Serial.println("Simulating 2 minute outage");
    delay(120000);
  }
  else
  {
     delay(random(5000, 60000));
  }
 
}
