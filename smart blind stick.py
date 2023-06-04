#define trig 2
#define echo 3
int led=4;
float distance;
long duration;
void setup()
{
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);
pinMode(led,OUTPUT);
Serial.begin(9600);
}
void loop()
{
digitalWrite(trig,LOW);
delayMicroseconds(2);
digitalWrite(trig,HIGH);
delayMicroseconds(10);
digitalWrite(trig,LOW);
duration=pulseIn(echo,HIGH);
distance=duration * 0.034/2;
Serial.print("distance");
Serial.print(distance);
Serial.println("CM");
if(distance>100)
  digitalWrite(led,HIGH);
else
digitalWrite(led,LOW);
}