  Throat-Cutter

This is a program to monitor the internet connection.                                                                                                
      The tester will consist of the following items:                                                                                                     
                                                                                                                                                          
            RasPi Pico                                                                                                                                    
            128x32 Oled display                                                                                                                           
            2 relays to switch power to Modem and Router                                                                                                  
            Led Indicator/s  - 1x Neopixel and 1x RGB led                                                                                                                              
            Pushbutton test switches x 2   
            uSD card for logging
            NTP connection for accurate logging

Design notes:                                                                                                                                             
        make the boot wait time approx 1 minute                                                                                                             
                                                                                                                                                                  
                                                                                                                                                           
        a switch sets the Mode. Modes are:   Reboot Modem :   The associated relay switches off and beeps, then on.                                        
                                             Reboot Router:   The associated relay switches off and beeps, then on.                                        
                                             Auto         :   The internet is connected and monitored                                                      
                                                              The internet is booting - no activity                                                        
                                                              The internet is waiting for SSID response, but not yet connected                             
        buzzer tweeps when internet is depowered                                                                                                            
        buzzer tweeps when internet is repowered                                                                                                            
        a 64 x 128 LCD displays relevant info                                                                                                                        
                                                                                                                                                           
        The device will operate in the following manner:                                                                                                   
            The device turns on the relays to power the modem and router display a sign-on on the lcd     LCD message  1                                   
            The device will wait for 20 seconds                                                                                                            
            The device will try to the WLAN, router and a network device                                                                                   
            When it connects, it will give a LCD message.                                                                                                   
            Pings will occur every 30 seconds to ensure connection                                                                                         
            If it loses connection, it will wait 30 seconds to try again, twice                                                                            
            After 3 retrys, it will disconnect power for 3 seconds, then go throught the power-up sequence                                                 
            The addresses pinged are:                                                                                                                      
                WLAN      :  1.1.1.1       (Cloud Flare)            Green                                                                                  
                LAN       :  192.168.1.254 (Router address)         Red                                                                                    
                Network   :  192.168.1.70  (PiHole)                 Blue    
      All events are logged to the uSD card in CSV format.
                
