#include "Freenove_WS2812_SPI.h"

//Freenove_WS2812_SPI strip = Freenove_WS2812_SPI(8, TYPE_GRB);//led_count, led_type
Freenove_WS2812_SPI strip = Freenove_WS2812_SPI();//led_count=8, led_type=TYPE_GRB

void Ctrl_C_Handler(int value)
{
    strip.end();
    exit(0);
}

int main(int argc, char *argv[])
{
    //Ctrl+C Event
    signal(SIGINT, Ctrl_C_Handler);  
    
    //Init ledpixel
    strip.begin();
    strip.setBrightness(20);
    strip.setLedType((LED_TYPE)TYPE_GRB);
    
    while(true)
    {
        //some tips
        if(argc == 1)
        {
            printf("The use of ledpixel:\n");
            printf("  please enter ./main RGB\n");
            printf("  please enter ./main Rainbow\n");
            printf("  please enter ./main Breathing\n\n");
            exit(0);
        }
        else if(argc == 2 && strncmp(argv[1], "RGB", 3) == 0)
        {
            unsigned int i = 0, color_index = 0;
            unsigned int colors[]={0xFF0000,0x00FF00,0x0000FF,0xFFFF00,0xFF00FF,0x00FFFF,0xFFFFFF};
            for(color_index=0; color_index < sizeof(colors)/sizeof(colors[0]); color_index++)
            {         
                for(i=0;i<strip.getLedCount();i++)
                {
                    strip.setLedColor(i, colors[color_index]);
                    usleep(10000);
                }
                strip.show();
                usleep(500000);
            }
        }
        else if(argc == 2 && strncmp(argv[1], "Rainbow", 7) == 0)
        {
            for (int j = 0; j < 255; j += 2) {
                for (int i = 0; i < strip.getLedCount(); i++) {
                    strip.setLedColorData(i, strip.Wheel((i * 256 / strip.getLedCount() + j) & 255));
                }
                strip.show();
                usleep(10000);
            }  
        }
        else if(argc == 2 && strncmp(argv[1], "Breathing", 9) == 0)
        {
            unsigned int colors[]={0xFF0000,0x00FF00,0x0000FF,0xFFFF00,0xFF00FF,0x00FFFF,0xFFFFFF};
            for(unsigned int color_index=0; color_index < sizeof(colors)/sizeof(colors[0]); color_index++)
            {
                for(unsigned int br=0;br<50;br++)
                {
                    strip.setBrightness(br);
                    strip.setAllLedsColorData(colors[color_index]);
                    strip.show();
                    usleep(10000);
                }
                for(unsigned int br=50;br>0;br--)
                {
                    strip.setBrightness(br);
                    strip.setAllLedsColorData(colors[color_index]);
                    strip.show();
                    usleep(10000);
                }
            }
        }
    }
    return 0;
}
