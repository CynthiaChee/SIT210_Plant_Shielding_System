int led = D4;
int buzzer = D2;

// The following line is optional, but recommended in most firmware. It
// allows your code to run before the cloud is connected. In this case,
// it will begin blinking almost immediately instead of waiting until
// breathing cyan,
SYSTEM_THREAD(ENABLED);

// The setup() method is called once when the device boots.
void setup()
{
	pinMode(led, OUTPUT);
	pinMode(buzzer, OUTPUT);
	Particle.subscribe("light", alert, ALL_DEVICES); // subscribes to the event "light" to alert when it is published
}

// blinks the LED
void blink_led()
{
    digitalWrite(led, HIGH);
	delay(500);
	digitalWrite(led, LOW);
	delay(500);
}

// activates the buzzer
void buzzer_sound()
{
    tone(buzzer, 2000, 500);
    delay(1000);
}

// alerts the user by blinking the LED and playing the buzzer
void alert(const char *event, const char *data)
{
    blink_led();
    blink_led();
    blink_led();
    buzzer_sound();
    buzzer_sound();
    buzzer_sound();
}

// The loop() method is called frequently.
void loop()
{
}